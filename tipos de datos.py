import os
import platform
import sys


def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")
def saludar():
    print("hola alienigena ")
    input("")
    clear_cls()
def r_cuadrada():
    x=int(input("a que numero desea hallarle la raiz cuadrada: "))
    total=x**(1/2)
    print(f"la raiz cuadrada de {x} es {total}")
    input("")
    clear_cls()
resp=""
while(resp!="7"):
    print(" MENU ")
    print("1. sumar 2 numeros ")
    print("2. restar 2 numeros ")
    print("3. multiplicar2 numeros ")
    print("4. dividir 2 numeros ")
    print("5. saludos")
    print("6. raiz cuadrada ")
    print("7. salir ")
    resp=input("\n\t\a") 
    clear_cls() 
    if (resp!="7" and resp!="6" and resp!="5" ):
        num_1=int(input("numero 1: "))
        num_2=int(input("numero 2: "))
    if (resp =="1"):
        total=num_1+num_2     
    elif (resp =="2"):
        total=num_1-num_2   
    elif (resp =="3"):
        total=num_1*num_2
    elif(resp =="4"):
        total=num_1/num_2
    elif(resp=="5"): 
        saludar()
    elif(resp=="6"):
        r_cuadrada()    
if (resp!="7"and resp!="6" and resp!="5"):
        print(f"El resultado es {total}") 