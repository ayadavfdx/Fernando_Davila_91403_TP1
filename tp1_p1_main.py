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

def pause():
    input(
        f"\n{Fore.LIGHTWHITE_EX}Press{Style.RESET_ALL}"
        f"{Fore.LIGHTBLUE_EX}Enter{Style.RESET_ALL} to continue..."
        )

def space():
    print ("\n"*5)

#Crew for testing
p1= Tripulante("Luffy",1300.65,100,100)
p2= Tripulante("Sanji",3010.3,100,70)
p3= Tripulante("Ussop",3250.65,100,80)
navio_test= Navio("Boat",[p1,p2,p3])
#TESTING

#Test create a crew member
def test_create_members():
    title("Create-Crew-Members (tripulante)".upper())
    print(p1)
    print(p2)
    print(p3)

#Test work
def test_work():
    title("TEST-WORK")
    p1.trabalhar(5)
    p2.trabalhar(3)
    p3.trabalhar(10)
    print(p1)
    print(p2)
    print(p3)


#Test Rest
title("TEST-REST")
p1.descansar()
p2.descansar()
p3.descansar()
print(p1)
print(p2)
print(p3)
space()


#Test Create Navio
title("Create-Navio".upper())
navio= Navio("Going Marry",[p1,p2,p3],100)
navio.mostrar_manifesto()
space()

#Test Recruit
title("TEST-RECRUIT-CREW-MEMBER")
p4= Tripulante("Nami",389.43,88,50)
navio.recrutar(p4)
#p5= Tripulante("Nami","Janitor",563.23,85,30)
#navio.recruit(p5)
navio.mostrar_manifesto()
print(f"{Fore.LIGHTWHITE_EX}New member recluted: {navio.tripulacao[-1]} ")
space()

#Test Kick
title("TEST-KICK-CREW-MEMBER")
navio.mostrar_manifesto()
status=navio.expulsar("Nami")
#status=navio.expulsar("Nami")

if status == True:
    print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTGREEN_EX}{status} ")
else:
    print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTRED_EX}{status} ")

space()

#Test total Power
title("TEST-TOTAL-POWER")
navio.mostrar_manifesto()
print(f"{Fore.LIGHTWHITE_EX}Total Power: {Fore.LIGHTYELLOW_EX}{navio.calcular_poder_total()} ")
space()

#Show final manifesto
title("MANIFESTO")
navio.mostrar_manifesto()
print(f"{Fore.LIGHTWHITE_EX}Total Power: {Fore.LIGHTYELLOW_EX}{navio.calcular_poder_total()} ")




