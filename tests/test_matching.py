import unittest

from Ingredient import Ingredient
from Matching import Matching
from categories.produits_laitiers import produits_laitiers
import categories.viandes as viandes


class TestMatching(unittest.TestCase):

    def test_browse_database(self):
        matching = Matching()

        fromage_product = produits_laitiers.children[0].children[3]
        score1, expected_fromage = matching.browse_database("fromage", matching.database)

        self.assertEqual(fromage_product, expected_fromage)

        score2, expected_fromage2 = matching.browse_database("fromage", produits_laitiers)

        self.assertEqual(fromage_product, expected_fromage2)

        self.assertEqual(score1, score2)

        score3, expected_match = matching.browse_database("fromage", viandes.viandes)

        self.assertEqual(expected_match, viandes.volaille.children[2].children[0])

        self.assertGreater(score1, score3)

        self.assertNotEqual(matching.browse_database("fromage", matching.database),
                            matching.browse_database("viande", matching.database))

    def test_match_ingredient(self):
        matching = Matching()

        fromage_product = produits_laitiers.children[0].children[3]

        self.assertEqual(fromage_product, matching.match_ingredient("fromae"))

        self.assertEqual(fromage_product, matching.match_ingredient("fromae latier"))

        self.assertNotEqual(fromage_product, matching.match_ingredient("jambon de porc"))

    def test_compute_footprint(self):
        matching = Matching()

        chou_fleur_ingredient = Ingredient("chou-fleur", "", percent=100)

        self.assertEqual(matching.compute_footprint(chou_fleur_ingredient), 0.5)

        fromage_ingredient = Ingredient("fromage", "", percent=100)

        self.assertEqual(matching.compute_footprint(fromage_ingredient), 5.44)

        fromage_ingredient = Ingredient("fromage", "", percent=50)

        self.assertEqual(matching.compute_footprint(fromage_ingredient), 5.44 / 2)

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

        self.assertEqual(matching.compute_footprint(pizza), 3.042)


if __name__ == "__main__":
    unittest.main()
