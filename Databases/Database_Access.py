import mysql.connector
from mysql.connector import errorcode

class DatabaseAccess:
    ''' Provides tools for accessing databases

    Will create database and then allow adding, removing, and searching
    of database contents.

    '''

    def __init__(self, username = 'root',
                       password = 'gomitech',
                       host = 'localhost'):
        ''' Initialize all necessary parameters

        Create the objects that will be used for accessing and
        manipulating values in the database.

        Args:
            username (str): Name used to access database.
            password (str): Password used to access database.
            host (str): Name of the server host.

        Returns:
            None
            
        '''
        
        self.cnx = mysql.connector.connect( host = host,
                                            user = username,
                                            password = password )
        self.cursor = self.cnx.cursor()

        

    def create_database(self, database_name):
        '''Create a new database

        Try constructing a database with the given name.  If the
        database already exists let the user know and return false.

        Args:
            database_name (str): The name of the database to be created.

        Returns:
            True if created, False if failed
            
        '''

        try:
            self.cursor.execute(
                'CREATE DATABASE {} DEFAULT CHARACTER SET wro"utf8"'
                .format(database_name))

            return True # if successful

        except mysql.connector.Error as err:
            print('Failed creating database: {}'.format(err))

            return False # if successful

        

    def connect_to_database(self, database_name):
        ''' Connect to a database

        Try connecting to the specified database.  If something goes
        wrong, refer to the output error codes.

        Args:
            database_name (str): Name of the database to be accessed

        Returns:
            1 if the connection succeeded,
            -1 if the database does not exist,
            0 if an error occured (the error is also printed for debugging)
       
        '''

        try:
            self.cnx.database = database_name
            return 1

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                return -1
            else:
                print(err)
                return 0



    def gomi_tables(self):
        ''' Creates tables for use with the gomi shift

        Configures the database with the necessary entities for managing
        fridge inventory.

        This function should probably be moved to a different class
        later on. It's very specific to the database design required for
        the gomi shift.

        Returns:
            tables (str): A dictionary of database entities and their
                          corresponding tables.

        '''
        tables = {}
        
        tables['fridge_owner'] = (
            'CREATE TABLE `fridge_owner` ('
            '  `username` varchar(32) NOT NULL,'
            '  `password` varchar(16) NOT NULL,'
            '  `date_of_birth` date NOT NULL,'
            '  PRIMARY KEY (`username`)'
            ') ENGINE=InnoDB')

        tables['add'] = (
            'CREATE TABLE `add` ('
            '  `item` varchar(32) NOT NULL,'
            '  `date` date NOT NULL,'
            '  PRIMARY KEY (`item`)'
            ') ENGINE=InnoDB')

        tables['remove'] = (
            'CREATE TABLE `remove` ('
            '  `item` varchar(32) NOT NULL,'
            '  `date` date NOT NULL,'
            '  PRIMARY KEY (`item`)'
            ') ENGINE=InnoDB')

        tables['fridge_name'] = (
            'CREATE TABLE `fridge_name` ('
            '  `name` varchar(32) NOT NULL,'
            '  `size` int(255) NOT NULL,'
            '  `location` varchar(255) NOT NULL,'
            '  `capacity` int(255) NOT NULL,'
            '  `base_weight` int(255) NOT NULL,'
            '  PRIMARY KEY (`name`)'
            ') ENGINE=InnoDB')

        tables['item'] = (
            '  CREATE TABLE `item` ('
            '  `name` varchar(64) NOT NULL,'
            '  `weight` int(255) NOT NULL,'
            '  `certainty` int(255) NOT NULL,'
            '  `price_paid` int(255) NOT NULL,'
            '  `location_of_purchase` varchar(64) NOT NULL,'
            '  `ISBN` int(16) NOT NULL,'
            '  `location` varchar(255) NOT NULL,'
            '  PRIMARY KEY (`name`)'
            ') ENGINE=InnoDB')

        return tables



    def initialize_tables(self, tables):
        
        for name, ddl in tables.items():
            try:
                print('Creating table {}: '.format(name), end='')
                self.cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('already exists.')
                else:
                    print(err.msg)
            else:
                print('OK')
    

    def close_connection(self):
        ''' Close connection with MySQL server

        When a connection has been opened this function can be called
        to close connection with the MySQL server

        Args:
            None

        Returns:
            True when connection has been closed

        '''

        self.cursor.close()
        self.cnx.close()
        return True
        

if __name__ == '__main__':

    # Open connection with server.
    #
    # If using a database on your local machine, use the following
    #   instructions.
    #   - host='localhost',
    #   - user='root',
    #   - password='gomitech'
    #   - database='***name of database***'
    database = DatabaseAccess()

    connected = database.connect_to_database('gomi_shift_test_1')
    if(connected == 1):
        print('connection successful')
    elif(connected == -1):
        database.create_database('gomi_shift_test_1')
        print('database created')
    else:
        print('failed to connect')

    database.initialize_tables(
        database.gomi_tables())

    database.close_connection()

    
    
