import unittest
from Ingredient import Ingredient


# test parsing

class TestIngredient(unittest.TestCase):

    def test_parsing(self):
        test = Ingredient("test",
                          "Farine de BLE 27%, sucre, huile de colza, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")

        self.assertEqual(8, len(test.children))
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

    def test_assign_children_percentage(self):
        test1 = Ingredient("test",
                           "Farine de BLE 27%, sucre, huile de colza, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")
        test1.assign_percent_from_name()
        begin, middle, end = test1.assign_children_percentage()

        self.assertEqual(-1, begin)
        self.assertEqual(1, end)
        self.assertEqual(0, len(middle))

        test4 = Ingredient("test4",
                           "CHOCOLAT SUPÉRIEUR AU LAIT (SUCRE, LAIT EN POUDRE, BEURRE DE CACAO, PÂTE DE CACAO, ÉMULSIFIANTS : LÉCITHINES (SOJA), VANILLINE), LAIT ÉCRÉMÉ EN POUDRE 12%, SUCRE, GRAISSES VÉGÉTALES, BEURRE concentré 1%, ÉMULSIFIANTS : LÉCITHINES (soja), VANILLINE")

        test4.assign_percent_from_name()
        begin, middle, end = test4.assign_children_percentage()

        self.assertEqual(0, begin)
        self.assertEqual(5, end)
        self.assertEqual([(2, 3)], middle)

    def test_assign_percent_from_name(self):
        test1 = Ingredient("test",
                           "Farine de BLE 27%, sucre, huile de colza 10%, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")

        test1.assign_percent_from_name()
        self.assertEqual(27.0, test1.children[0].percent)
        self.assertEqual(None, test1.children[1].percent)
        self.assertEqual(10.0, test1.children[2].percent)
        self.assertEqual(None, test1.children[3].percent)
        self.assertEqual(None, test1.children[7].percent)

        test2 = Ingredient("test2",
                           "Pomme de terre précuite 38%, eau, oignon 14,2%, comté (contient lait) 8,6%, crème fraîche liquide (lait) 6,5%, lait entier en poudre, beurre (lait), fécule de pomme de terre, sel, épaississant : gomme xanthane, poivre blanc.")

        test2.assign_percent_from_name()
        self.assertEqual(38.0, test2.children[0].percent)
        self.assertEqual(None, test2.children[1].percent)
        self.assertEqual(14.2, test2.children[2].percent)
        # self.assertEqual(8.6, test2.children[3].percent)
        self.assertEqual(None, test2.children[3].children[0].percent)

    def test_assign_percent_end(self):
        test1 = Ingredient("test",
                           "Farine de BLE 27%, sucre, huile de colza 10%, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")

        test1.assign_percent_end(3, 10.0)
        self.assertEqual(5.0, test1.children[3].percent)
        self.assertEqual(2.5, test1.children[4].percent)
        self.assertEqual(len(test1.children), 5)

    def test_middle_percent(self):
        test = Ingredient("test", "fruit rouge 60%, eau, épaississant 1%")
        i_start = 0
        i_final = 2
        test.children[i_start].percent = 60
        test.children[i_final].percent = 1
        test.assign_percent_middle(i_start + 1, i_final - 1, test.children[i_start].percent,
                                   test.children[i_final].percent)
        self.assertEqual(30.5, test.children[1].percent)

        test2 = Ingredient("test", "fruit rouge 60%, épaississant 1%")
        i_start = 0
        i_final = 1
        test2.children[i_start].percent = 60
        test2.children[i_final].percent = 1
        test2.assign_percent_middle(i_start + 1, i_final - 1, test2.children[i_start].percent,
                                    test2.children[i_final].percent)
        self.assertEqual(60, test2.children[0].percent)
        self.assertEqual(1, test2.children[1].percent)

        test3 = Ingredient("test", "fruit rouge 60%, eau, farine de blé, épaississant 1%")
        i_start = 0
        i_final = 3
        test3.children[i_start].percent = 60
        test3.children[i_final].percent = 1
        test3.assign_percent_middle(i_start + 1, i_final - 1, test3.children[i_start].percent,
                                    test3.children[i_final].percent)
        self.assertEqual(45.25, test3.children[1].percent)
        self.assertEqual(15.75, test3.children[2].percent)

        test4 = Ingredient("test", "fruit rouge 60%, eau, farine de blé, lait, épaississant 1%")
        i_start = 0
        i_final = 4
        test4.children[i_start].percent = 60
        test4.children[i_final].percent = 1
        test4.assign_percent_middle(i_start + 1, i_final - 1, test4.children[i_start].percent,
                                    test4.children[i_final].percent)
        self.assertEqual(45.25, test4.children[1].percent)
        self.assertEqual(30.5, test4.children[2].percent)
        self.assertEqual(15.75, test4.children[3].percent)

        test5 = Ingredient("test", "fruit rouge 60%, eau, farine de blé, lait, framboise, épaississant 1%")
        i_start = 0
        i_final = 5
        test5.children[i_start].percent = 60
        test5.children[i_final].percent = 1
        test5.assign_percent_middle(i_start + 1, i_final - 1, test5.children[i_start].percent,
                                    test5.children[i_final].percent)
        self.assertEqual(52.625, test5.children[1].percent)
        self.assertEqual(37.875, test5.children[2].percent)
        self.assertEqual(23.125, test5.children[3].percent)
        self.assertEqual(8.375, test5.children[4].percent)

        test6 = Ingredient("test", "fruit rouge 60%, eau, farine de blé, lait, framboise, groseille, épaississant 1%")
        i_start = 0
        i_final = 6
        test6.children[i_start].percent = 60
        test6.children[i_final].percent = 1
        test6.assign_percent_middle(i_start + 1, i_final - 1, test6.children[i_start].percent,
                                    test6.children[i_final].percent)
        self.assertEqual(52.625, test6.children[1].percent)
        self.assertEqual(37.875, test6.children[2].percent)
        self.assertEqual(30.5, test6.children[3].percent)
        self.assertEqual(23.125, test6.children[4].percent)
        self.assertEqual(8.375, test6.children[5].percent)

    def test_rectify_total_percent(self):
        test = Ingredient("test", "fruit rouge 60%, eau, épaississant 1%")
        test.update_percent()

        self.assertEqual(test.percent, 100)
        self.assertAlmostEqual(test.children[0].percent, 65.57, places=2)
        self.assertAlmostEqual(test.children[1].percent, 33.33, places=2)
        self.assertAlmostEqual(test.children[2].percent, 1.09, places=2)


        test = Ingredient("test", "fruit rouge 60%, eau 39%, épaississant 1%")
        test.update_percent()

        self.assertEqual(test.percent, 100)
        self.assertEqual(test.children[0].percent, 60)
        self.assertEqual(test.children[1].percent, 39)
        self.assertEqual(test.children[2].percent, 1)


        test = Ingredient("test", "fruit rouge 40% (pomme 30%, cerise 20%), eau 20%, épaississant 10%")
        test.update_percent()

        self.assertEqual(test.percent, 100)
        self.assertAlmostEqual(test.children[0].percent, 57.14, places=2)
        self.assertEqual(test.children[0].children[0].percent, 60)
        self.assertEqual(test.children[0].children[1].percent, 40)
        self.assertAlmostEqual(test.children[1].percent, 28.57, places=2)
        self.assertAlmostEqual(test.children[2].percent, 14.29, places=2)

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
