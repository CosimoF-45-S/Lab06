from dataclasses import dataclass

@dataclass
class GoDailySalesDTO:
    _retailerCode : int
    _productNumber : int
    _orderMethodCode : int
    _date : str
    _quantity : int
    _unitPrice : float
    _unitSalePrice : float


    @property
    def retailerCode(self):
        return self._retailerCode
    @retailerCode.setter
    def retailerCode(self, retailerCode):
        self._retailerCode = retailerCode

    @property
    def productNumber(self):
        return self._productNumber

    @productNumber.setter
    def productNumber(self, prodNumber):
        self._productNumber = prodNumber

    @property
    def orderMethodCode(self):
        return self._orderMethodCode
    @orderMethodCode.setter
    def orderMethodCode(self, orderMethodCode):
        self._orderMethodCode = orderMethodCode

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self,date):
        self._date = date

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def unitPrice(self):
        return self._unitPrice

    @unitPrice.setter
    def unitPrice(self, unitPrice):
        self._unitPrice = unitPrice

    @property
    def unitSalePrice(self):
        return self._unitSalePrice

    @unitSalePrice.setter
    def unitSalePrice(self, unitSalePrice):
        self._unitSalePrice = unitSalePrice

    def __eq__(self, other):
        return (self._retailerCode == other._retailerCode and self._productNumber == other._productNumber and
                self._orderMethodCode == other._orderMethodCode and self)

    def __hash__(self):
        return hash((self._retailerCode, self._productNumber, self._orderMethodCode))