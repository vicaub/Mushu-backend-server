from Ingredient import Ingredient
from Product import Product
from categories import fruits, legumes, poissons, produits_laitiers, viandes
from fuzzywuzzy import process


class Matching:
    def __init__(self):
        products = [
            fruits.fruits,
            legumes.legumes,
            poissons.poissons,
            produits_laitiers.produits_laitiers,
            viandes.viandes
        ]

        self.database = Product("database", None, products)


    def browse_database(self, ingredient, product):
        """
        :param ingredient: ingredient string from openfoodfact to match with product
        :param product:
        :return: product from database that match the best with openfoodfact ingredient
        """
        if product.children and len(product.children) > 0:
            best_result = process.extractOne(ingredient, product.convert_to_dict())
            for child in product.children:
                child_best_score = self.browse_database(ingredient, child)
                if child_best_score[1] > best_result[1]:
                    best_result = child_best_score
            return best_result
        else:
            return None, 0

    def match_ingredient(self, ingredient):
        """
        :param ingredient: string input of ingredient to match with db
        :return: Best Product object match with string input
        """
        best_choice = self.browse_database(ingredient, self.database)

        return best_choice[2].cfp

    def compute_footprint(self, ingredient):
        """
        Match ingredient names with db and sum cft with percent
        :param ingredient: Ingredient object with all children and percentages
        :return: total footprint for this ingredient
        """
        footprint = 0

        # match children ingredients with database
        if ingredient.children and len(ingredient.children) > 0:
            for child in ingredient.children:
                footprint += self.compute_footprint(child) * child.percent / 100
        else:
            match_ingredient = self.match_ingredient(ingredient.name)
            footprint += match_ingredient

        return footprint


if __name__ == "__main__":

    pizza = Ingredient("pizza", "garniture 65,7% (fromage 50%, tomate 12%, fraise 8%), pate 44,3% "
                                "(farine 90%, eau 10%)", percent=100,
                       children=[Ingredient("garniture", "(fromage 50%, tomate 12%, fraise 8%)", percent=65.7,
                                            children=[Ingredient("fromage", "fromage 50%", percent=50),
                                                      Ingredient("tomate", "tomate 12%", percent=12),
                                                      Ingredient("fraise", "fraise 8%", percent=8)]),
                                 Ingredient("pate", "(farine 90%, eau 10%)", percent=44.3,
                                            children=[Ingredient("farine,", "farine 90%,", percent=90),
                                                      Ingredient("eau,", "eau 10%,", percent=10)])])
    matching = Matching()

    footprint = matching.compute_footprint(pizza)
    print("footprint", footprint)
