from server.models.Product import Product

legumes = Product('Légume', None, [
    Product('tomate', None, [
        Product('sauce tomate', 2.9),
        Product('tomate fraiche hors saison', 2.2),
        Product("tomate fraîche saison", 0.3),
        Product("tomate destinée l'industrie", 0.5),
        Product('tomate pelées', 1.4),
        Product('pulpe tomate', 1.4),
        Product('tomate fraiche importée', 0.6)
    ]),
    Product('chou', None, [
        Product('chou-fleur', 0.5),
        Product('chou pommé', 0.5)
    ]),
    Product('pois', None, [
        Product("pois d'hiver frais", 1.4),
        Product('pois surgelés', 0.8),
        Product('pois conserve', 0.7),
        Product('pois printemps frais', 0.5),
        Product('pois chiche', 0.77)
    ]),
    Product('aubergine', 0.9, [
        Product('aubergine serre chauffée', 5)
    ]),
    Product('asperge', None, [
        Product('asperge saison', 0.7),
        Product('asperge boite', 2)
    ]),
    Product('haricot', None, [
        Product('haricot vert frais', 0.7),
        Product('haricot blanc en conserve', 1.6),
        Product('haricot vert importé', 22.1)
    ]),
    Product('carotte', 0.3),
    Product('bettrave', 0.2),
    Product('epinard', 0.3),
    Product('poireau', 0.3),
    Product('brocoli', 0.4),
    Product('artichaut', 0.5),
    Product('radis', 0.5),
    Product('oignon', 0.5),
    Product('concombre', 1.4),
    Product('champignon', 1.5),
    Product('avocat', 1.2),
    Product('olive', 0.9),
    Product('citrouille', 0.7),
    Product('courges', 0.7),
    Product('potiron', 0.7),
    Product('lentilles', 0.9),
    Product('endive', 0.7),
    Product('poivron', 0.9),
    Product('navet', 0.7),
    Product('celeri', 0.8),
    Product('mais', 0.7),
    Product('pomme de terre', 0.6),
    Product('salade', 0.5),
    Product('soja', 0.45),
    Product('fenouil', 0.48),
    Product('courgette', 0.6)
])
