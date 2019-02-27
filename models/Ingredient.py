import re
from fuzzywuzzy import process as fuzzy


class Ingredient:
    expression = r"[0-9]+[ .,]?[0-9]*?[ .]?[%]"
    expression_compilee = re.compile(expression)
    stop_liste_expression = r"(sel|sodium|trace)|([a-z][0-9]{3}|[a-z][0-9]{3}[a-z])"
    stop_liste_expression_compilee = re.compile(stop_liste_expression)

    def __init__(self, name, ingredient_string, percent=None, children=None):
        if children is None:
            children = []
        self.name = name.replace("_", "")
        self.percent = percent
        self.children = children
        self.match = None
        self.ingredient_string = ingredient_string
        if not self.children:
            self.parse_string()

    def parse_string(self):
        """
        analyse the ingredient string attribute and generate children according to it
        parenthesis are considered as children delimiters
        """
        if self.ingredient_string:
            # TODO - Sophie owner
            stack = []
            start = None
            # on remplace les éventuels œ par oe
            self.ingredient_string = self.ingredient_string.replace("œ", "oe")
            for i in range(len(self.ingredient_string)):
                if type(start) != int:
                    if self.ingredient_string[i].isalpha():
                        start = i
                elif self.ingredient_string[i] == '(':
                    # on entre dans une parenthèse
                    stack.append(i)
                elif self.ingredient_string[i] == ')':
                    # on sort d'une parenthèse
                    i_open_bracket = stack.pop()
                    if len(stack) == 0:
                        # cela signifie qu'on a matché toutes les parenthèses ouvrantes précédentes
                        if self.ingredient_string[i_open_bracket - 1] == " ":
                            ingr_name = self.ingredient_string[start:i_open_bracket - 1]
                        else:
                            ingr_name = self.ingredient_string[start:i_open_bracket]

                        ingr_substring = self.ingredient_string[i_open_bracket + 1:i]
                        self.children.append(Ingredient(ingr_name, ingr_substring))
                        start = None
                elif self.ingredient_string[i] == ',':
                    if not self.ingredient_string[i + 1].isdigit():
                        if len(stack) == 0:
                            # si je ne suis pas au milieu de parenthèses
                            # on ajoute un ingrédient dans les enfants
                            name = self.ingredient_string[start:i]
                            self.children.append(Ingredient(name, None))
                            start = None
                elif i == len(self.ingredient_string) - 1:
                    if self.ingredient_string[i] == ".":
                        name = self.ingredient_string[start:i]
                    else:
                        name = self.ingredient_string[start:i + 1]
                    self.children.append(Ingredient(name, None))

    # def add_children(self, split_string):
    #     for child in split_string:
    #         self.children.append(Ingredient("key", "string"))
    #
    #     return True

    def update_percent(self):
        # if il y a un pourcentage et un if il y a pas de pourcentage
        self.assign_percent_from_name()

        # ajout du percentage 100 pour top ingredient
        if not self.percent:
            self.percent = 100

        self.assign_children_percentage()

        self.rectify_total_percent()

    def assign_children_percentage(self):
        """
        detection des groupes et appeler les fonctions correspondantes
        :return:
            begin group: index of last child without percent before child with percent (-1 if not exists)
            middle group: list of (i, j) with i index of child without percent and i-1 with percent, j child without percent and j + 1 with
            end group: index of last child with percent + 1
        """

        if len(self.children) > 0:

            # getting begin_group
            begin_group = -1  # index of last child in begin group
            for i in range(len(self.children)):
                if self.children[i].percent:
                    break
                else:
                    begin_group = i

            # getting end group
            end_group = len(self.children)  # index of first end group index
            for i in range(len(self.children) - 1, -1, -1):
                if self.children[i].percent:
                    break
                else:
                    end_group = i

            # getting middle groups
            middle_groups = []
            prev_percent_child = None  # left border of current middle group
            next_percent_child = None  # right border of current middle group
            for i in range(begin_group + 1, end_group):
                if self.children[i].percent:
                    if prev_percent_child is None:
                        # initialize left border
                        prev_percent_child = i
                    elif next_percent_child is None:
                        # found right border so a new middle group
                        next_percent_child = i
                        middle_groups.append((prev_percent_child + 1, next_percent_child - 1))
                        prev_percent_child = i
                        next_percent_child = None

            if end_group == 0:
                # there is no percentage in the ingredient string
                self.assign_percent_end(end_group, 100)
            else:
                for middle_indexes in middle_groups:
                    self.assign_percent_middle(middle_indexes[0],
                                               middle_indexes[1],
                                               self.children[middle_indexes[0] - 1].percent,
                                               self.children[middle_indexes[1] + 1].percent)
                if end_group < len(self.children):
                    self.assign_percent_end(end_group, self.children[end_group - 1].percent)

                if len(self.children) - 1 > begin_group > -1:
                    self.assign_percent_begin(begin_group, self.children[begin_group + 1].percent)

            for child in self.children:
                child.assign_children_percentage()

            # for testing purpose
            return begin_group, middle_groups, end_group

    def assign_percent_begin(self, j, percent_right):
        """
        assigner les pourcentages sur le groupe tout devant
        """
        total_percent = 0
        # compute total percent assigned
        for child in self.children:
            if child.percent:
                total_percent += child.percent

        if float((100 - total_percent) / (j + 1)) >= percent_right:
            # we have enough percentage left to distribute to front ingredients
            if j == 0:
                self.children[0].percent = 100 - total_percent

            else:
                percent_avg = (float((100 - total_percent) / (j + 1)) + percent_right) / 2
                self.children[j].percent = percent_avg
                self.assign_percent_begin(j - 1, percent_avg)
        else:
            # we don't have enough percentage left
            # There will be a extra amount of percentage that will be corrected by rectify_total_percent
            # delta = ((percent_right - float((100 - total_percent)/(j+1)))*(j+1))*1.5
            # l = len(self.children)
            # for child in self.children:
            # if child.percent:
            #     child.percent -= delta * (child.percent / total_percent)
            # self.assign_percent_begin(j, self.children[j+1].percent)
            self.children[j].percent = percent_right
            if j > 0:
                self.assign_percent_begin(j - 1, percent_right)

    def assign_percent_middle(self, i, j, percent_left, percent_right):
        """
        assigner les pourcentages sur un groupe au milieu
        """
        if j - i + 1 > 0:
            if percent_left > percent_right:
                # calcul de la moyenne
                average = (percent_left + percent_right) / 2
                # si j'ai un nombre impair de pourcentages à assigner
                if (j - i + 1) % 2 == 1:
                    # calcul de l'indice du milieu
                    i_middle = i + (j - i) // 2
                    # j'alloue le pourcentage à l'ingrédient du milieu
                    self.children[i_middle].percent = average
                    # j'applique récursivement si ce que je viens de traiter avait plus d'un élément
                    if j - i + 1 > 1:
                        self.assign_percent_middle(i, i_middle - 1, percent_left, average)
                        self.assign_percent_middle(i_middle + 1, j, average, percent_right)

                # si j'ai un nombre pair de pourcentages à assigner:
                else:
                    # si je n'ai que 2 ingrédient alors j'assigne un pourcentage
                    if j - i + 1 == 2:
                        average_left = (percent_left + average) / 2
                        average_right = (average + percent_right) / 2
                        self.children[i].percent = average_left
                        self.children[j].percent = average_right
                    # sinon je fais un appel récursif
                    else:
                        self.assign_percent_middle(i, i + (j - i) // 2, percent_left, average)
                        self.assign_percent_middle(i + (j - i) // 2 + 1, j, average, percent_right)
            else:
                # left percent < right percent il y a un probleme
                for k in range(i, j + 1):
                    self.children[k].percent = 0

    def assign_percent_end(self, i, percent_left):
        """
        Assigner les pourcentages sur le groupe de la fin (par moitié du précédent)
        i est le premier ingrédient auquel on doit assigner un pourcentage
        """
        stop_liste_to_put = ["sel", "acidifiant", "conservateur", "emulisfient", "émulsifiants", "dextrose",
                             "correcteur d'acidité", "lactosérum", "acidifiants", "acidifiant", "antioxydants",
                             "antioxydant", "antibiotique", "stabilisants", "stabilisants", "stabilisant", "arôme",
                             "arômes", "colorants", "colorant", "contient", "enzyme", "épaississant", "édulcorants",
                             "édulcorant", "diphosphates", "sodium", "extrait"]

        stop_index = None
        for l in range(i, len(self.children)):
            if fuzzy.extractOne(self.children[l].name.lower(), stop_liste_to_put)[1] < 89:
                if Ingredient.stop_liste_expression_compilee.search(self.children[l].name.lower()) is None:
                    # rajouter la fonction de victor qui utilise la stop_liste_to_put
                    self.children[l].percent = float(percent_left / 2)
                    percent_left = self.children[l].percent
                    # print("nom: ", self.children[l].percent, "pourcentage assigné", percent_left)
                else:
                    stop_index = l
                    break
            else:
                stop_index = l
                break
        if stop_index:
            #print("nous avous supprimons les éléments suivants: ", self.children[stop_index:])
            self.children = self.children[:stop_index]
            # print("les enfants restants sont: ", self.children)

    def rectify_total_percent(self):
        """
        check que la somme de tous les pourcentages fassent bien 100%
        """
        total_percent = 0
        for child in self.children:
            total_percent += child.percent
        if total_percent != 100:
            for child in self.children:
                child.percent /= total_percent / 100

        for child in self.children:
            child.rectify_total_percent()

    def assign_percent_from_name(self):
        """
        Look for percent string in name and assign it to ingredient
        Finally call same method to all children
        :return:
        """
        if Ingredient.expression_compilee.search(self.name) is not None:
            regex = Ingredient.expression_compilee.search(self.name)
            index_to_delete = int(regex[0].find('%'))  # renvoie une liste comprenant l'element cherché
            resultat = regex[0][0:index_to_delete]  # on supprime le sigle pourcentage
            resultat = float(resultat.replace(",", "."))
            self.name = self.name[:regex.start()].strip()
            self.percent = resultat
        for child in self.children:
            child.assign_percent_from_name()

    def __repr__(self):
        percent_string = ""
        if self.percent:
            percent_string = ", percent: " + str(self.percent)
        children_string = ""
        if self.children:
            children_string = ", " + str(self.children)
        match_string = ""
        if self.match:
            match_string = ", match: " + str(self.match)

        return "name: " + self.name + percent_string + match_string + children_string
