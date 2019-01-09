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

        #split_string = self.parse_string(ingredient_string)
        #self.add_children(split_string)

    def __repr__(self):
        return "name: " + self.name + ", percent: " + str(self.percent) + ", children: " + str(self.children)


    def parse_string(self, ingredient_string):
        # TODO - Sophie owner

        stack = []
        start = None

        for i in range(len(ingredient_string)):
            if type(start) != int:
                if ingredient_string[i].isalpha():
                    start = i
            elif ingredient_string[i] == '(':
                # on entre dans une parenthèse
                stack.append(i)
            elif ingredient_string[i] == ')':
                # on sort d'une parenthèse
                i_open_bracket = stack.pop()
                if len(stack) == 0:
                    # cela signifie qu'on a matché toutes les parenthèses ouvrantes précédentes
                    ingr_name = ingredient_string[start:i_open_bracket]
                    ingr_substring = ingredient_string[i_open_bracket + 1:i]
                    self.children.append(Ingredient(ingr_name, ingr_substring))
                    start = None
            elif ingredient_string[i] == ',':
                if len(stack) == 0:
                    name = ingredient_string[start:i]
                    self.children.append(Ingredient(name, None))
                    start = None
            elif i == len(ingredient_string) - 1:
                name = ingredient_string[start:i + 1]
                self.children.append(Ingredient(name, None))


    def add_children(self, split_string):

        for child in split_string:
            self.children.append(Ingredient("key", "string"))

        return True


    def update_percent(self):
        #TODO - Camille owner
        # if il y a un pourcentage et un if il y a pas de pourcentage
        if not self.percent:
            if Ingredient.expression_compilee.search(self.name) is not None:
                self.percent_from_name()
            else:
                self.percent_from_nothing()
        if self.children and len(self.children) > 0:
            # pass
            for child in self.children:
                child.update_percent()

    def complete_percent_after(self):
        # pour remplir les self.children qui n'ont pas de pourcentage en fonction des autres.
        pass

    def percent_from_nothing(self):
        if len(self.children) >= 5:
            self.children[0].percent = 40
            self.children[1].percent = 20
            self.children[2].percent = 20
            self.children[3].percent = 10
            self.children[4].percent = 10
            for i in range(5, len(self.children)):
                self.children[i].percent = 0
        elif len(self.children) >= 2:
            self.children[0].percent = 60
            self.children[1].percent = 40
            for i in range(2, len(self.children)):
                self.children[i].percent = 0
        elif  len(self.children) > 0:
            self.children[0].percent = 80

    def percent_from_name(self):
        regex = Ingredient.expression_compilee.search(self.name)
        index_to_delete = int(regex[0].find('%'))  # renvoie une liste comprenant l'element cherché
        resultat = regex[0][0:index_to_delete]  # on supprime le sigle pourcentage
        resultat = float(resultat.replace(",", "."))
        self.name = self.name[:regex.start()].strip()
        self.percent = resultat

    def display_ingredients(self):
        print("*********")
        if self.children != None:
           for el in self.children:
               el.display_ingredients
        else:
            print(self.name)


# if __name__ == "__main__":
#     test = Ingredient("test", "Garniture aux fruits rouges (griotte (eau, sucre), groseille, cassis, mûre, framboise), pâte à crumble (farine de blé, eau), acidifiant, colorant")
#     test.parse_string(test.ingredient_string)
#
#     print("***" + test.children[0].name)
#     print("***" + test.children[1].name)
#     print("***", test.children[0].ingredient_string)
#     print(test.children[1].ingredient_string)
#     print(test.children[2].name)
#     print(test.children[3].name)

if __name__ == '__main__':
    pizza = Ingredient("pizza ", "garniture 65,7% (fromage 50%, tomate 12%, fraise 8%), pate 44,3% "
                                          "(farine 90%, eau 10%)",percent=100,
                       children=[Ingredient("garniture 65,7%", "(fromage 50%, tomate 12%, fraise 8%)",
                                            children=[Ingredient("fromage 50%", "fromage 50%"),
                                                      Ingredient("tomate 12%", "tomate 12%"),
                                                      Ingredient("fraise 8,3%", "fraise 8%")]),
                                 Ingredient("pate 44,3%", "(farine 90%, eau 10%)",
                                            children=[Ingredient("farine 90%,","farine 90%,"),
                                                    Ingredient("eau 10%,", "eau 10%,")])])
    print(pizza)
    pizza.update_percent()
    print(pizza)

