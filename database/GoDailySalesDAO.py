from database.DB_connect import DBConnect


class GoDailySalesDAO:
    def __init__(self):
        pass

    def years(self):

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(Date) FROM go_daily_sales ORDER BY `Date`"""
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        cursor.close()
        cnx.close()

        return result

    def handle_top_vendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """SELECT * FROM go_daily_sales gds , go_products gp WHERE gds.Product_number = gp.Product_number and 
                   YEAR(Date) = COALESCE(%s, YEAR(Date)) AND  gp.Product_brand = COALESCE(%s, gp.Product_brand) AND 
                   gds.Retailer_code  = COALESCE(%s, gds.Retailer_code) ORDER BY gds.Quantity * gds.Unit_sale_price 
                   DESC LIMIT 5 """

        cursor.execute(query, (anno, brand, retailer))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append([row[3].strftime("%Y-%m-%d"), float(row[4]*row[6]), row[0], row[1]])
        cursor.close()
        cnx.close()
        return result

    def handle_analizza_vendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        query = """SELECT * FROM go_daily_sales gds , go_products gp WHERE gds.Product_number = gp.Product_number and 
                   YEAR(Date) = COALESCE(%s, YEAR(Date)) AND  gp.Product_brand = COALESCE(%s, gp.Product_brand) AND 
                   gds.Retailer_code  = COALESCE(%s, gds.Retailer_code)"""

        cursor.execute(query, (anno, brand, retailer))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append([float(row[4] * row[6]), row[0], row[1]])
        cursor.close()
        cnx.close()
        return result



