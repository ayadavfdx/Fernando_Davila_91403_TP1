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
        for b in self.__crew:
            total += b.bounty
        return total
    
    #METHODS

    #Function to recruit 
    def recruit(self,new_tripulante):
        self.__crew.append(new_tripulante)

    #Function to kick
    def kick(self,name_tripulante):
        for crew_member in self.__crew:
            if crew_member== name_tripulante:
                self.__crew.remove(crew_member)
                return True
        
        return False

    #Function to calculate total power of the crew
    def total_power(self):
        total=0
        for power in self.__crew:
            total += power.power
        return total




p1= Tripulante("zoro","sword",300.423,100,100)
p2= Tripulante("pepe","sword",500.45,100,100)
p3= Tripulante("Adam","xyz",222,45,67)

navio=Navio("Olha",[p1,p2])
navio.recruit(p3)

navio.show_manifesto()