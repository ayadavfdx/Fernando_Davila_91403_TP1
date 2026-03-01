#Import all the necesary files/libraries
from colorama import Style
from colorama import Fore
from colorama import init
from tripulante import Tripulante

#Initialice colorama
init(autoreset= True)

class Navio:
    def __init__(self,nome,tripulacao,life=100,gold=0):
        self.__nome=str(nome)
        self.life=int(life)
        self.gold=int(gold)

        #Validate objets of class Tripulante
        if isinstance(tripulacao,list):
            for people in tripulacao:
                if isinstance(people,Tripulante):
                    self.__tripulacao=tripulacao
                else:
                    self.__tripulacao= None
        else:
            self.__tripulacao= None

    #Create getter, make private attributes
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tripulacao(self):
        return self.__tripulacao
    
    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self,value):
        if value <0:
            self.__life=0
        elif value >100:
            self.__life = 100
        else:
            self.__life= value

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
    def recompensa_total(self):
        total=0
        for b in self.__tripulacao:
            total += b.bounty
        return round(total,2)
    
    #METHODS


    #Function to recrutar 
    def recrutar(self,new_tripulante):
        for tripulacao_member in self.__tripulacao:
            if tripulacao_member.nome == new_tripulante.nome:
                raise ValueError(f"{Fore.LIGHTWHITE_EX} Tripulante already exists")
            
        self.__tripulacao.append(new_tripulante)

    #Function to expulsar
    def expulsar(self,nome_tripulante):
        for tripulacao_member in self.__tripulacao:
            if tripulacao_member.nome== nome_tripulante:
                self.__tripulacao.remove(tripulacao_member)
                return True
        
        return False
    
    #Function to calculate total power of the tripulacao
    def calcular_poder_total(self):
        total=0
        for power in self.__tripulacao:
            total += power.power
        return total

    #Function to add life
    def reparar(self,value):
        self.life += value

    #Function to damage life
    def danificar(self,value):
        self.life -= value
    
    #Function to obtain gold
    def ganhar_ouro(self,value):
        self.gold += value

    #Function to action
    def executar_acao(self,navio):
        print(f"This message will be replaced")


    #Function to show manifesto
    def mostrar_manifesto(self):
        print(f"{Fore.LIGHTWHITE_EX}Navio:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{self.__nome}")
        print(f" ")
        print(f"{Fore.LIGHTWHITE_EX}tripulacao:")
        for tripulacao in self.__tripulacao:
            print(tripulacao)
        print(" ")
        print(f"{Fore.LIGHTWHITE_EX}Total Bounty: {Fore.LIGHTRED_EX}{self.recompensa_total} M{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}Life: {self.show_hearths} {self.__life} {Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}Gold:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX} {self.__gold} {Style.RESET_ALL} ")


