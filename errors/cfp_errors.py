class APICallError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Error while calling API"


class ProductNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Nous n'avons pas trouvé les informations de ce produit :/"


class APIResponseError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Response from API is not readable"
