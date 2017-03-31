

class Installation :
    """
        Class representing the Installation object
        While be created using datas from the installations_table.csv file
    """
    def __init__(self, id, name, address, postal_code, city, latitude, longitude):
        self.id = id
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longotude = longitude




class Activity :
    """
        Class representig the Activity object
        While be created using datas from the equipements_activites.csv file
        It is composed of a unique id and a name
    """
    def __init__(self, id, name):
        """
            Constructor of the Activity object
        """
        self.id = id
        self.name = name
        


class Equipement :
    """
        Class representig the Equipement object
        While be created using datas from the equipements.csv file
    """
    
    def __init__(self, id, name):
        """
            Constructor of the Equipement object
        """
        self.id = id
        self.name = name
    