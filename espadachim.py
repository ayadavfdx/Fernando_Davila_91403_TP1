
#Import all necessary
from tripulante import Tripulante

class Espadachim(Tripulante):
    def __init__(self,espadas=[]):
        super().__init__(name,bounty,power,energy)
        self.__espadas=list(espadas)

    @property
    def espadas(self):
        return self.__espadas
    
    def __str__(self):
        return super().__str__()