#Import all the necesary files/libraries
from colorama import Style
from colorama import Fore
from colorama import init
from tripulante import Tripulante

#Initialice colorama
init(autoreset= True)

class Navio:
    def __init__(self,name,crew,life=100,gold=0):
        self.__name=str(name)
        self.life=int(life)
        self.gold=int(gold)

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
    
    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self,value):
        if value <0 or value > 100:
            raise ValueError(Fore.BLUE + "Must be a value between (0-100) try again!".upper() + Style.RESET_ALL)
        else:    
            self.__life=value
            if value ==0:
                print(Fore.RED + "---GAME OVER---" + Style.RESET_ALL)
    
    #Function to show hearths in console
    @property
    def show_hearths(self):
        hearth= self.__life
        bar= hearth//10

        if hearth == 0:
            return (f"{' '}")
        elif 0 < hearth <=10:
            return (f"{'💙'}")
        else:
            return (f"{'💙' * bar}")



    @property
    def gold(self):
        return self.__gold
    
    @gold.setter
    def gold(self,value):
        if value <0:
            raise ValueError(Fore.BLUE +"GOLD CANNOT BE UNDER 0" + Style.RESET_ALL)
        else:
            self.__gold=value

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

    #Function to add life
    def repair(self,value):
        gained_life= self.__life + value
        return gained_life

    #Function to damage life
    def damage(self,value):
        reduced_life= self.__life - value
        return reduced_life
    
    #Function to obtain gold
    def obtain_gold(self,value):
        get_gold= self.__gold + value
        return get_gold

    #Function to show manifesto
    def show_manifesto(self):
        print(f"{Fore.LIGHTWHITE_EX}Navio:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{self.__name}")
        print(f" ")
        print(f"{Fore.LIGHTWHITE_EX}Crew:")
        for crew in self.__crew:
            print(crew)
        print(" ")
        print(f"{Fore.LIGHTWHITE_EX}Total Bounty: {Fore.LIGHTRED_EX}{self.total_bounty} M{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}Life: {self.show_hearths} {self.__life} {Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}Gold:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX} {self.__gold} {Style.RESET_ALL} ")


