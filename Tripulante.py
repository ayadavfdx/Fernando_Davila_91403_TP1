#Import library "Colorama"
from colorama import Style
from colorama import Fore
from colorama import init
#Initialize Colorama
init()

#Define Class
class Tripulante():
    def __init__(self,name,role,bounty,power,energy):
        self.__name=str(name)
        self.__role=str(role)
        self.__bounty=float(bounty)
        self.power=int(power)
        self.energy=int(energy)

    #Function to validate range to 0-100
    def __validate_range(self,value):
        if value <0 or value > 100:
            raise ValueError(Fore.BLUE + "Must be a value between (0-100) try again!".upper() + Style.RESET_ALL)
        else:    
            return value
    
    #Use getters, make private attributes

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
    
    #Use a setter to validate range 0-100
    @power.setter
    def power(self,value):
        self.__power= self.__validate_range(value)

    @property
    def energy(self):
        return self.__energy
    
    #Use a setter to validate range 0-100
    @energy.setter
    def energy(self,value):
        self.__energy= self.__validate_range(value)

    def __str__(self):
        return (f"«{self.__name} [{self.__role}] -Bounty:{self.__bounty} |Power: {self.power} |Energy: {self.energy}» ")

p1= Tripulante("Zoro","Janitor",350,300,300)
print(p1)