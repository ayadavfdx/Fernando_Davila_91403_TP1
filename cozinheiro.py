
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Cozinheiro(Tripulante):
    def __init__(self,nome,recompensa,poder,energia=100,refeicoes_preparadas=0):
        super().__init__(nome,recompensa,poder,energia)
        self.refeicoes_preparadas=int(refeicoes_preparadas)

    @property
    def refeicoes_preparadas(self):
        return self.__refeicoes_preparadas
    
    @refeicoes_preparadas.setter
    def refeicoes_preparadas(self,value):
        if value <0:
            self.__refeicoes_preparadas=0
        else:
            self.__refeicoes_preparadas= value

    def executar_acao(self,navio):
        for members in navio.tripulacao:
            members.energia +=20

        self.refeicoes_preparadas +=1
        print(f"{self.random_colors()}{self.nome}{Style.RESET_ALL}{Fore.LIGHTWHITE_EX} prepared a meal! "
            f"Everyone gained +20 energy.{Style.RESET_ALL}"
            )



    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|Food Cooked:{Style.RESET_ALL} {self.random_colors()}{self.__refeicoes_preparadas}")
