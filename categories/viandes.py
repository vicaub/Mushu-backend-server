from Product import Product

# VIANDE

## VOLAILLE

volaille = Product("volaille", 1.07, [
    Product("poulet", 3.71, [
        Product("blanc de poulet", 4.8),
        Product("poulet roti entier", 3.6),
        Product("cuisse de poulet", 4.1)
    ]),
    Product("dinde", 7.83, [
        Product("cuisse de dinde", 5.3),
        Product("blanc de dinde", 6.3)
    ]),
    Product("canard", 5.8, [
        Product("magret", 9.75),
    ])
])

## boeuf

boeuf = Product("boeuf", 28.6, [
    Product("cote de boeuf", 34.94)
])

## VEAU

veau = Product("veau", 16.4)

## PORC

porc = Product("porc", 5.9, [
    Product("lardon", 4.5),
    Product("saucisse de porc", 4.4),
    Product("saucisson de porc", 5.1),
    Product("Filet mignon de porc", 5.11),
    Product("jambon")
])

## LAPIN

lapin = Product("lapin", 4.9)

## AGNEAU

agneau = Product("agneau", 25.58, [
    Product("cotelette d'agneau", 33),
    Product("gigot d'agneau", 34.69)
])

viandes = Product("viande", children=[volaille, boeuf, veau, porc, lapin, agneau])
