#Import all the necesary 

from colorama import Style
from colorama import Fore
from colorama import init
from Tripulante import Tripulante
from Navio import Navio
from os import system

#Initialice colorama
init(autoreset= True)

def clean_console():
    system("cls")

def title(title):
    print(f"{Fore.LIGHTGREEN_EX}-----{title}-----")

#TESTING
title("Create Crew Members (tripulante)")
p1= Tripulante("Luffy","Captain",900,100,100)
p2= Tripulante("Sanji","Chef",500,80,100)
p3= Tripulante("Ussop","Sniper",350,75,100)
print(p1)
print(p2)
print(p3)