nombre=[["3134262","adrian uribe"],["15957531", "erick scala"],["31329488","melani velasquez"] ]
res=""
while(res!="0"):
    flag = 0
    print("\n------------------------------")
    print("registro de estudiantes")
    print("1.agregar estudiantes")
    print("2.buscar estudiantes")
    print("3.eliminar estudiantes")
    print("4.guardar en un archivo")
    print("5.cargar desde un archibo")
    print("6.lista de estudiante ")
    print("0.salir")
    
    res=input("elige una opcion: ")
    print("------------------------------\n")
    if(res=="1"):
        nombre.append([input("C.I:"),input("nombre y apellido:").title()])
    elif(res=="2"):
        search=input("ingrse la C.I:")
        for estudiante in nombre:
            if(search == estudiante[0]): #coincidencia exacta (grasias a esta funcion en resultado es exacto)

                print(f"\n\t{estudiante[0]}, {estudiante[1]}")
                flag = 1 ;
        if (not flag): 
            print("\n no se encontro el estudiante")

    elif(res=="3"):
        if nombre:           
            print(f"se ha eliminadoa {nombre.pop()}")
            if nombre:
                print("fin del archivo")
    elif(res =="6"):
        print()
        for estudiante in range(len(nombre)):
            print(f"C.I: {nombre[estudiante][0]} estudiantes {nombre[estudiante][1]}")


        
            