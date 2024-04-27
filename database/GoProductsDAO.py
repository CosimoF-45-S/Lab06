from database.DB_connect import DBConnect
from model import Products


class GoProductsDAO:
    def __init__(self):
        pass

    def products(self):

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """SELECT * FROM go_products"""
        cursor.execute(query)
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append(Products.GoProductsDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        cursor.close()
        cnx.close()
        return products



