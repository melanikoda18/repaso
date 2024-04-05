sub=0
niño=float(input("cual es el precio para niños: "))
A=float(input("cual es el precio para adultos: "))
C=int(input("cuantos niño hay: "))
T=int(input("cuantos adultos hay: "))
sub=niño*C+A*T
print(f"el sub es: ${sub:.2f}")
tasa=float(input("cual es tasa de impuestos: "))
I=tasa*sub/100
print(f"la tasa de impuestos es: ${I:.2f}")
total=I+sub
print(f"El total es: ${total:.2f}")
p=float(input("cual es el monto del pago: "))
cambio=p-total
print(f"su cambio es: ${cambio:.2f}")