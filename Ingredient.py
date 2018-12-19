import re

class Ingredient:

    def __init__(self, name, ingredient_string, percent=None, children=[]):
        self.name = name
        self.percent = percent
        self.children = children
        self.ingredient_string = ingredient_string

        #split_string = self.parse_string(ingredient_string)
        #self.add_children(split_string)

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
        self.percent = 60.0

    def display_ingredients(self):
        print("*********")
        if self.children != None:
           for el in self.children:
               el.display_ingredients
        else:
            print(self.name)


if __name__ == "__main__":
    test = Ingredient("test", "Garniture aux fruits rouges (griotte (eau, sucre), groseille, cassis, mûre, framboise), pâte à crumble (farine de blé, eau), acidifiant, colorant")
    test.parse_string(test.ingredient_string)


    print("***" + test.children[0].name)
    print("***" + test.children[1].name)
    print("***", test.children[0].ingredient_string)
    print(test.children[1].ingredient_string)
    print(test.children[2].name)
    print(test.children[3].name)
