import re


class Ingredient:
    expression = r"[0-9]+[ .,]?[0-9]*?[ .]?[%]"
    expression_compilee = re.compile(expression)

    def __init__(self, name, ingredient_string, percent=None, children=None):
        if children is None:
            children = []
        self.name = name
        self.percent = percent
        self.children = children
        self.ingredient_string = ingredient_string
        if not self.children:
            self.parse_string()

    def __repr__(self):
        return "name: " + self.name + ", percent: " + str(self.percent) + ", children: " + str(self.children)

    def parse_string(self):
        if self.ingredient_string:
            # TODO - Sophie owner
            stack = []
            start = None

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
                    if not self.ingredient_string[i+1].isdigit():
                        if len(stack) == 0:
                            name = self.ingredient_string[start:i]
                            self.children.append(Ingredient(name, None))
                            start = None
                elif i == len(self.ingredient_string) - 1:
                    if self.ingredient_string[i] == ".":
                        name = self.ingredient_string[start:i]
                    else:
                        name = self.ingredient_string[start:i + 1]
                    self.children.append(Ingredient(name, None))

    def add_children(self, split_string):

        for child in split_string:
            self.children.append(Ingredient("key", "string"))

        return True

    def update_percent(self):
        # if il y a un pourcentage et un if il y a pas de pourcentage
        self.percent_from_name()

        # ajout du percentage 100 pour top ingredient
        if not self.percent:
            self.percent = 100


        self.get_children_percentage()


    def get_children_percentage(self):
        """detection des groupes et appeler les fonctions correspondantes"""
        if len(self.children) > 0:
            pass

    def get_percent_begin(self, j, percent_right):
        """assigner les pourcentages sur le groupe tout devant"""
        pass

    def get_percent_middle(self, i, j, percent_left, percent_right):
        """assigner les pourcentages sur un groupe au milieu"""
        pass

    def get_percent_end(self, i, percent_left):
        """Assigner les pourcentages sur le groupe de la fin (par moitié du précédent)"""
        pass

    def check_percent(self):
        """check que la somme de tous les pourcentages fassent bien 100% """

    def percent_from_name(self):
        """
        Look for percent string in name and assign it to ingredient
        Finally call same method to all children
        :return:
        """
        if Ingredient.expression_compilee.search(self.name) is not None:
            self.percent_from_name()
            regex = Ingredient.expression_compilee.search(self.name)
            index_to_delete = int(regex[0].find('%'))  # renvoie une liste comprenant l'element cherché
            resultat = regex[0][0:index_to_delete]  # on supprime le sigle pourcentage
            resultat = float(resultat.replace(",", "."))
            self.name = self.name[:regex.start()].strip()
            self.percent = resultat
        for child in self.children:
            child.percent_from_name()

    def __repr__(self):
        return "name: " + self.name + ", percent: " + str(self.percent) + ", " + str(self.children)

# # Camille
# # if __name__ == '__main__':
# #     pizza = Ingredient("pizza ", "garniture 65,7% (fromage 50%, tomate 12%, fraise 8%), pate 44,3% "
# #                                  "(farine 90%, eau 10%)", percent=100,
# #                        children=[Ingredient("garniture 65,7%", "garniture 65,7% (fromage 50%, tomate 12%, fraise 8%)",
# #                                             children=[Ingredient("fromage 50%", "fromage 50%"),
# #                                                       Ingredient("tomate 12%", "tomate 12%"),
# #                                                       Ingredient("fraise 8,3%", "fraise 8%")]),
# #                                  Ingredient("pate 44,3%", "(farine 90%, eau 10%)",
# #                                             children=[Ingredient("farine 90%,", "farine 90%,"),
# #                                                       Ingredient("eau 10%,", "eau 10%,")])])
# #     print(pizza)
# #     pizza.update_percent()
# #     print(pizza)

# Sophie
if __name__ == "__main__":
    test = Ingredient("Crumble aux fruits rouges - Picard - 170 g", "Garniture aux fruits rouges 67,1% (fruits rouges 60% (griotte, groseille, cassis, mûre, framboise), eau, sucre, fécule de manioc, épaississants (farine de graines de caroube, gomme de xanthane)), pâte à crumble 32,9% (farine de blé, beurre, sucre, chapelure (farine de blé, eau, dextrose de blé et/ou maïs, levure, huile de colza, sel, colorants (extrait de paprika et de curcuma), sirop de glucose de blé et/ou de maïs))")
    test2 = Ingredient("Gratin de pomme de terre, oignon, comté surgelé - Picard - 220 g", "Pomme de terre précuite 38%, eau, oignon 14,2%, comté (contient lait) 8,6%, crème fraîche liquide (lait) 6,5%, lait entier en poudre, beurre (lait), fécule de pomme de terre, sel, épaississant : gomme xanthane, poivre blanc.")
    test3 = Ingredient("test",
                      "Farine de BLE 27%, sucre, huile de colza, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")

    print(test)
    print(test2)
    print(test3)
    print(len(test3.children))

    # test.display_ingredients()
