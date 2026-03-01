#Import library "Colorama Random Os"
from random import choice
from colorama import Style
from colorama import Fore
from colorama import init
from colorama import Back

#Initialize Colorama
init(autoreset=True)

#Define Class
class Tripulante():
    def __init__(self,nome,recompensa,poder,energia=100,status = "Ok"):
        self.__nome=str(nome)
        self.__recompensa=float(recompensa)
        self.poder=int(poder)
        self.energia=int(energia)
        self.__status= status

    #Function to validate range to 0-100
    def __validate_range(self,value):
        if value <0:
            return 0
        elif value >100:
            return 100
        else:    
            return value
    
    #Use getters, make private attributes

    @property
    def nome(self):
        return self.__nome
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def poder(self):
        return self.__poder
    
    #Use a setter to validate range 0-100
    @poder.setter
    def poder(self,value):
        self.__poder= self.__validate_range(value)

    @property
    def energia(self):
        return self.__energia
    
    #Use a setter to validate range 0-100
    @energia.setter
    def energia(self,value):
        self.__energia= self.__validate_range(value)

    #Function to read the state of the energia and change color
    @property
    def energia_color(self):
        energia= self.__energia
        bar= energia //10
        if 0<= self.__energia <=20:
            return (f"{Back.RED}{' '*3}{Style.RESET_ALL}{Fore.RED} {energia} %{Style.RESET_ALL}")
        elif  20< self.__energia <=50:
            return (f"{Back.YELLOW}{" "*bar}{Style.RESET_ALL}{Fore.YELLOW} {energia} %{Style.RESET_ALL}")
        else:
            return (f"{Back.GREEN}{" "*bar}{Style.RESET_ALL}{Fore.GREEN} {energia} %{Style.RESET_ALL}")
    
    @property
    def status(self):
        return self.__status


    #String to show in console
    def __str__(self):
        return (
    f"{self.random_colors()}«{self.__nome} [{type(self).__name__}]\n"
    f"{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}-recompensa:{Style.RESET_ALL}"
    f"{self.random_colors()}{self.__recompensa} M "
    f"{Fore.LIGHTWHITE_EX}|poder: {Style.RESET_ALL}"
    f"{self.random_colors()}{self.poder} "
    f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}|energia:"
    f"{Style.RESET_ALL}{self.energia_color}  » "
                )

    #Function to choose random colors
    def random_colors(self):
        colors=[Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.BLUE,Fore.LIGHTMAGENTA_EX,Fore.LIGHTBLUE_EX]
        return choice(colors)
    
    #Methods
    def trabalhar(self,time):
        self.energia -= time*5

    def descansar(self):
        self.energia= 100



