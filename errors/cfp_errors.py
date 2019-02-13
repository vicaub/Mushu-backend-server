class APICallError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Error while calling API"


class ProductNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "No product found. Please check your barcode"


class APIResponseError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Response from API is not readable"
