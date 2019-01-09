import unittest
from Ingredient import Ingredient


# test parsing

class TestIngredient(unittest.TestCase):

    def test_parsing(self):
        test = Ingredient("test",
                          "Farine de BLE 27%, sucre, huile de colza, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")

        self.assertEqual(8,len(test.children))
        self.assertEqual("Farine de BLE 27%", test.children[0].name)
        self.assertEqual("poudres à lever : diphosphates et carbonates de sodium", test.children[7].name)

        test2 = Ingredient("test2",
                           "Pomme de terre précuite 38%, eau, oignon 14,2%, comté (contient lait) 8,6%, crème fraîche liquide (lait) 6,5%, lait entier en poudre, beurre (lait), fécule de pomme de terre, sel, épaississant : gomme xanthane, poivre blanc.")

        self.assertEqual(11, len(test2.children))
        self.assertEqual("Pomme de terre précuite 38%", test2.children[0].name)
        self.assertEqual("poivre blanc", test2.children[10].name)
        self.assertEqual("contient lait", test2.children[3].children[0].name)

        test3 = Ingredient("test3",
                          "Garniture aux fruits rouges 67,1% (fruits rouges 60% (griotte, groseille, cassis, mûre, framboise), eau, sucre, fécule de manioc, épaississants (farine de graines de caroube, gomme de xanthane)), pâte à crumble 32,9% (farine de blé, beurre, sucre, chapelure (farine de blé, eau, dextrose de blé et/ou maïs, levure, huile de colza, sel, colorants (extrait de paprika et de curcuma), sirop de glucose de blé et/ou de maïs))")

        self.assertEqual(2, len(test3.children))
        self.assertEqual(5, len(test3.children[0].children))
        self.assertEqual(5, len(test3.children[0].children[0].children))
        self.assertEqual("épaississants", test3.children[0].children[4].name)
        self.assertEqual("pâte à crumble 32,9%", test3.children[1].name)
        self.assertEqual("extrait de paprika et de curcuma", test3.children[1].children[3].children[6].children[0].name)

        test4 = Ingredient("test4",
                           "CHOCOLAT SUPÉRIEUR AU LAIT 47% (SUCRE, LAIT EN POUDRE, BEURRE DE CACAO, PÂTE DE CACAO, ÉMULSIFIANTS : LÉCITHINES (SOJA), VANILLINE), LAIT ÉCRÉMÉ EN POUDRE, SUCRE, GRAISSES VÉGÉTALES, BEURRE concentré, ÉMULSIFIANTS : LÉCITHINES (soja), VANILLINE")

        self.assertEqual(7, len(test4.children))
        self.assertEqual("SOJA", test4.children[0].children[4].children[0].name)
        self.assertEqual("ÉMULSIFIANTS : LÉCITHINES", test4.children[5].name)

if __name__ == '__main__':
    unittest.main()

# test percents



# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()