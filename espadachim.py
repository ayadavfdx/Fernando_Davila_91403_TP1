
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Espadachim(Tripulante):
    def __init__(self,nome,recompensa=0.0,poder=0,energia=100,espadas=[]):
        super().__init__(nome,recompensa,poder,energia)
        self.__espadas=list(espadas)

    @property
    def espadas(self):
        return self.__espadas
    
    def executar_acao(self,navio):
        bonus= 10* len(self.__espadas)
        self.poder += bonus
        print(
        f"{self.random_colors()}{self.nome}{Style.RESET_ALL}{Fore.LIGHTWHITE_EX} attacked"
        f", Current poder:{Style.RESET_ALL}{self.random_colors()}{self.poder}{Style.RESET_ALL}"
            )

    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|Swords:{Style.RESET_ALL} {self.random_colors()}{', '.join(self.__espadas)}")

