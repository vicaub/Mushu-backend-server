import re

class Ingredient:

    expression = r"[0-9]+[ .,]?[0-9]*?[ .]?[%]"
    expression_compilee = re.compile(expression)

    def __init__(self, name, ingredient_string, percent=None, children=[]):
        self.name = name
        self.percent = percent
        self.children = children
        self.ingredient_string = ingredient_string

        #split_string = self.parse_string(ingredient_string)
        #self.add_children(split_string)

    def parse_string(self, ingredient_string):
        # TODO - Sophie owner
        split_string = {"pate à pizza": "blé, ...", "garniture": "tomate, ..."}

        return split_string

    def add_children(self, split_string):

        for child in split_string:
            self.children.append(Ingredient("key", "string"))

        return True


    def update_percent(self):
        #TODO - Camille owner
        # if il y a un pourcentage et un if il y a pas de pourcentage
        if self.percent is None:
            if Ingredient.expression_compilee.search(self.name) is not None:
                self.percent_from_name()
                print("le pourcentage a été assigné")
        else: # a appliquer une fois qu'on a parser toutes la listes
            #il faut faire en sorte de les attribuer alléatoirement
            for i in range(len(self.children)):
                self.percent_from_nothing()
                if self.children[i].children is not None:
                    pass

            pass

    def percent_from_nothing(self):
        if len(self.children) >= 5:
            self.children[0].percent = 40
            self.children[1].percent = 20
            self.children[2].percent = 20
            self.children[3].percent = 10
            self.children[4].percent = 10
        elif len(self.children) >= 2:
            self.children[0].percent = 60
            self.children[1].percent = 40
        else:
            self.children[0].percent = 80

    def percent_from_name(self):
        regex = Ingredient.expression_compilee.search(self.name)
        index_to_delete = int(regex[0].find('%'))  # renvoie une liste comprenant l'element cherché
        resultat = regex[0][0:index_to_delete]  # on supprime le sigle pourcentage
        resultat = float(resultat.replace(",", "."))
        self.percent = resultat


if __name__ == '__main__':
    pizza = Ingredient("garniture 65,7%", "tomate 12%")
    a = pizza.update_percent()
    print(pizza.percent)