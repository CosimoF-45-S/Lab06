from database.DB_connect import DBConnect
from model import Retailers


class GoRetailersDAO:
    def __init__(self):
        pass

    def retailers(self):

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """SELECT * FROM go_retailers;"""
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(Retailers.GoRetailerDTO(row[0], row[1], row[2], row[3]))
        cursor.close()
        cnx.close()
        return result



