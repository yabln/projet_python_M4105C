#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Installation :
    """
        Class representing the Installation object
        While be created using datas from the installations_table.csv file
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
        self.equipements = set()
        
    def add_equipements(self, equipement):
        """
            Function used to set the equipement of the current installation
        """
        self.equipements.add(equipement)
    


class Equipement :
    """
        Class representig the Equipement object
        While be created using datas from the equipements.csv file
        It is composed of a unique id, a name, and has a reference to the
        installation it is linked to in the database
    """

    def __init__(self, id, name, installation):
        """
            Constructor of the Equipement object
        """
        self.id = id
        self.name = name
        self.installation = installation
        self.activities = set()

    def add_activity(self, activity):
        """
            Function used to set the activities that while use the current equipement
        """
        self.activities.add(activity)


class Activity :
    """
        Class representig the Activity object
        While be created using datas from the equipements_activites.csv file
        It is composed of a unique id, a name and a table containing the references
        to every equipement it is linked to
    """

    def __init__(self, id, name, equipement):
        """
            Constructor of the Activity object
        """
        self.id = id
        self.name = name
        self.equipement_refs = set()
        self.equipement_refs.add(equipement)

    def add_equipement(self, equipement):
        """
            Function used to set the activities that while use the current equipement
        """
        self.equipement_refs.add(equipement)
