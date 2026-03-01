#Import all the necesary files/libraries
from colorama import Style
from colorama import Fore
from colorama import init
from tripulante import Tripulante

#Initialice colorama
init(autoreset= True)

class Navio:
    def __init__(self,nome,tripulacao=None,vida=100,ouro=0):
        self.__nome=str(nome)
        self.vida=int(vida)
        self.ouro=int(ouro)

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
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self,value):
        if value <0:
            self.__vida=0
        elif value >100:
            self.__vida = 100
        else:
            self.__vida= value

        if value ==0:
            print(Fore.RED + "---GAME OVER---" + Style.RESET_ALL)
    
    #Function to show hearths in console
    @property
    def show_hearths(self):
        hearth= self.__vida
        bar= hearth//10

        if hearth == 0:
            return (f"{' '}")
        elif 0 < hearth <=10:
            return (f"{'💙'}")
        else:
            return (f"{'💙' * bar}")



    @property
    def ouro(self):
        return self.__ouro
    
    @ouro.setter
    def ouro(self,value):
        if value <0:
            self.__ouro=0
        else:
            self.__ouro=value

    #Property to calculate bounty
    @property
    def recompensa_total(self):
        total=0
        for b in self.__tripulacao:
            total += b.recompensa
        return round(total,2)
    
    #METHODS


    #Function to recrutar 
    def recrutar(self,novo_tripulante):
        for tripulacao_member in self.__tripulacao:
            if tripulacao_member.nome == novo_tripulante.nome:
                raise ValueError(f"{Fore.LIGHTWHITE_EX} Tripulante already exists")
            
        self.__tripulacao.append(novo_tripulante)

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
            total += power.poder
        return total

    #Function to add vida
    def reparar(self,value):
        self.vida += value

    #Function to damage vida
    def danificar(self,value):
        self.vida -= value
    
    #Function to obtain ouro
    def ganhar_ouro(self,value):
        self.ouro += value

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
        print(f"{Fore.LIGHTWHITE_EX}vida: {self.show_hearths} {self.__vida} {Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}ouro:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX} {self.__ouro} {Style.RESET_ALL} ")


