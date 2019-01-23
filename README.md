# 2018 Mushu App Environnementale
# Python backend

<<<<<<< HEAD
## Description 

Mushu App Environnementale project aim to compute an estimation of the carbon footprint of anyt food product.

The project contains into two parts:
- The front-end: a hybrid mobile app developed with react native that get barcodes from products with camera.
- The Python back-end (this project) that serve an API for the mobile app to compute the carbon footprint from a barcode.

Our back-end technology use openfoodfacts API to get the ingredient string and some other relevant information from a barcode.

The ingredient string is parsed into an Ingredient object (see Ingredient.py) and extract the tree structure from it.

Then we match every individual ingredient with a product we know the footprint in the database.

Finally, by extracting existing percentages in the string and estimating the ones left we compute the total carbon footprint.

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

You need Python 3 environment and libraries in requirements.txt


You need python 3.6 installed and libraries located in requirements.txt file

```
sudo apt install python3
```

```
sudo apt install python3-pip
```

```
pip3 install -r requirements.txt
```

## How to run

```
python3 server.py
```

## Run tests

Tests are located in ./tests folder
```
python3 -m unittest discover ./tests
```
