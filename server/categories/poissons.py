from server.models.Product import Product

poissons = Product("poisson", children=[
    Product("poisson", 3.49, [
        Product("poisson sauvage", None, [
            Product("poisson sauvage entier", 5.5),
            Product("poisson sauvage filet", 9.2),
        ])
    ]),
    Product("truite", 4.2, [
        Product("truite entiere", None, [
            Product("truite elevage entière", 2.9),
        ]),
        Product("pave de truite", 5.2),
        Product("truite fumee", None, [
            Product("truite fumee elevage", 5.5)
        ])

    ]),
    Product("thon", 2.15, [
        Product("thon boite", 3.2)
    ])
    ,
    Product("saumon", 3.47, [
        Product("saumon elevage", 5.2),
        Product("truite fumee", None, [
            Product("truite fumee elevage", 5.5)
        ])
    ]),
    Product("bar", None, [
        Product("bar elevage", None, [
            Product("bar elevage filet", 9.2)
        ])
    ]),
    Product("dorade", None, [
        Product("dorade elevage", None, [
            Product("dorade elevage filet", 9.2)
        ])
    ]),
    Product("poisson roche", 6.94, [
        Product("crustace", 5.3, [
            Product("moule", 5.3),
            Product("crabe", 5.7),
            Product("crevette", 5.7),
            Product("langouste", 5.68)
        ]),
        Product("huitre", 5.68)

    ]),
    Product("sole", 20.86),
    Product("turbot", 14.51),
    Product("poulpe", 7.13),
    Product("homard", 28.05),
    Product("maquereau", 1.8),
    Product("merlan", 2.66),
    Product("cabillaud", 9.56),
    Product("anchois", 9.56),
    Product("requin", 11.5),
    Product("sardine", 1.1)
])
