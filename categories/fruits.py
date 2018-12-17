from Product import Product


fruit = Product("fruit", None ,
                [ Product("Pomme", None,
                          [
                              Product("pomme france", 0.3),
                              Product("Pomme amérique du Sud", 1.3)
                          ]),
                  Product("Abricot", None,
                          [
                              Product("Abricot saison (France)", 0.3),
                              Product("Abricot 'Pays du Sud'",0.5)
                          ]),
                  Product("peche", None,
                          [
                              Product("peche france", 0.3),
                              Product("Pêche 'Pays du Sud'", 0.5)
                          ]),
                  Product("Fruit", None,
                          [
                              Product("Fruit ou légume moyen de saison, produit localement", 0.3),
                              Product('Fruit ou légume moyen importé par bateau et camion', 1.3),
                              Product("Fruit ou légume moyen, hors saison produit sous serre chauffée", 2.2),
                              Product("Fruit ou légume moyen , importé par avion (saison ou hors saison)", 21.9)
                          ]),
                  Product("Melon", 0.3),
                  Product("citron", 0.5),
                  Product("poire", None,
                          [
                              Product("poire belgique", 0.5),
                              Product("poire argentine", 0.9)
                          ]),
                  Product("orange", None,
                          [
                              Product("Orange destinée à l'industrie", 0.5),
                              Product("orange", 0.5)
                        ]),
                  Product("fraise", None,
                          [
                              Product("fraise saison (france)", 0.6),
                              Product("fraise 'pays du sud", 0.8),
                              Product("Fraise hors saison sous serre (France)", 3.4)
                          ]),
                  Product("Raisin", 0.6),
                  Product("mandarine", 0.8)
                  Product("banane", 0.7),
                  Product("cerise", 0.7),
                  Product("noix", 0.7),
                  Product("Amande", 2.9)
                  Product("mangue", None,
                          [
                              Product("mangue importée par bateau", 0.7),
                              Product("mangue importée par avion", 21.9)
                  ])
                ])