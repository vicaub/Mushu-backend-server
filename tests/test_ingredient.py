import unittest
from Ingredient import Ingredient


# test parsing

class TestIngredient(unittest.TestCase):

    def test_parsing(self):
        test = Ingredient("test",
                          "Farine de BLE 27%, sucre, huile de colza, OEUFS entiers, sirop de sucre inverti, sel, arôme naturel, poudres à lever : diphosphates et carbonates de sodium.")
        test.parse_string()

        self.assertEqual(len(test.children), 8)
        self.assertEqual(test.children[0].name, "Farine de BLE 27%")
        self.assertEqual(test.children[7].name, "poudres à lever : diphosphates et carbonates de sodium.")



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