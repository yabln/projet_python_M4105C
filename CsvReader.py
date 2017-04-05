#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
from equipement import Equipement
from DatabaseModel import *
import codecs

class CsvReader:
     """
         Class read et parse the Csv files
     """     
     
     def __init__(self):
          """
              Constructor of the CsvReader object
          """          
          self.installations = {}
          self.equipements = {}
          self.activities = {}          
    
     
     def parse_Csv_files(self):
          """
              Parse the 3 Csv files
              Create object from fields and add it to list
          """          
          with codecs.open('installations.csv', encoding = 'utf-8') as csvfile:
               reader = csv.DictReader(csvfile)
               for row in reader:          
                    adresse= ""
                    if (row['Nom du lieu dit']):
                         if (row['Nom de la voie']):
                              adresse = row['Nom du lieu dit'] + ", " + row['Numero de la voie'] + " " + row['Nom de la voie']
                         else:
                              adresse = row['Numero de la voie'] + " " + row['Nom du lieu dit']
                    else:
                         adresse = row['Numero de la voie'] + " " + row['Nom de la voie']
                         
                    tmp_installation = Installation(row['Numéro de l\'installation'], row['Nom usuel de l\'installation'], adresse, row['Code postal'], row['Nom de la commune'], row['Latitude'], row['Longitude'])
                    self.installations[row['Numéro de l\'installation']] = tmp_installation
          
          with codecs.open('equipements.csv', encoding = 'utf-8') as csvfile:
               reader = csv.DictReader(csvfile)
               for row in reader:
                    tmp_equipement = Equipement(row['EquipementId'], row['EquNom'], self.installations.get(row['InsNumeroInstall']))
                    self.equipements[row['EquipementId']] = tmp_equipement
          
          
          with codecs.open('activites.csv', encoding = 'utf-8') as csvfile:
               reader = csv.DictReader(csvfile)
               for row in reader:
                    if (row['ActCode'] not in activities):
                         tmp_activiti = Activity(row['ActCode'], row['ActLib'], self.equipements[row['EquipementId']])
                         self.equipements[row['EquipementId']].add_activitie(tmp_activiti)
                    else:
                         self.activities[row['ActCode']].add_equipement(self.equipements[row['EquipementId']])
                         self.equipements[row['EquipementId']].add_activitie(activities[row['ActCode']])          


          
