#Import all the necesary 

from colorama import Style
from colorama import Fore
from colorama import init
from tripulante import Tripulante
from navio import Navio
from os import system

#Initialice colorama
init(autoreset= True)

def clean_console():
    system("cls")

def title(title):
    print(f"{Fore.LIGHTGREEN_EX}-----{title}-----")

def space():
    print ("\n"*5)
#TESTING

#Test create a crew member
title("Create-Crew-Members (tripulante)".upper())
p1= Tripulante("Luffy","Captain",1300.65,100,100)
p2= Tripulante("Sanji","Chef",3010.3,100,70)
p3= Tripulante("Ussop","Sniper",3250.65,100,80)
print(p1)
print(p2)
print(p3)
space()

#Test work
title("TEST-WORK")
p1.work(5)
p2.work(3)
p3.work(10)
print(p1)
print(p2)
print(p3)
space()

#Test Rest
title("TEST-REST")
p1.rest()
p2.rest()
p3.rest()
print(p1)
print(p2)
print(p3)
space()


#Test Create Navio
title("Create-Navio".upper())
navio= Navio("Going Marry",[p1,p2,p3])
navio.show_manifesto()
space()

#Test Recruit
title("TEST-RECRUIT-CREW-MEMBER")
p4= Tripulante("Nami","Navigator",389.43,88,50)
navio.recruit(p4)
#p5= Tripulante("Nami","Janitor",563.23,85,30)
#navio.recruit(p5)
navio.show_manifesto()
print(f"{Fore.LIGHTWHITE_EX}New member recluted: {navio.crew[-1]} ")
space()

#Test Kick
title("TEST-KICK-CREW-MEMBER")
navio.show_manifesto()
status=navio.kick("Nami")
#status=navio.kick("Nami")

if status == True:
    print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTGREEN_EX}{status} ")
else:
    print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTRED_EX}{status} ")

space()

#Test total Power
title("TEST-TOTAL-POWER")
navio.show_manifesto()
print(f"{Fore.LIGHTWHITE_EX}Total Power: {Fore.LIGHTYELLOW_EX}{navio.total_power()} ")
space()

#Show final manifesto
title("MANIFESTO")
navio.show_manifesto()
print(f"{Fore.LIGHTWHITE_EX}Total Power: {Fore.LIGHTYELLOW_EX}{navio.total_power()} ")




