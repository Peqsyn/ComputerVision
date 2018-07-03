import mysql.connector
from mysql.connector import errorcode

class DatabaseAccess:
    ''' Provides tools for accessing databases

    Allows user to create database and then add, remove, and search
    items in database contents.

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
        self.cursor = self.cnx.cursor(buffered = True)

        

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


        # Note: Isbn is a 12 digit number and cannot be contained in the
        # standard variable types.
        tables['item'] = (
            '  CREATE TABLE `item` ('
            '  `name` varchar(64) NOT NULL,'
            '  `weight` int(255) NOT NULL,'
            '  `certainty` int(255) NOT NULL,'
            '  `price_paid` int(255) NOT NULL,'
            '  `location_of_purchase` varchar(64) NOT NULL,'
            '  `ISBN` int(255) NOT NULL,'
            '  `location` varchar(255) NOT NULL,'
            '  PRIMARY KEY (`name`)'
            ') ENGINE=InnoDB')

        return tables



    def initialize_tables(self, tables):
        ''' Create a collection of tables from a dictionary

        There is a standard form for creating a dictionary that will be
        converted to tables.

        tables = {}
        
        tables['name of entity'] = (
            '  CREATE TABLE `name of entity` ('
            '  `parameter1` datatype(bit depth etc.) NOT NULL,'
            '  `parameter2` datatype(bit depth etc.) NOT NULL,'
            '   .                                    '
            '   .                                    '
            '   .                                    '
            '  PRIMARY KEY (`parameter#`)'
            ') ENGINE=InnoDB')

        Args:
            tables (dict): dictionary defined as described in this
                heading.

        Returns:
            None

        '''
        
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



    def add_entry(self, table, *args):
        ''' Add data to the current database

        Add all necessary values to the requested table.

        Args:
            table (str): The name of the table in which the values are
                to be input.

            *args (n-values): Values to go into each column of the
                table.

        Returns:
            None

        '''

        # Move cursor to the requested table
        self.cursor.execute('SHOW columns FROM ' + table)

        # Get column names
        column_names = [column[0] for column in self.cursor.fetchall()]

        # Compose command to add data
        add_data = 'INSERT INTO ' + table + ' ('
        for column in column_names:
            add_data += column + ', '

        # Remove the extra ', '
        add_data = add_data[:-2]

        add_data += (') VALUES ('
                    + ('%s, '
                    * len(column_names)))

        # remove the extra ', '
        add_data = add_data[:-2]

        add_data += ')'

        # commit data to database
        self.cursor.execute(add_data, args)
        self.cnx.commit()



    ####################################################################
    #                                                                  #
    #                      Database Query Commands                     #
    #                                                                  #
    ####################################################################

    def number_less_than(self, table, column_name, number):
        ''' Find entries with a value less than the specified number

        The specified table's column will be searched for a value that
        is less than the one specified.  The matching entries will then
        be provided to the user as a list of dictionaries containing
        parameters which can be searched by name.

        Args:
            table (str): table to be searched
            column_name (str): name of the column to be searched
            number (int): number to be compared against

        Returns:
            List of dictionaries.  Each dictionary can be referenced by
            the name specified in the definition of the database.

        '''
        
        query = ('SELECT * FROM '
                 + table
                 + ' WHERE '
                 + column_name
                 + ' < %s') %(number)


        # Move cursor to the requested table
        self.cursor.execute('SHOW columns FROM ' + table)

        # Get column names
        column_names = [column[0] for column in self.cursor.fetchall()]

        
        self.cursor.execute(query)

        values = []
        for column in self.cursor.fetchall():
            values.append({})
            for i in range(len(column_names)):
                values[len(values)-1].update(
                    {column_names[i]:column[i]})

        return values
        

        
    def number_greater_than(self, table, column_name, number):
        ''' Find entries with a value less than the specified number

        The specified table's column will be searched for a value that
        is greater than the one specified.  The matching entries will
        then be provided to the user as a list of dictionaries
        containing parameters which can be searched by name.

        Args:
            table (str): table to be searched
            column_name (str): name of the column to be searched
            number (int): number to be compared against

        Returns:
            List of dictionaries.  Each dictionary can be referenced by
            the name specified in the definition of the database.

        '''
        
        query = ('SELECT * FROM '
                 + table
                 + ' WHERE '
                 + column_name
                 + ' > %s') %(number)


        # Move cursor to the requested table
        self.cursor.execute('SHOW columns FROM ' + table)

        # Get column names
        column_names = [column[0] for column in self.cursor.fetchall()]

        
        self.cursor.execute(query)

        values = []
        for column in self.cursor.fetchall():
            values.append({})
            for i in range(len(column_names)):
                values[len(values)-1].update(
                    {column_names[i]:column[i]})

        return values


    
    def number_between(self, table, column_name, number_1, number_2):
        ''' Find entries with a value less than the specified number

        The specified table's column will be searched for a value that
        is between the two specified.  The matching entries will then
        be provided to the user as a list of dictionaries containing
        parameters which can be searched by name.

        Args:
            table (str): table to be searched
            column_name (str): name of the column to be searched
            number_1 (int): number specifying first boundary
            number_2 (int): number specifying second boundary

        Returns:
            List of dictionaries.  Each dictionary can be referenced by
            the name specified in the definition of the database.

        '''

        query = ('SELECT * FROM '
                 + table
                 + ' WHERE '
                 + column_name
                 + ' BETWEEN %s AND %s') %(number_1, number_2)


        # Move cursor to the requested table
        self.cursor.execute('SHOW columns FROM ' + table)

        # Get column names
        column_names = [column[0] for column in self.cursor.fetchall()]

        
        self.cursor.execute(query)

        values = []
        for column in self.cursor.fetchall():
            values.append({})
            for i in range(len(column_names)):
                values[len(values)-1].update(
                    {column_names[i]:column[i]})

        return values


    
    def equal_to(self, table, column_name, value):
        ''' Find entries with a value less than the specified number

        The specified table's column will be searched for a value that
        is the same as the one specified.  The matching entries will 
        then be provided to the user as a list of dictionaries
        containing parameters which can be searched by name.

        Args:
            table (str): table to be searched
            column_name (str): name of the column to be searched
            value (*): value to be compared against

        Returns:
            List of dictionaries.  Each dictionary can be referenced by
            the name specified in the definition of the database.

        '''

        query = ('SELECT * FROM '
                 + table
                 + ' WHERE '
                 + column_name
                 + ' LIKE %s%s%s') %('\'', value, '\'')

        # Move cursor to the requested table
        self.cursor.execute('SHOW columns FROM ' + table)

        # Get column names
        column_names = [column[0] for column in self.cursor.fetchall()]

        
        self.cursor.execute(query)

        values = []
        for column in self.cursor.fetchall():
            values.append({})
            for i in range(len(column_names)):
                values[len(values)-1].update(
                    {column_names[i]:column[i]})

        return values



    ####################################################################

    

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

    #database.add_entry('item', 'bean3', 311, 100, 30
    #                    , 'starbucks', 200289, 'fridge')

    print([data['name'] for data in database.number_between(
        'item', 'weight', 200, 310)])

    database.close_connection()

    
    
