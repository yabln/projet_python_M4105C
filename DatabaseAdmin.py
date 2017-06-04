#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import re
from CsvReader import *
from pprint import pprint

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
        for installation_key in reader.installations:
            insert_query = "INSERT INTO Installation(Id, Name, Address, PostalCode, City, Latitude, Longitude) VALUES(?, ?, ?, ?, ?, ?, ?)"
            instal = reader.installations[installation_key]
            c.execute(insert_query, (instal.id, instal.name, instal.address, instal.postal_code, instal.city, instal.latitude, instal.longitude))

        for activity_key in reader.activities:
            insert_query = "INSERT INTO Activity(Id, Name) VALUES(?, ?)"
            act = reader.activities[activity_key]
            c.execute(insert_query, (act.id, act.name))

        for equipement_key in reader.equipements:
            insert_query = "INSERT INTO Equipement(Id, Name, IdInstallation) VALUES(?, ?, ?)"
            equip = reader.equipements[equipement_key]
            c.execute(insert_query, (equip.id, equip.name, equip.installation.id))

            for act in equip.activities:
                insert_query = "INSERT INTO EquipementActivity(IdEquipement, IdActivity) VALUES(?, ?)"
                c.execute(insert_query, (equip.id, act.id))

        conn.commit()
        conn.close()

    def regexp(expr, item):
        reg = re.compile(expr)
        return reg.search(item) is not None


    def get_search_result(self, user_input):
        """
            Takes a user input, verify that it's conform, and then make a SQL request to fetch elements whose names correspond to that input
        """

        conn = sqlite3.connect(self.db_name)

        request_field = '%' + user_input[0].strip() + '%'
        request_city = '%' + user_input[1].strip() + '%'

        activity_ids = []
        activities_dictionary = {}
        activities_array = self.search_activity(conn, request_field)
        for datas in activities_array:
            activity_ids.append(datas[0])
            activities_dictionary[datas[0]] = datas[1]


        equipement_activity_ids = {}
        equipement_ids = []
        for datas in self.get_equipements_by_activity(conn, activity_ids):
            equipement_ids.append(datas[0])
            if datas[0] in equipement_activity_ids:
                equipement_activity_ids.get(datas[0]).append(datas[1])
            else:
                equipement_activity_ids[datas[0]] = [datas[1]]

        equipements_array = self.get_equipements_by_ids(conn, equipement_ids)

        installation_ids = []
        for datas in equipements_array:
            if not(datas[2] in installation_ids):
                installation_ids.append(datas[2])

        installations_list = []
        for datas_installation in self.search_installation(conn, request_city, installation_ids):
            current_intallation = Installation(datas_installation[0], datas_installation[1], datas_installation[2], datas_installation[3], datas_installation[4], datas_installation[5], datas_installation[6])
            for datas_equipement in equipements_array:
                if datas_equipement[2] == current_intallation.id:
                    current_equipement = Equipement(datas_equipement[0], datas_equipement[1], datas_equipement[2])
                    for key in equipement_activity_ids.keys():
                        if key == current_equipement.id:
                            for value in equipement_activity_ids.get(key):
                                current_equipement.add_activity(Activity(value, activities_dictionary.get(value)))

                    current_intallation.add_equipement(current_equipement)
                    equipements_array.remove(datas_equipement)

            installations_list.append(current_intallation)

        conn.close()

        return installations_list


    def search_installation(self, conn, city, ids):
        """
            Search the Installation table and get the lines that matches the city name in the request
        """

        c = conn.cursor()
        params = [city] + ids
        search_query = "SELECT * FROM Installation T1 WHERE T1.City LIKE ? AND T1.Id IN ({})".format(",".join(["?"] * len(ids)))

        #sqlite3.sqlite3_bind_text(search_query, 0, city)
        #for i in range(len(ids)):
        #    sqlite3.sqlite3_bind_text(search_query, i+1, ids[i])
        c.execute(search_query, params)
        result = c.fetchall()
        return result


    def search_activity(self, conn, request):
        """
            Search the Activity table to get lines that matches the request
        """

        c = conn.cursor()
        search_query = "SELECT * FROM Activity T1 WHERE T1.Name LIKE ?"
        c.execute(search_query, (request,))
        result = c.fetchall()
        return result


    def get_equipements_by_activity(self, conn, request):
        """
            For a set of activities' id passed in argument, returns a set of the equpements' id linked to the former
        """

        c = conn.cursor()
        search_query = "SELECT * FROM EquipementActivity T1 WHERE T1.IdActivity IN ({})".format(",".join(["?"] * len(request)))
        c.execute(search_query, tuple(request))
        result = c.fetchall()
        return result


    def get_equipements_by_ids(self, conn, request):
        """
            Fetch all equipements in the table via their Ids
        """

        c = conn.cursor()
        search_query = "SELECT * FROM Equipement T1 WHERE T1.Id IN ({})".format(",".join(["?"] * len(request)))
        c.execute(search_query, tuple(request))
        result = c.fetchall()
        return result
