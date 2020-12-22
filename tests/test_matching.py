import unittest

from server.categories.database import database
from server.models.Ingredient import Ingredient
from server.models.Matching import Matching
from server.categories.produits_laitiers import produits_laitiers
import server.categories.viandes as viandes


class TestMatching(unittest.TestCase):

    def test_browse_database(self):
        fromage_product = produits_laitiers.children[0].children[3]
        matching1 = Matching(fromage_product)
        score1, expected_fromage = matching1.browse_database("fromage", database)
        self.assertEqual(fromage_product, expected_fromage)

        score2, expected_fromage2 = matching1.browse_database("fromage", produits_laitiers)
        self.assertEqual(fromage_product, expected_fromage2)
        self.assertEqual(score1, score2)

        score3, expected_match = matching1.browse_database("fromage", viandes.viandes)
        self.assertEqual(expected_match, viandes.volaille.children[2].children[0])
        self.assertGreater(score1, score3)
        self.assertNotEqual(matching1.browse_database("fromage", database),
                            matching1.browse_database("viande", database))

        score3, expected_match = matching1.browse_database("Produit soufflé à base de pomme de terre", database)

    def test_match_ingredient(self):
        fromage_product = produits_laitiers.children[0].children[3]
        matching = Matching(fromage_product)

        self.assertEqual(fromage_product, matching.match_ingredient("fromae"))

        self.assertEqual(fromage_product, matching.match_ingredient("fromae latier"))

        self.assertNotEqual(fromage_product, matching.match_ingredient("jambon de porc"))

    def test_compute_footprint(self):
        chou_fleur_ingredient = Ingredient("chou-fleur", None, percent=100)
        matching1 = Matching(chou_fleur_ingredient)
        self.assertEqual(matching1.compute_footprint(), 0.5)

        fromage_ingredient = Ingredient("fromage", None, percent=100)
        matching2 = Matching(fromage_ingredient)
        self.assertEqual(matching2.compute_footprint(), 5.44)
        self.assertEqual(fromage_ingredient.match, matching2.match_ingredient("fromage"))

        fromage_ingredient = Ingredient("fromage", None, percent=50)
        matching3 = Matching(fromage_ingredient)
        self.assertEqual(matching3.compute_footprint(), 5.44 / 2)

        pizza = Ingredient("pizza", "", percent=100,
                           children=[Ingredient("garniture", "", percent=60,
                                                children=[
                                                    Ingredient("fromage", "", percent=50),
                                                    Ingredient("sauce tomate", "", percent=20)
                                                ]),
                                     Ingredient("pate", "", percent=20,
                                                children=[
                                                    Ingredient("sporc,", "", percent=90),
                                                ])
                                     ])
        matching4 = Matching(pizza)
        self.assertEqual(matching4.compute_footprint(), 3.042)


if __name__ == "__main__":
    unittest.main()
