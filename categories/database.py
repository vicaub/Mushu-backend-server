from categories import fruits, legumes, poissons, produits_laitiers, viandes, epicerie, boissons
from models.Product import Product

categories = [
    fruits.fruits,
    legumes.legumes,
    poissons.poissons,
    produits_laitiers.produits_laitiers,
    viandes.viandes,
    epicerie.epicerie,
    boissons.boissons
]

for category in categories:
    category.set_children_category(category)

database = Product("database", None, categories)
