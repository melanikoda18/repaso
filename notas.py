apell=input("apellidos:  ")
nom=input("nombre: ")
nota_1=int(input("nota 1: "))
nota_2=int(input("nota 2: "))
nota_3=int(input("nota 3: "))
total=nota_1+nota_2+nota_3
prom=total/3
print(f"{apell.upper()}, {nom.title()} NOTA difinitiva: {prom}")