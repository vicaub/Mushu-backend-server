from models.Product import Product
from categories.database import database
from fuzzywuzzy import process as fuzzy
from fuzzywuzzy import fuzz

class Matching:
    """
    Utility class to compute carbon footprints of Ingredient objects by comparing them to Product database
    """

    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.matches = []

    def browse_database(self, ingredient_name, product):
        """
        :param ingredient_name: string ingredient name to match with product names in product and product children
        :param product: product object to be browse for matching with ingredient (start with full Product database)
        :return: tuple object (best matching score, product object that correspond to best match)
        """
        if product.children and len(product.children) > 0:
            best_score, best_product = fuzzy.extractOne(ingredient_name, product.convert_to_dict())[1:3]
            for child in product.children:
                child_best_score, child_best_product = self.browse_database(ingredient_name, child)
                if child_best_score > best_score:
                    best_product = child_best_product
                    best_score = child_best_score
                elif best_score != 0 and child_best_score == best_score:
                    if fuzz.ratio(ingredient_name, best_product.name) < fuzz.ratio(ingredient_name, child_best_product.name):
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
        best_score, best_product = self.browse_database(ingredient_name, database)

        # self.matches.append({ingredient_name: (best_product.name, best_product.cfp)})

        return best_product

    def compute_footprint(self):
        """
        Match ingredient names with db and sum cft with percent
        :param ingredient_obj: Ingredient object with all children and percentages already parsed
        :return: total footprint for this ingredient in carbon kg/product kg
        """
        footprint = 0

        if self.ingredient.children and len(self.ingredient.children) > 0:
            # iterate function over all children and apply percentages
            for child in self.ingredient.children:
                footprint += Matching(child).compute_footprint()
        else:
            # when bottom ingredient match ingredient with product in db
            product = self.match_ingredient(self.ingredient.name)
            self.ingredient.match = product
            footprint += product.cfp

        return footprint * self.ingredient.percent / 100
