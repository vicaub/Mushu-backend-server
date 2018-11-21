class Product:
    def __init__(self, name, cfp, children=None):
        if not isinstance(name, str):
            raise TypeError("The name should be a string")
        if cfp and not isinstance(cfp, float):
            raise TypeError("The carbon footprint should be a float or None")
        if children and not isinstance(children, list):
            raise TypeError("The children should be a list of Products or None")

        self.name = name
        self.cfp = cfp
        self.children = children
