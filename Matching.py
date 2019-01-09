from Ingredient import Ingredient
from Product import Product
from categories import fruits, legumes, poissons, produits_laitiers, viandes
from fuzzywuzzy import process


class Matching:
    """
    Utility class to compute carbon footprints of Ingredient objects by comparing them to Product database
    """

    def __init__(self):
        products = [
            fruits.fruits,
            legumes.legumes,
            poissons.poissons,
            produits_laitiers.produits_laitiers,
            viandes.viandes
        ]

        self.database = Product("database", None, products)

    def browse_database(self, ingredient_name, product):
        """
        :param ingredient_name: ingredient string from openfoodfact to match with product
        :param product: product object to be browse for matching with ingredient (start with full Product database)
        :return: tuple object (best matching score, product object that correspond to best match)
        """
        if product.children and len(product.children) > 0:
            best_score, best_product = process.extractOne(ingredient_name, product.convert_to_dict())[1:3]
            for child in product.children:
                child_best_score, child_best_product = self.browse_database(ingredient_name, child)
                if child_best_score > best_score:
                    best_product = child_best_product
                    best_score = child_best_score
            return best_score, best_product
        else:
            return 0, None

    def match_ingredient(self, ingredient_name):
        """
        :param ingredient_name: string ingredient name to match with product names in db
        :return: Best Product object match with ingredient_name
        """
        best_score, best_product = self.browse_database(ingredient_name, self.database)
        print("ingredient", ingredient_name, "score", best_score, "product", best_product)

        return best_product

    def compute_footprint(self, ingredient_obj):
        """
        Match ingredient names with db and sum cft with percent
        :param ingredient_obj: Ingredient object with all children and percentages already parsed
        :return: total footprint for this ingredient in carbon kg/product kg
        """
        footprint = 0

        if ingredient_obj.children and len(ingredient_obj.children) > 0:
            # iterate function over all children and apply percentages
            for child in ingredient_obj.children:
                footprint += self.compute_footprint(child) * child.percent / 100
        else:
            # when bottom ingredient match ingredient with product in db
            match_ingredient = self.match_ingredient(ingredient_obj.name)
            footprint += match_ingredient.cfp

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
    pizza2 = Ingredient("fromage", "garniture 65,7% (fromage 50%, tomate 12%, fraise 8%), pate 44,3% "
                                "(farine 90%, eau 10%)", percent=100)
    matching = Matching()

    footprint = matching.compute_footprint(pizza)
    print("footprint", footprint)
