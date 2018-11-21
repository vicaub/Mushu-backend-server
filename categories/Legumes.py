from Produit import Produit
legumes = Produit('Legume', None)

tomate = Produit('tomate', None,
                 [Produit('sauce tomate', 2.9),
                  Produit('tomate fraiche hors saison', 2.2),
                  Produit("tomate fraîche saison", 0.3),
                  Produit("tomate destinée à l'industrie", 0.5),
                  Produit('tomate pelées', 1.4),
                  Produit('pulpe de tomate', 1.4),
                  Produit('tomate fraiche importée', 0.6)])