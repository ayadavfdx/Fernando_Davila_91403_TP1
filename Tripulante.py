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
        self.__power=int(power)
        self.__energy=int(energy)

    def give_info(self):
        print(f"""
              |Name:   {self.__name}
              |Role:   {self.__role}
              |Bounty: {self.__bounty}
              |Power:  {self.__power}
              |Energy: {self.energy}  """)


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
    
p1= Tripulante("Zoro","Swordsman","354","1000","50")
p1.give_info()