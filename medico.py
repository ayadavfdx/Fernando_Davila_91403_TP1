
#Import all necessary
from tripulante import Tripulante
from colorama import Style,Fore,init


#Initialize colorama
init(autoreset=True)

class Medico(Tripulante):
    def __init__(self,name,bounty,power,energy,pacientes_curados=0):
        super().__init__(name,bounty,power,energy)
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


    def __str__(self):
        info= super().__str__()
        return (f"{info} {Fore.LIGHTWHITE_EX}|pacientes_curados:{Style.RESET_ALL} {self.random_colors()}{self.__pacientes_curados}")
