from Ingredient import Ingredient
from Product import Product
from categories import fruits, legumes, poissons, produits_laitiers, viandes
from fuzzywuzzy import process


class Matching:
    def __init__(self):
        products = [
            fruits.fruit,
            legumes.legumes,
            poissons.poissons,
            produits_laitiers.produits_laitiers,
            viandes.viandes
        ]

        self.database = Product("database", None, products)

    def browse_database(self, openfoodfact_ingredient, ingredient):
        best_result = process.extractOne(openfoodfact_ingredient, {ingredient: ingredient.name})

        if ingredient.children and len(ingredient.children) > 0:
            for child in ingredient.children:
                child_best_score = process.extractOne(openfoodfact_ingredient, {child: child.name})
                if child_best_score[1] > best_result[1]:
                    best_result = child_best_score
            return best_result
        else:
            return None




    def match_ingredient(self, openfoodfact_ingredient):
        # openfoodfact_ingredient -> product in database
        best_choice = self.browse_database(openfoodfact_ingredient, self.database)

        return best_choice[2]

    def compute_footprint(self, ingredient):
        """match ingredient names with db and sum cft with percent"""

        footprint = 0

        # match children ingredients with database
        if ingredient.children and len(ingredient.children) > 0:
            for child in ingredient.children:
                footprint += self.compute_footprint(child) * child.percent


        # get footprint for them

        # sum footprints with percentage

        return 0.12


if __name__ == "__main__":
    matching = Matching()
    ingredient_names = [
        "griotte",
        # "groseille",
        # "farine de graines de caroube",
        # "sucre",
        # "sirop de glucose de blé et/ou de maïs",
        # "eau",
        # "Farine de blé",
        # "pulpe de tomate",
        "mozzarella",
        "jambon cru fumé speck",
        "viande de porc",
        "roquette"
    ]

    for openfoodfact_ingredient in ingredient_names:
        print(openfoodfact_ingredient)
        print(matching.match_ingredient(openfoodfact_ingredient))

    garniture = Ingredient("garniture", None, 50)
    pate = Ingredient("pate à pizza", None, 50)

    tomate = Ingredient("sauce tomate", None, 50)
    mozzarella = Ingredient("mozzarella", None, 50)
    farine = Ingredient("farine de blé", None, 100)

    garniture.children = [tomate, mozzarella]
    pate.children = [farine]

    pizza = Ingredient("pizza", None, 100)

    pizza.children = [garniture, pate]

    matching.compute_footprint(pizza)

