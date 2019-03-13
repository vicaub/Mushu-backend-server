class APICallError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Erreur de réseau"


class ProductNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Nous n'avons pas trouvé les informations de ce produit :/"


class APIResponseError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Les informations de la base de donnée ne sont pas utilisables"
