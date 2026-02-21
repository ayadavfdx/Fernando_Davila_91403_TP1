#Import library "Colorama and Random"
from random import choice
from colorama import Style
from colorama import Fore
from colorama import init
#Initialize Colorama
init(autoreset=True)

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

    #Function to read the state of the energy and change color
    @property
    def energy_color(self):
        if 0< self.__energy <=20:
            return (f"{Fore.RED} {self.__energy} {Style.RESET_ALL}")
        elif  20< self.__energy <=50:
            return (f"{Fore.YELLOW} {self.__energy} {Style.RESET_ALL}")
        else:
            return (f"{Fore.GREEN} {self.__energy} {Style.RESET_ALL}")
    
    #String to show in console
    def __str__(self):
        return (f"{self.random_colors()}«{self.__name} [{self.__role}]{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}-Bounty:{Style.RESET_ALL}{self.random_colors()}{self.__bounty} M {Fore.LIGHTWHITE_EX}|Power: {Style.RESET_ALL}{self.random_colors()}{self.power} {Style.RESET_ALL}{Fore.LIGHTWHITE_EX}|Energy:{Style.RESET_ALL}{self.energy_color}  » ")

    #Function to choose random colors
    def random_colors(self):
        colors=[Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.BLUE,Fore.LIGHTMAGENTA_EX,Fore.LIGHTBLUE_EX]
        return choice(colors)
    


p1= Tripulante("Zoro","Janitor",350,100,20)
p2= Tripulante("Lufi","Pirate",900,100,80)
print(p1)
print(p2)