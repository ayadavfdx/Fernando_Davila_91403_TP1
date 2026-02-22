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
    
    #Property to calculate bounty
    @property
    def total_bounty(self):
        total=0
        for i in self.__crew:
            total += i.bounty
        return total
    
    #Function to add colors to total bounty
    def add_bounty_color(self):
        print(f"Total Bounty of the crew:{Fore.RED}{self.total_bounty}{Style.RESET_ALL}")

p1= Tripulante("zoro","sword",300.423,100,100)
p2= Tripulante("pepe","sword",500.45,100,100)

navio=Navio("Olha",[p1,p2])
print(f"{navio.total_bounty}")