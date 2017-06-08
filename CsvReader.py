#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import csv

from DatabaseModel import *


class CsvReader:
    """
         Class read et parse the Csv files
    """

    def __init__(self):
        """
              Constructor of the CsvReader object
        """
        self.installations = {}
        self.equipments = {}
        self.activities = {}

    def parse_csv_files(self):
        """
              Parse the 3 Csv files
              Create object from fields and add it to list
        """
        with codecs.open('installations.csv', 'rb', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                address = ""
                if row['Nom du lieu dit']:
                    if row['Nom de la voie']:
                        address = row['Nom du lieu dit'] + ", " + row['Numero de la voie'] + " " + row['Nom de la voie']
                    else:
                        address = row['Numero de la voie'] + " " + row['Nom du lieu dit']
                else:
                    address = row['Numero de la voie'] + " " + row['Nom de la voie']

                tmp_installation = Installation(row['Numéro de l\'installation'], row['Nom usuel de l\'installation'],
                                                address, row['Code postal'], row['Nom de la commune'], row['Latitude'],
                                                row['Longitude'])
                self.installations[row['Numéro de l\'installation']] = tmp_installation

        with codecs.open('equipements.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tmp_equipement = Equipment(row['EquipementId'], row['EquNom'],
                                           self.installations.get(row['InsNumeroInstall']))
                self.equipments[row['EquipementId']] = tmp_equipement

        with codecs.open('activites.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['ActCode'] != '':
                    if row['ActCode'] not in self.activities.keys():
                        tmp_activity = Activity(row['ActCode'], row['ActLib'], self.equipments[row['EquipementId']])
                        self.activities[row['ActCode']] = tmp_activity
                        self.equipments[row['EquipementId']].add_activity(tmp_activity)
                    else:
                        self.activities[row['ActCode']].add_equipment(self.equipments[row['EquipementId']])
                        self.equipments[row['EquipementId']].add_activity(self.activities[row['ActCode']])
