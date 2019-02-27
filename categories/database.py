from categories import fruits, legumes, poissons, produits_laitiers, viandes, epicerie, boissons
from models.Product import Product

products = [
    fruits.fruits,
    legumes.legumes,
    poissons.poissons,
    produits_laitiers.produits_laitiers,
    viandes.viandes,
    epicerie.epicerie,
    boissons.boissons,
]

database = Product("database", None, products)
