#Import all the necesary files/libraries
from colorama import Style
from colorama import Fore
from colorama import init
from Tripulante import Tripulante

#Initialice colorama
init(autoreset= True)

class Navio:
    def __init__(self,name,crew):
        self.__name=str(name)

        #Validate objets of class Tripulante
        if isinstance(crew,list):
            for people in crew:
                if isinstance(people,Tripulante):
                    self.__crew=crew
                else:
                    self.__crew= None
        else:
            self.__crew= None

    #Create getter, make private attributes
    @property
    def name(self):
        return self.__name
    
    @property
    def crew(self):
        return self.__crew