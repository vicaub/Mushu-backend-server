from server.models.Product import Product

boissons = Product("Boissons", None,
                   [Product("Boissons chaudes", None,
                            [Product("Café", 4.14),
                             Product("Thé", 7.10),
                             Product("Soupe", 3.25)
                             ]),
                    Product("Boissons froides", None,
                            [Product("Eau", None,
                                     [Product("Eau robinet", 0.04),
                                      Product("Eau bouteille", 0.45)
                                      ]),
                             Product("Jus", None,
                                     [Product("Jus d'orange", 2.28),
                                      Product("Jus pomme", 1.19),
                                      Product("Jus poire", 2.03),
                                      Product("Jus fruit", 2.28)
                                      ]),
                             Product("Boissons gazeuzes", None,
                                     [Product("Soda", 1.39),
                                      Product("Eau gazeuse", 1.39),
                                      ]),
                             Product("Alcool", None,
                                     [Product("Alcool pur", 1.56),
                                      Product("Champagne", 2.99),
                                      Product("Bière", 2.72),
                                      Product("Vin", 1.21),
                                      Product("Vodka"),
                                      Product("Whiskey"),
                                      Product("Cidre")
                                      ])
                             ])
                    ])
