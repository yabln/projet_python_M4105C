#!/usr/bin/python3

import sqlite3

class DatabaseAdmin :
    """
        This class has the goal to create, access, modify or destroy the sqlite3 database used to store the project datas
    """

    def __init__(self):
        """
            Empty constructor
        """

    def create_tables(self, db_name):
        """
            Create a connection to the .db file referenced by db_name,
            wipe existing tables and create the ones that are going to be used by the project
        """

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS Installation;")
        c.execute("DROP TABLE IF EXISTS Equipement;")
        c.execute("DROP TABLE IF EXISTS Activity;")
        c.execute("DROP TABLE IF EXISTS EquipementActivity;")

        c.execute("CREATE TABLE Installation (Id INTEGER PRIMARY KEY, Name TEXT, Address TEXT, \
        PostalCode INTEGER, City TEXT, Latitude REAL, Longitude Real);")
        c.execute("CREATE TABLE Equipement (Id INTEGER PRIMARY KEY, Name TEXT);")
        c.execute("CREATE TABLE Activity (Id INTEGER PRIMARY KEY, Name TEXT);")
        c.execute("CREATE TABLE EquipementActivity (IdEquipement INTEGER, IdActivity INTEGER, PRIMARY KEY (IdEquipement, IdActivity));")

        conn.commit()
        conn.close()


admin = DatabaseAdmin()
admin.create_tables("datas.db")
