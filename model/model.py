from database import GoDailySalesDAO
from database import GoProductsDAO
from database import GoRetailersDAO

class Model:
    def __init__(self):
        pass

    def fill_dd_anno(self):
        dailySDAO = GoDailySalesDAO.GoDailySalesDAO()
        return dailySDAO.years()

    def fill_dd_brand(self):
        productsDAO = GoProductsDAO.GoProductsDAO()
        brands = set()
        for product in productsDAO.products():
            brands.add(product.product_brand)
        return sorted(brands)

    def fill_dd_retailer(self):
        retailersDAO =  GoRetailersDAO.GoRetailersDAO()
        return retailersDAO.retailers()

    def handle_top_vendite(self, anno, brand, retailer):
        dailySalesDAO = GoDailySalesDAO.GoDailySalesDAO()
        return dailySalesDAO.handle_top_vendite(anno, brand, retailer)

    def handle_analizza_vendite(self, anno, brand, retailer):
        dailySalesDAO = GoDailySalesDAO.GoDailySalesDAO()
        sales = dailySalesDAO.handle_analizza_vendite(anno, brand, retailer)
        statistiche = []

        #STATISTICHE
        giro = 0
        numero_vendite = 0
        retailers = []
        prodotti = []
        for sale in sales:
            giro += sale[0]
            numero_vendite += 1
            if sale[1] not in retailers:
                retailers.append(sale[1])
            if sale[2] not in prodotti:
                prodotti.append(sale[2])

        statistiche.append(giro)
        statistiche.append(numero_vendite)
        statistiche.append(len(retailers))
        statistiche.append(len(prodotti))

        return statistiche

