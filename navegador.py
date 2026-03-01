
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Navegador(Tripulante):
    def __init__(self,nome,recompensa=0.0,poder=0,energia=100,milhas_navegadas=0):
        super().__init__(nome,recompensa,poder,energia)
        self.milhas_navegadas=int(milhas_navegadas)

    @property
    def milhas_navegadas(self):
        return self.__milhas_navegadas
    
    @milhas_navegadas.setter
    def milhas_navegadas(self,value):
        if value <0:
            self.__milhas_navegadas=0
        else:
            self.__milhas_navegadas= value

    def executar_acao(self,navio):
        self.__milhas_navegadas += 50
        print(
            f"{self.random_colors()}{self.nome}{Style.RESET_ALL}{Fore.LIGHTWHITE_EX} Took a safer way "
            f"+50 miles, (Total: {Style.RESET_ALL}{self.milhas_navegadas})"
            )

    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|Milhas_navegadas:{Style.RESET_ALL} {self.random_colors()}{self.__milhas_navegadas}")
