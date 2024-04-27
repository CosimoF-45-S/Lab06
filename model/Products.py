from dataclasses import dataclass

@dataclass
class GoProductsDTO:
    _product_number : int
    _product_name : str
    _product_type : str
    _product : str
    _product_brand : str
    _product_color : str
    _unit_cost : float
    _unit_price : float

    @property
    def product_number(self):
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        self._product_number = product_number

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self,product_name):
        self._product_name = product_name

    @property
    def product_type(self):
        return self

    @product_type.setter
    def product_type(self,product_type):
        self._product_type = product_type

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def product_brand(self):
        return self._product_brand

    @product_brand.setter
    def product_brand(self,product_brand):
        self._product_brand = product_brand

    @property
    def product_color(self):
        return self._product_color

    @product_color.setter
    def product_color(self,product_color):
        self._product_color = product_color

    @property
    def unit_cost(self):
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self,unit_cost):
        self._unit_cost = unit_cost

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self,unit_price):
        self._unit_price = unit_price

    def __eq__(self, other):
        return self.product_number == other.product_number

    def __hash__(self):
        return hash(self.product_number)


