#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

from CsvReader import *


class DatabaseAdmin:
    """
        This class has the goal to create, access, modify or destroy the sqlite3 database used to store the project data
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
        c.execute("DROP TABLE IF EXISTS Equipment;")
        c.execute("DROP TABLE IF EXISTS Activity;")
        c.execute("DROP TABLE IF EXISTS EquipmentActivity;")

        c.execute("CREATE TABLE Installation (Id INTEGER PRIMARY KEY, Name TEXT, Address TEXT, "
                  "PostalCode INTEGER, City TEXT, Latitude REAL, Longitude Real);")

        c.execute("CREATE TABLE Equipment (Id INTEGER PRIMARY KEY, Name TEXT, "
                  "IdInstallation INTEGER, FOREIGN KEY(IdInstallation) REFERENCES Installation(Id));")

        c.execute("CREATE TABLE Activity (Id INTEGER PRIMARY KEY, Name TEXT);")

        c.execute(
            "CREATE TABLE EquipmentActivity (IdEquipment INTEGER, IdActivity INTEGER, PRIMARY KEY (IdEquipment, "
            "IdActivity));")

        conn.commit()
        conn.close()

    def insert_from_csv_reader(self, reader):
        """
            Takes a CsvReader and adds the contained objects into the database
        """

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for installation_key in reader.installations:
            insert_query = "INSERT INTO Installation(Id, Name, Address, PostalCode, City, Latitude, Longitude) " \
                           "VALUES(?, ?, ?, ?, ?, ?, ?) "
            install = reader.installations[installation_key]
            c.execute(insert_query, (
                install.id, install.name, install.address, install.postal_code, install.city, install.latitude,
                install.longitude))

        for activity_key in reader.activities:
            insert_query = "INSERT INTO Activity(Id, Name) VALUES(?, ?)"
            act = reader.activities[activity_key]
            c.execute(insert_query, (act.id, act.name))

        for equipment_key in reader.equipements:
            insert_query = "INSERT INTO Equipment(Id, Name, IdInstallation) VALUES(?, ?, ?)"
            equip = reader.equipements[equipment_key]
            c.execute(insert_query, (equip.id, equip.name, equip.installation.id))

            for act in equip.activities:
                insert_query = "INSERT INTO EquipmentActivity(IdEquipment, IdActivity) VALUES(?, ?)"
                c.execute(insert_query, (equip.id, act.id))

        conn.commit()
        conn.close()

    def get_search_result(self, user_input):
        """
        Takes a user input, verify that it's conform, and then make a SQL request to fetch elements whose names
        correspond to that input
        """

        conn = sqlite3.connect(self.db_name)

        request_field = '%' + user_input[0].strip() + '%'
        request_city = '%' + user_input[1].strip() + '%'

        activity_ids = []
        activities_dictionary = {}
        activities_array = self.search_activity(conn, request_field)
        for data in activities_array:
            activity_ids.append(data[0])
            activities_dictionary[data[0]] = data[1]

        equipment_activity_ids = {}
        equipment_ids = []
        for data in self.get_equipments_by_activity(conn, activity_ids):
            equipment_ids.append(data[0])
            if data[0] in equipment_activity_ids:
                equipment_activity_ids.get(data[0]).append(data[1])
            else:
                equipment_activity_ids[data[0]] = [data[1]]

        equipments_array = self.get_equipments_by_ids(conn, equipment_ids)

        installation_ids = []
        for data in equipments_array:
            if not (data[2] in installation_ids):
                installation_ids.append(data[2])

        installations_list = []
        for data_installation in self.search_installation(conn, request_city, installation_ids):
            current_installation = Installation(data_installation[0], data_installation[1], data_installation[2],
                                                data_installation[3], data_installation[4], data_installation[5],
                                                data_installation[6])
            for data_equipment in equipments_array:
                if data_equipment[2] == current_installation.id:
                    current_equipment = Equipment(data_equipment[0], data_equipment[1], data_equipment[2])
                    for key in equipment_activity_ids.keys():
                        if key == current_equipment.id:
                            for value in equipment_activity_ids.get(key):
                                current_equipment.add_activity(Activity(value, activities_dictionary.get(value)))

                    current_installation.add_equipment(current_equipment)
                    equipments_array.remove(data_equipment)

            installations_list.append(current_installation)

        conn.close()

        return installations_list

    @staticmethod
    def search_installation(conn, city, ids):
        """
            Search the Installation table and get the lines that matches the city name in the request
        """

        c = conn.cursor()
        params = [city] + ids
        search_query = "SELECT * FROM Installation T1 WHERE T1.City LIKE ? AND T1.Id IN ({})".format(
            ",".join(["?"] * len(ids)))

        c.execute(search_query, params)
        result = c.fetchall()
        return result

    @staticmethod
    def search_activity(conn, request):
        """
            Search the Activity table to get lines that matches the request
        """

        c = conn.cursor()
        search_query = "SELECT * FROM Activity T1 WHERE T1.Name LIKE ?"
        c.execute(search_query, (request,))
        result = c.fetchall()
        return result

    @staticmethod
    def get_equipments_by_activity(conn, request):
        """
            For a set of activities' id passed in argument, returns a set of the equipments' id linked to the former
        """

        c = conn.cursor()
        search_query = "SELECT * FROM EquipmentActivity T1 WHERE T1.IdActivity IN ({})".format(
            ",".join(["?"] * len(request)))
        c.execute(search_query, tuple(request))
        result = c.fetchall()
        return result

    @staticmethod
    def get_equipments_by_ids(conn, request):
        """
            Fetch all equipments in the table via their Ids
        """

        c = conn.cursor()
        search_query = "SELECT * FROM Equipment T1 WHERE T1.Id IN ({})".format(",".join(["?"] * len(request)))
        c.execute(search_query, tuple(request))
        result = c.fetchall()
        return result
