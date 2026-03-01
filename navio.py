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
        return round(total,2)
    
    #METHODS


    #Function to recruit 
    def recruit(self,new_tripulante):
        for crew_member in self.__crew:
            if crew_member.name == new_tripulante.name:
                raise ValueError(f"{Fore.LIGHTWHITE_EX} Tripulante already exists")
            
        self.__crew.append(new_tripulante)

    #Function to kick
    def kick(self,name_tripulante):
        for crew_member in self.__crew:
            if crew_member.name== name_tripulante:
                self.__crew.remove(crew_member)
                return True
        
        return False
    
    #Function to calculate total power of the crew
    def total_power(self):
        total=0
        for power in self.__crew:
            total += power.power
        return total

    #Function to show manifesto
    def show_manifesto(self):
        print(f"{Fore.LIGHTWHITE_EX}Navio:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{self.__name}")
        print(f" ")
        print(f"{Fore.LIGHTWHITE_EX}Crew:")
        for crew in self.__crew:
            print(crew)
        print(" ")
        print(f"{Fore.LIGHTWHITE_EX}Total Bounty: {Fore.LIGHTRED_EX}{self.total_bounty} M{Style.RESET_ALL}")




