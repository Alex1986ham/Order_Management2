import mysql.connector
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='192.168.178.22',
                                        database='information_schema',
                                        user='aldudko2',
                                        password='Dudko010914')


except Error as e:
    print("Error while connection to mysql", e)
