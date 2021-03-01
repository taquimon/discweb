import mysql.connector
from mysql.connector import errorcode
from mysql.connector.cursor import MySQLCursor


class MysqlConnection(object):
    """[summary]

    Args:
        object ([type]): [description]
    """
    def __init__(self, **kwargs):
        """AI is creating summary for __init__
        """
        self.connection_options = {}
        self.connection_options['user'] = 'root'
        self.connection_options['password'] = 'phantom'
        self.connection_options['host'] = 'localhost'
        self.connection_options['port'] = '3306'
        self.connection_options['database'] = "eami4ehag5yx1sji"
        self.connection_options['raise_on_warnings'] = True
        self.connection()

    def connection(self):
        """AI is creating summary for connection
        """
        
        try:
            self.connect = mysql.connector.connect(**self.connection_options)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists") 
            else:
                print(err)
    
    def query(self, statement, data=''):
        """AI is creating summary for query

        Args:
            statement ([type]): [description]
            data (str, optional): [description]. Defaults to ''.

        Returns:
            [type]: [description]
        """
        if self.connect:
            cursor = self.connect.cursor(buffered=True)
            print(statement)
            cursor.execute(statement)
            print(cursor.rowcount)
            result = cursor.fetchall()
            cursor.close
        
        return result

    def get_version(self):
        """AI is creating summary for get_version
        """
                
        print(self.query("select version()"))
