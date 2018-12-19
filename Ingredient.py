
class Ingredient:

    def __init__(self, name, ingredient_string, percent=None):
        self.name = name
        self.percent = percent
        self.children = []
        self.ingredient_string = ingredient_string

        split_string = self.parse_string(ingredient_string)
        self.add_children(split_string)

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
        self.percent = 60.0


