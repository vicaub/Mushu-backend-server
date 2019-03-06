from models.Product import Product

epicerie = Product("Épicerie", None, [
    Product("Asaisonnement", None, [
        Product("Huiles", None, [
            Product("Huile d'olive", 2.66),
            Product("Huile colza", 2.30),
            Product("Huile tournesol", 2.88),
            Product("Huile palme")
        ]),
        Product("Vinaigre de vin", 4.23)
    ]),
    Product("Épices", None, [
        Product("Sucres", None,
                [Product("Sucre", 2.17),
                 Product("Dextrose", None)
                 ]),
        Product("glucose", 1.816),
        Product("Sel", 0.60),
        Product("Poivre", 3.42),
        Product("Ail", 0.54),
        Product("Canelle", 2.50),
        Product("Cumin", 2.50),
        Product("Curry", 2.50),
        Product("Gingembre", 2.50),
        Product("Gousse vanille", 3.61),
        Product("Persil", 2.50),
        Product("Piment", 3.67),
        Product("Anis Badiane", 3.41),
        Product("Basilic", 2.87),
        Product("Ciboulette", 2.87),
        Product("Coriandre", 2.87),
        Product("Menthe", 2.87),
        Product("Thym", 2.87),
        Product("Autres épices", 3.19),
        Product("Origan", None)
    ]),
    Product("Sauces", None, [
        Product("Ketchup", 2.70),
        Product("Moutarde", 3.58)
    ]),
    Product("Céréales", 1.87, [
        Product("Blé", None, [
            Product("Farines", None, [
                Product("Farine blé", 1.23),
                Product("Farine sarrasin", 1.23),
                Product("Farine seigle", 1.23)
            ]),
            Product("Levures", None, [
                Product("Levure liquide", 0.67),
                Product("Levure pressée", 1.04),
                Product("Levure sèche", 3.51)
            ]),
            Product("Pains", None, [
                Product("Pain blanc", 1.58),
                Product("Pain complet", 1.58)
            ]),
            Product("Amidon", None)
        ]),
        Product("Avoine")
    ]),
    Product("Féculents", None, [
        Product("Pâtes sèches", 1.54),
        Product("Riz sec", 3.30),
        Product("Semoule sèche", 2.80),
        Product("Quinoa", 2.03),
        Product("Soja", 2.80),
        Product("Tofu", 2.80),
        Product("Autre céréale", 3.03)
    ]),
    Product("Biscuits et sucreries", None, [
        Product("Biscottes", 1.83),
        Product("Biscuit beurre", 4.81),
        Product("Brioche", 2.59),
        Product("Brioche industrielle", 3.18),
        Product("Cake", 5.42),
        Product("Croissant", 2.59),
        Product("Confiture d'abricot", 1.22),
        Product("Confiture fraise", 3.95),
        Product("Compote fruit", 0.80),
        Product("Glace", 2.40),
        Product("Pain chocolat", 2.34),
        Product("Pâte tarte", 7.35),
        Product("Salade fruits de saison", 0.80),
        Product("Tarte pommes", 1.63),
        Product("Tarte fraises", 4.20),
        Product("Miel", 1.92),
        Product("Chocolats", None, [
            Product("Chocolat lait en morceaux", 6.86),
            Product("Chocolat blanc en morceaux", 6.86),
            Product("Chocolat poudre", 5.70),
            Product("Chocolat noir morceaux", 5.87),
            Product("Cacao", None)
        ])
    ])
])
