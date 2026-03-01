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
def test_rest():
    title("TEST-REST")
    p1.descansar()
    p2.descansar()
    p3.descansar()
    print(p1)
    print(p2)
    print(p3)

#Test Create Navio
def test_show_navio():
    title("Create-Navio".upper())
    navio_test.mostrar_manifesto()

#Test Recruit
def test_recruit():
    title("TEST-RECRUIT-CREW-MEMBER")
    p4= Tripulante("Nami",389.43,88,50)
    navio_test.recrutar(p4)
    #p5= Tripulante("Nami",563.23,85,30)
    #navio_test.recruit(p5)
    navio_test.mostrar_manifesto()
    print(f"{Fore.LIGHTWHITE_EX}New member recluted: {navio_test.tripulacao[-1]} ")


#Test Kick
def test_kick():
    title("TEST-KICK-CREW-MEMBER")
    navio_test.mostrar_manifesto()
    status=navio_test.expulsar("Nami")
    #status=navio_test.expulsar("Nami")

    if status == True:
        print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTGREEN_EX}{status} ")
    else:
        print(f"{Fore.LIGHTWHITE_EX}Kick Status: {Fore.LIGHTRED_EX}{status} ")

#Test total Power
def test_total_power():
    title("TEST-TOTAL-POWER")
    navio_test.mostrar_manifesto()
    print(f"{Fore.LIGHTWHITE_EX}Total Power: {Fore.LIGHTYELLOW_EX}{navio_test.calcular_poder_total()} ")

def menu():
    while True:
        clean_console()
        title(f"{Fore.LIGHTCYAN_EX}---MENU---{Style.RESET_ALL}")

        print("1 - Create Crew Members")
        print("2 - Test Work")
        print("3 - Test Rest")
        print("4 - Show Ship Manifest")
        print("5 - Recruit Member")
        print("6 - Kick Member")
        print("7 - Show Total Power")
        print("8 - Exit")

        option= input("Select an option: ")
        clean_console()

        if option == "1":
            test_create_members()
        elif option == "2":
            test_work()
        elif option == "3":
            test_rest()
        elif option == "4":
            test_show_navio()
        elif option == "5":
            test_recruit()
        elif option == "6":
            test_kick()
        elif option == "7":
            test_total_power()
        elif option == "8":
            print("BYE")
            break
        else:
            print("Select an option")

        pause()

