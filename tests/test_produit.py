from Product import Product

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

var = viandes.viande
