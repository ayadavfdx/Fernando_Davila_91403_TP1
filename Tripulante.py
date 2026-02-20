#Import library "Colorama"
from colorama import Style
from colorama import Fore
from colorama import init
#Initialize Colorama
init()

#Define Class
class Tripulantes():
    def __init__(self,name,role,bounty,power,energy):
        self.__name=name
        self.__role=role
        self.__bounty=bounty
        self.__power=power
        self.__energy=energy

    #Use getters and setters
    @property
    def name(self):
        return self.__name
    
    @property
    def role(self):
        return self.__role
    
    @property
    def bounty(self):
        return self.__bounty
    
    @property
    def power(self):
        return self.__power
    
    @property
    def energy(self):
        return self.__energy