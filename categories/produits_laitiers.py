from models.Product import Product

produits_laitiers = Product("Produit Laitier Oeuf", None,
                            [Product("Produit Laitier", None,
                                     [
                                         Product("Yaourt", 3.22),
                                         Product("Lait", None,
                                                 [
                                                     Product("Lait", 1.56),
                                                     Product("Lait semi-écrémé pasteurisé", 1.20),
                                                     Product("Lait coco", 4.12),
                                                     Product("Lait soja", 2.15),
                                                     Product("Lait d'amande", 0.90)
                                                 ]),
                                         Product("Beurre Margarine", None,
                                                 [
                                                     Product("Beurre doux", 9.84),
                                                     Product("Margarine", 1.74)
                                                 ]),
                                         Product("Fromage", None,
                                                 [
                                                     Product("Fromage frais", None,
                                                             [
                                                                 Product("Fromage blanc", 3.85),
                                                                 Product("Fromage frais", 3.50),
                                                                 Product("Fromage frais vache", 3.85),
                                                                 Product("Fromage frais chèvre", 3.95)
                                                             ]),
                                                     Product("Fromage pâte dure", 5.94),
                                                     Product("Fromage pâte molle", 4.62),
                                                     Product("Fromage sec chèvre", 5.76),
                                                     Product("mozzarella")
                                                 ]),
                                         Product("Crème", None,
                                                 [
                                                     Product("Crème pasteurisée", 4.2),
                                                     Product("Crème", 4.5)
                                                 ])
                                     ]),
                             Product("Oeuf", None,
                                     [
                                         Product("Oeuf moyen", 1.76),
                                         Product("Oeuf catégorie 0 biologique", 1.52),
                                         Product("Oeuf catégorie 1 plein air", 2.13),
                                         Product("Oeuf catégorie 2 sol", 2.32),
                                         Product("Oeuf catégorie 3 cage", 1.76)
                                     ]),
                             ])
