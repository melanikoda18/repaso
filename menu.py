resp=""
while(resp!="5"):
    print("seleccine una opcion. ")
    print("1. sumar 2 numeros ")
    print("2. restar 2 numeros ")
    print("3. multiplicar2 numeros ")
    print("4. dividir 2 numeros ")
    print("5. salir ")
    resp=input("\n\t\a") 
    if (resp!="5"):
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
    if (resp!="5"):
        print(f"El resultado es {total}") 