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
        :param ingredient_name: string ingredient name to match with product names in product and product children
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
                footprint += self.compute_footprint(child)
        else:
            # when bottom ingredient match ingredient with product in db
            match_ingredient = self.match_ingredient(ingredient_obj.name)
            footprint += match_ingredient.cfp

        return footprint * ingredient_obj.percent / 100
