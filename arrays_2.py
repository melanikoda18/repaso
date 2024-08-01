arr = [1,2,99,37,42,55,76,7,5,101]
resp = ""
while (resp != "0"):
    print(f"\n--------------------\n{arr}\n--------------------\n")
    print("1. Agregar elemento al inicio")
    print("2. Agregar elemento al final")
    print("3. Quitar último elemento")
    print("4. Quitar primer elemento")
    print("5. Ordenar Array")
    print("0. Salir del programa")
    resp = input("\n\tSeleccione una opción ")
    if (resp == "1"):
        num = float(input("escriba un numero:  "))
        arr.insert (0 ,num)
    elif (resp == "2"):
        num=float(input("escriba un numero: "))
        arr.append(num)#esto  sirve para agregar un elemento al final
    elif (resp == "3"):
        if arr:
            arr.pop()
    elif (resp == "4"):
        if arr:
            arr.pop(0)
    elif (resp == "5"):
        arr.sort()
print("\nPrograma Terminado\n\n")