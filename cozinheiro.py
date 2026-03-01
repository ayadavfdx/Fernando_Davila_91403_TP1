
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Medico(Tripulante):
    def __init__(self,name,bounty,power,energy,refeicoes_preparadas=0):
        super().__init__(name,bounty,power,energy)
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


    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|Food Cooked:{Style.RESET_ALL} {self.random_colors()}{self.__refeicoes_preparadas}")
