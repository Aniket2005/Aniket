import pymysql as pm
class dbconnection:
    @staticmethod
    def createconnection():
        con=pm.connect("localhost","root","aniket","collegerating")
        return con
