from dataclasses import dataclass

@dataclass
class GoRetailerDTO:
    _retailer_code : int
    _retailer_name : str
    _type : str
    _country : str

    @property
    def retailer_code(self):
        return self._retailer_code

    @retailer_code.setter
    def retailer_code(self, retailer_code):
        self._retailer_code = retailer_code

    @property
    def retailer_name(self):
        return self._retailer_name

    @retailer_name.setter
    def retailer_name(self, retailer_name):
        self._retailer_name = retailer_name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)