
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Medico(Tripulante):
    def __init__(self,nome,recompensa=0.0,poder=0,energia=100,pacientes_curados=0):
        super().__init__(nome,recompensa,poder,energia)
        self.pacientes_curados=int(pacientes_curados)

    @property
    def pacientes_curados(self):
        return self.__pacientes_curados
    
    @pacientes_curados.setter
    def pacientes_curados(self,value):
        if value <0:
            self.__pacientes_curados=0
        else:
            self.__pacientes_curados= value

    def executar_acao(self,navio):
        injured= min(navio.tripulacao, key=lambda e:e.energia)
        injured.energia +=40
        self.pacientes_curados += 1

        print(
            f"{self.random_colors()}{self.nome}{Style.RESET_ALL} {Fore.LIGHTWHITE_EX} healed "
            f"{Style.RESET_ALL}{self.random_colors()}{injured.nome}{Style.RESET_ALL}"
            f"{Fore.LIGHTWHITE_EX}energia is now {Style.RESET_ALL}"
            f"{ self.random_colors()}{injured.energia}{Style.RESET_ALL}"
        )

    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|Cured:{Style.RESET_ALL} {self.random_colors()}{self.__pacientes_curados}")
