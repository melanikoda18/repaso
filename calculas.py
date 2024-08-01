def par_impar(x):
    return x%2==0
def es_primo(a):
    contador=0
    for i in range(1,a+1,1):
        if(a/i%1==0):
            contador+=1
        if(contador==2 and i !=a):  #if(contador>2):esta es otra opcion de hacer el programa 
            return False
    #print(f"contador vale: {contador}") esta es es otra forma de hacerlo pero mas largo y mas lento y se borra la linea 8y9 para usarla 
    return contador ==2 
def tiene_raiz(a):
    return (a**(1/2))%1==0
resp=""
while(resp!="0"):
    print("menu")
    print("1. par/impar")
    print("2. es primo")
    print("3. tiene raiz cuadrada")
    print("0. para salir")
    resp=input("seleccione una opcion: ")
    if(resp=="1"):
        x=int(input("ingrse el numero: "))
        if (par_impar(x)):
            print(f"el numero es par")
        else:
            print(f"el numero es impar ")    
    elif(resp=="2"):
        x=int(input("ingrse el numero: "))
        if (es_primo(x)):
            print("Es un numero primo ")
        else:
            print("NO es un numero primo")
    elif(resp=="3"):
        num=int(input("ingrse el numero a evaluar: "))
        if(tiene_raiz(num)):
            print("el numero es un cuadrado perfecto ")
        else:
            print("el numero no es un cuadrado perfecto ")    