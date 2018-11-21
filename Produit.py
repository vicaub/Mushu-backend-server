class Produit:
    def __init__(self, nom, ec, children=None):
        self.nom = nom
        self.ec = ec
        self.children = children