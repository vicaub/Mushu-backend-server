# 2018 Mushu App Environnementale
# Python backend

## Description 

Mushu App Environnementale project aim to compute an estimation of the carbon footprint of anyt food product.

The project contains into two parts:
- The front-end: a hybrid mobile app developed with react native that get barcodes from products with camera.
- The Python back-end (this project) that serve an API for the mobile app to compute the carbon footprint from a barcode.

Our back-end technology use openfoodfacts API to get the ingredient string and some other relevant information from a barcode.

The ingredient string is parsed into an Ingredient object (see Ingredient.py) and extract the tree structure from it.

Then we match every individual ingredient with a product we know the footprint in the database.

Finally, by extracting existing percentages in the string and estimating the ones left we compute the total carbon footprint.

Server deployed at IP address: 54.37.23.103/mushu/

### Database

The database is located in ./categories folder. It contains a file for each top product category:
- fruits
- legumes
- poissons
- produits_laitiers
- viandes

In each of these files you can find a tree structure of subproducts with their carbon footprint or not.

Products in database are created with the Matching class and declare the sub products (children)


## Prerequisites

Prerequisites in Dockerfile

## How to run

### Locally
```
make run
```

### On remote server

systemctl service
```
sudo vim /etc/systemd/system/mushu.service
```

Service status
```
systemctl status mushu.service
```

Service restart
```
sudo systemctl restart mushu.service
```

Service log
```
sudo journalctl -u mushu.service -f
```

## Run tests

Tests are located in ./tests folder
```
python3 -m unittest discover ./tests
```


