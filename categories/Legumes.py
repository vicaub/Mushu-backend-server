from Product import Product
legumes = Product('Legume', None)

tomate = Product('tomate', None,
                 [Product('sauce tomate', 2.9),
                  Product('tomate fraiche hors saison', 2.2),
                  Product("tomate fraîche saison", 0.3),
                  Product("tomate destinée à l'industrie", 0.5),
                  Product('tomate pelées', 1.4),
                  Product('pulpe de tomate', 1.4),
                  Product('tomate fraiche importée', 0.6)])