resp=""
while(resp!="0"):
    nom=input("nombre y apellido: ")
    nota=int(input("ingrese su nota:  "))
    if (nota >=90):
        letra="A"
    elif (nota>=80):
        letra="B"
    elif (nota >=70):
        letra="C" 
    elif(nota>=60):
        letra="D"
    elif(nota<60):
        letra="F"
    if(nota%10>=7 and letra!="A" and letra!= "F"):
        signo="+"
    elif(nota%10<3 and letra !="F"):
        signo="-"
    else: signo=""
    if (nota>=70):
        print(f"aprobaste con {letra+signo}")
    else :
        print(f"reprobaste con {letra+signo}")
    resp=input("0 para salir , ENTER para continuar: ")    
        #for i in range (5):