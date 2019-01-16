from Product import Product
import unittest

from categories import produits_laitiers, poissons

legume1 = Product("courgette", None)
legume2 = Product("poivron", 1.3)
legume3 = Product("oignon", 0, [legume1, legume2])

try:
    Product(1)
    raise Exception("TypeError expected")
except TypeError:
    pass

try:
    Product("aubergine", "12")
    raise Exception("TypeError expected")
except TypeError:
    pass

try:
    Product("aubergine", 12, 3)
    raise Exception("TypeError expected")
except TypeError:
    pass

import categories.viandes as viandes

var = viandes.viandes


class TestMatching(unittest.TestCase):

    def test_get_cfp(self):
        fromage_product = produits_laitiers.produits_laitiers.children[0].children[3]

        self.assertEqual(fromage_product.cfp, 5.44)

        truite_product = poissons.poissons.children[1]

        self.assertEqual(truite_product.cfp, 4.2)

if __name__ == "__main__":
    unittest.main()

