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
        self.__cfp = cfp
        self.children = children
        self.parent = None
        self.category = None
        if self.children:
            for child in self.children:
                child.parent = self

    def set_children_category(self, category):
        self.category = category
        if self.children:
            for child in self.children:
                child.set_children_category(category)

    def get_leaves(self):
        if self.children and len(self.children) > 0:
            leaves = []
            for child in self.children:
                leaves += child.get_leaves()
            return leaves
        else:
            return [self]

        # return list(map(lambda child: child.get_name(), self.children))

    def convert_to_dict(self):
        """s
        """
        dict_product = {}
        if self.children:
            for child in self.children:
                dict_product[child] = child.name

        return dict_product

    def retrieve_missing_cfp(self):
        """
        when cfp is None get average children cfp or parent cfp
        """
        cfp = 0
        if self.children:
            # first get children cfp
            i = 0
            for child in self.children:
                if child.__cfp:
                    cfp += child.__cfp
                    i += 1
            if i > 0:
                cfp /= i
            return cfp
        if not cfp:
            # still no cfp get parent cfp
            if self.parent.__cfp:
                return self.parent.__cfp
            else:
                return self.parent.retrieve_missing_cfp()

    @property
    def cfp(self):
        """
        getter for cfp attributen
        """
        cfp = self.__cfp
        if not cfp:
            cfp = self.retrieve_missing_cfp()
            self.__cfp = cfp
        return cfp

    def __repr__(self):
        """
        Convienient format to print Product objects
        """
        product_print = self.name + ", cfp: " + str(self.cfp)
        # if self.children:
        #     product_print += ", " + str(self.children)
        return product_print

    def to_json(self):
        json = dict()
        json["product"] = self.name
        json["cfp"] = self.cfp
        json["category"] = self.category.name
        return json
