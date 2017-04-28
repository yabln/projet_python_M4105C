#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from CsvReader import *

class DatabaseAdmin :
    """
        This class has the goal to create, access, modify or destroy the sqlite3 database used to store the project datas
    """

    def __init__(self, db_name):
        """
            Constructor
        """
        self.db_name = db_name

    def create_tables(self):
        """
            Create a connection to the .db file referenced by db_name,
            wipe existing tables and create the ones that are going to be used by the project
        """

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS Installation;")
        c.execute("DROP TABLE IF EXISTS Equipement;")
        c.execute("DROP TABLE IF EXISTS Activity;")
        c.execute("DROP TABLE IF EXISTS EquipementActivity;")

        c.execute("CREATE TABLE Installation (Id INTEGER PRIMARY KEY, Name TEXT, Address TEXT, \
        PostalCode INTEGER, City TEXT, Latitude REAL, Longitude Real);")

        c.execute("CREATE TABLE Equipement (Id INTEGER PRIMARY KEY, Name TEXT, \
        IdInstallation INTEGER, FOREIGN KEY(IdInstallation) REFERENCES Installation(Id));")

        c.execute("CREATE TABLE Activity (Id INTEGER PRIMARY KEY, Name TEXT);")

        c.execute("CREATE TABLE EquipementActivity (IdEquipement INTEGER, IdActivity INTEGER, PRIMARY KEY (IdEquipement, IdActivity));")

        conn.commit()
        conn.close()

    def insert_from_csv_reader(self, reader):
        """
            Takes a CsvReader and adds the contained objects into the database
        """

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for installation_key in reader.installations.keys():
            insert_query = "INSERT INTO Installation(Id, Name, Address, PostalCode, City, Latitude, Longitude) VALUES(?, ?, ?, ?, ?, ?, ?)"
            instal = reader.installations[installation_key]
            c.execute(insert_query, (instal.id, instal.name, instal.address, instal.postal_code, instal.city, instal.latitude, instal.longitude))

        for activity_key in reader.activities.keys():
            insert_query = "INSERT INTO Activity(Id, Name) VALUES(?, ?)"
            act = reader.activities[activity_key]
            print("Id : " + act.id + " Name : " + act.name)
            c.execute(insert_query, (act.id, act.name))

        conn.commit()

        for equipement_key in reader.equipements.keys():
            insert_query = "INSERT INTO Equipement(Id, Name, IdInstallation) VALUES(?, ?, ?)"
            equip = reader.equipements[equipement_key]
            c.execute(insert_query, (equip.id, equip.name, equip.installation.id))

            for act in equip.activities:
                #print("equipId : " + equip.id + " actId : " + act.id)
                insert_query = "INSERT INTO EquipementActivity(IdEquipement, IdActivity) VALUES(?, ?)"
                c.execute(insert_query, (equip.id, act.id))

        conn.commit()
        conn.close()
