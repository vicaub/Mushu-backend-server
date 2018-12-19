import numbers


class Product:
    def __init__(self, name, cfp=None, children=None):
        if not isinstance(name, str):
            raise TypeError("The name should be a string")
        if cfp and not isinstance(cfp, numbers.Real):
            raise TypeError("The carbon footprint should be a float or None")
        if children and not isinstance(children, list):
            raise TypeError("The children should be a list of Products or None")

        self.name = name
        self.cfp = cfp
        self.children = children

    def get_leaves(self):
        if self.children and len(self.children) > 0:
            leaves = []
            for child in self.children:
                leaves += child.get_leaves()
            return leaves
        else:
            return [self]

        # return list(map(lambda child: child.get_name(), self.children))
