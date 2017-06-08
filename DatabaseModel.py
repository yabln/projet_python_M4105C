#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Installation:
    """
        Class representing the Installation object
        While be created using data from the installations.csv file
    """

    def __init__(self, id, name, address, postal_code, city, latitude, longitude):
        """
            Constructor of the Installation object
        """
        self.id = id
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.equipments = set()

    def add_equipment(self, equipment):
        """
            Function used to add a new equipment to the current installation
        """
        self.equipments.add(equipment)


class Equipment:
    """
        Class representing the Equipment object
        While be created using data from the equipements.csv file
        It is composed of a unique id, a name, and has a reference to the
        installation it is linked to in the database
    """

    def __init__(self, id, name, installation):
        """
            Constructor of the Equipment object
        """
        self.id = id
        self.name = name
        self.installation = installation
        self.activities = set()

    def add_activity(self, activity):
        """
            Function used to set the activities that while use the current equipment
        """
        self.activities.add(activity)


class Activity:
    """
        Class representing the Activity object
        While be created using data from the activites.csv file
        It is composed of a unique id, a name and a table containing the references
        to every equipment it is linked to
    """

    def __init__(self, id, name, equipment=None):
        """
               Constructor of the Activity object
        """
        self.id = id
        self.name = name
        self.equipment_refs = set()
        if equipment is not None:
            self.equipment_refs.add(equipment)

    def add_equipment(self, equipment):
        """
            Function used to set the activities that while use the current equipment
        """
        self.equipment_refs.add(equipment)
