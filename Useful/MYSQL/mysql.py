import sys
#import _mysql

import MySQLdb
import json

class Database():
    
    # Initialization
    def __init__(self, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
        
        try:
            conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD)
        except:
            raise TypeError("Host, Username, or Password for mysql is incorrect")
        
        try:
            conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        except:
            conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD)
            conn.cursor().execute("CREATE DATABASE " + self.DB_NAME)
        conn.close()

    def reset(self):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)

        for T in self.get_all_tables():
            conn.cursor().execute("DROP TABLE " + T);
        
        conn.close()
        print("INFO:            Database empty")


    def custom_query(self, QUERY):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        conn.cursor().execute(QUERY)
        
        conn.close()
        print("INFO:            Query executed")
    
    # Populating
    def add_table(self, table_NAME):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        conn.cursor().execute("CREATE TABLE IF NOT EXISTS " + table_NAME + " (ID INT PRIMARY KEY AUTO_INCREMENT)");
        
        conn.close()
        print("INFO:            Table " + table_NAME + " created")

    def add_column(self, table_NAME, column_NAME, column_TYPE='string', isNullable=True):
        
        if column_TYPE == "array":
            # TODO figure out how to implement this
            return None
        if column_TYPE == "object" or column_TYPE == "json":
            # TODO figure out how to implement this
            return None
        
        mysql_column_TYPE = ""
        if column_TYPE == "boolean" or column_TYPE == "bool":
             mysql_column_TYPE = "BOOLEAN"
        elif column_TYPE == "string":
            mysql_column_TYPE = "VARCHAR(255)"
        elif column_TYPE == "int":
            mysql_column_TYPE = "INT"
        elif column_TYPE == "float":
            mysql_column_TYPE = "FLOAT"
        elif column_TYPE == "double":
            mysql_column_TYPE = "DOUBLE"
        else:
            raise TypeError("Could not parse column type.")
        
        if not isNullable:
            mysql_column_TYPE += " NOT NULL"

        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        conn.cursor().execute("ALTER TABLE " + table_NAME + " ADD COLUMN " + column_NAME + " " + mysql_column_TYPE);
        
        conn.close()
        print("INFO:            Column " + column_NAME + " created")
    
    def add_data(self, table_NAME, A):
        # A is an array of values in the order of the columns
        # In order to use this methof you have to manually create the columns before hand

        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)

        # If you don't have the 'with conn:' line then the data doesn't get added to the database
        with conn:
            cur = conn.cursor()
            cur.execute("SHOW columns FROM " + table_NAME)
            results = cur.fetchall()
            COLS = [column[0] for column in results if column[0] != "ID"]
            TYPES = [column[1] for column in results if column[0] != "ID"]

            query = "INSERT INTO " + table_NAME + "("
            for i in range(len(COLS)):
                query += COLS[i]
                if i != len(COLS)-1:
                    query += ","
                else:
                    query += ")"

            query += " VALUES("
            for i in range(len(COLS)):
                if type(A[i]) == str:
                    query += "'" + A[i] + "'"
                elif type(A[i]) == bool:
                    if A[i]:
                        query += "1"
                    else:
                        query += "0"
                else:
                    query += str(A[i])
                if i != len(A)-1:
                    query += ","
                else:
                    query += ")"
            cur.execute(query)
        
        conn.close()
        print("INFO:            Data added")
    
    def add_data_json(self, table_NAME, J):
        # J is a json object
        # This method will automatically create the colums in the database that match the json object
        fields = [str(f) for f in J]

        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)

        # If you don't have the 'with conn:' line then the data doesn't get added to the database
        with conn:
            cur = conn.cursor()

            cur.execute("SHOW columns FROM " + table_NAME)
            results = cur.fetchall()
            COLS = [column[0] for column in results if column[0] != "ID"]
            
            # creating columns
            for f in fields:
                if f not in COLS:
                    mysql_column_TYPE = ""
                    if type(J[f]) == bool:
                        mysql_column_TYPE = "BOOLEAN"
                    elif type(J[f]) == str:
                        mysql_column_TYPE = "VARCHAR(255)"
                    elif type(J[f]) == int:
                        mysql_column_TYPE = "INT"
                    elif type(J[f]) == float:
                        mysql_column_TYPE = "DOUBLE"
                    conn.cursor().execute("ALTER TABLE " + table_NAME + " ADD COLUMN " + f + " " + mysql_column_TYPE);

            query = "INSERT INTO " + table_NAME + "("
            for i in range(len(fields)):
                query += fields[i]
                if i != len(fields)-1:
                    query += ","
                else:
                    query += ")"

            query += " VALUES("
            for i in range(len(fields)):
                if type(J[fields[i]]) == str:
                    query += "'" + J[fields[i]] + "'"
                elif type(J[fields[i]]) == bool:
                    if J[fields[i]]:
                        query += "1"
                    else:
                        query += "0"
                else:
                    query += str(J[fields[i]])
                if i != len(fields)-1:
                    query += ","
                else:
                    query += ")"
            cur.execute(query)

        conn.close()
        print("INFO:            Data added")

    # Diplaying
    def to_json(self, column_NAMES, result):
        out = "{"
        for i in range(len(column_NAMES)):
            out += "'" + column_NAMES[i] + "':"
            
            if type(result[i]) == str:
                out += "'" + str(result[i]) + "'"
            else:
                out += str(result[i])
            
            if i != len(column_NAMES)-1:
                out += ","
        out += "}"
        return out

    def print_data(self, table_NAME, column_NAMES, results):
        print()
        print(table_NAME + ":")
        for r in results:
            print(self.to_json(column_NAMES, r))
        return results

    # Getting
    def get_all_tables(self):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        cur = conn.cursor()
        cur.execute("SHOW tables FROM " + self.DB_NAME)
        results = cur.fetchall()
        
        conn.close()
        return [table[0] for table in results]

    def get_all_columns(self, table_NAME):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        cur = conn.cursor()
        cur.execute("SHOW columns FROM " + table_NAME)
        results = cur.fetchall()
        
        conn.close()
        return [column[0] for column in results]
    
    def get_all_data(self, table_NAME):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + table_NAME)
        results = cur.fetchall()
        
        column_NAMES = self.get_all_columns(table_NAME) 
        self.print_data(table_NAME, column_NAMES, results)

        conn.close()
        return results

    def get_specific_columns(self, table_NAME, L):
        # L is a list of columns you want returned
        column_NAMES = self.get_all_columns(table_NAME)
        for c in L:
            if c not in column_NAMES:
                raise TypeError("column '" + c + "' does not exist in the table '" + table_NAME + "'") 
        
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        cur = conn.cursor()
        query = "SELECT "
        for i in range(len(L)):
            query += L[i]
            if i != len(L)-1:
                query += ","
        query += " FROM " + table_NAME
        cur.execute(query)
        results = cur.fetchall()
        
        self.print_data(table_NAME, L, results)
        
        conn.close()
        return results    
    
    
    # Filtering
    def filter_data(self, table_NAME, F):
        # F is just a string with a search query as one would write it in mysql
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + table_NAME + " WHERE " + F)
        results = cur.fetchall()

        column_NAMES = self.get_all_columns(table_NAME)
        self.print_data(table_NAME, column_NAMES, results)

        conn.close()
        return results
    
    # Deleting
    def delete_database(self):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        conn.cursor().execute("DROP DATABASE " + DB_NAME);
        
        conn.close()
        print("INFO:            Database " + self.DB_NAME + " deleted")

    def delete_table(self, table_NAME):
        conn = MySQLdb.connect(self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME)
        
        if table_Name not in self.get_all_tables():
            raise TypeError("Table '" + table_NAME + "' does not exist in the database")

        conn.cursor().execute("DROP TABLE " + table_NAME);
        
        conn.close()
        print("INFO:            Table " + table_NAME + " deleted")

    def load_json(self, table_NAME, json_file):
        f = open(json_file,'r')
        J_array = json.load(f)
        f.close()
        for J in J_array:
            self.add_data_json(table_NAME, J)
        
