from Product import Product


produit_laitier = Product("Produit Laitier et Oeuf", None ,
                    [ Product("Produit Laitier", None,
                              [
                                  Product("Yaourt", 3.22),
                                  Product("Lait", None,
                                    [
                                        Product("Lait", 1.56),
                                        Product("Lait semi-écrémé pasteurisé", 1.20)
                                    ]),
                                  Product("Beurre et Margarine", None,
                                    [
                                        Product("Beurre doux", 9.84),
                                        Product("Margarine", 1.74)
                                    ]),
                                  Product("Fromage", None,
                                    [
                                        Product("Fromage frais", None, 
                                          [
                                              Product("Fromage blanc", 3.85),
                                              Product("Fromage frais 58%", 3.50),
                                              Product("Fromage frais de vache", 3.85),
                                              Product("Fromage frais de chèvre", 3.95)
                                          ]),
                                        Product("Fromage à pâte dure", 5.94),
                                        Product("Fromage à pâte molle", 4.62),
                                        Product("Fromage sec de chèvre", 5.76)
                                    ]),
                                  Product("Crème", None, 
                                    [
                                        Product("Crème 40% MG pasteurisée", 4.2),
                                        Product("Crème", 4.5)
                                    ])
                              ]),
                      Product("oeuf", None,
                              [
                                  Product("Oeuf moyen", 1.76),
                                  Product("Oeuf catégorie 0 biologique", 1.52),
                                  Product("Oeuf catégorie 1 en plein air", 2.13),
                                  Product("Oeuf catégorie 2 au sol", 2.32),
                                  Product("Oeuf catégorie 3 en cage", 1.76)
                              ]),
                      ]);