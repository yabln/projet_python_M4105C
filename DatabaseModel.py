class Installation :
    """
        Class representing the Installation object
        While be created using datas from the installations_table.csv file
    """
    
    def __init__(self, id, name, address, postal_code, city, latitude, longitude):
        """
            Constructor of the Installation object
            Note that the dictionary containing references to equipements is not
            initialised here
        """
        self.id = id
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longotude = longitude
    
    def set_equipements(self, equipement_list):
        """
            Function used to set the equipements contained within an installation
        """
        self.equipements = equipement_list
        

class Equipement :
    """
        Class representig the Equipement object
        While be created using datas from the equipements.csv file
        It is composed of a unique id, a name, and has a reference to the 
        installation it is linked to in the database
    """
    
    def __init__(self, id, name, installation_ref):
        """
            Constructor of the Equipement object
        """
        self.id = id
        self.name = name
    
    def set_activities(self, activities_list):
        """
            Function used to set the activities that while use the current equipement
        """
        self.activities = activities_list
        

class Activity :
    """
        Class representig the Activity object
        While be created using datas from the equipements_activites.csv file
        It is composed of a unique id, a name and a table containing the references
        to every equipement it is linked to
    """
    
    def __init__(self, id, name, equipement_refs):
        """
            Constructor of the Activity object
        """
        self.id = id
        self.name = name
        self.equipement_refs = equipement_refs
        


    