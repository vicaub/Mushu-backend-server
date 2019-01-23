from categories import fruits, legumes, poissons, produits_laitiers, viandes
from models.Product import Product

products = [
    fruits.fruits,
    legumes.legumes,
    poissons.poissons,
    produits_laitiers.produits_laitiers,
    viandes.viandes
]

database = Product("database", None, products)
