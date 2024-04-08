aprobados=0
repro=0
prom_apro=0
suma_aprobados=0
prom_repro=0
suma_reprobados=0

for o in range (3):
    print(f"Estudiante {o+1}")
    contador=0
    sumador=0
    promedio_estudiante=0
    for i in range (3):
        sumador +=int(input(f"ingrese la nota del lapso {i+1}: "))
        contador+=1
    
    promedio_estudiante=int(round(sumador/contador,0))
    print(f"El  promedio es : {promedio_estudiante}")
    if promedio_estudiante>=10:
        aprobados+=1
        suma_aprobados+=promedio_estudiante
    else:
        repro+=1
        suma_reprobados+=promedio_estudiante
print(f"cantidad de aprobados: {aprobados} y su promedio es : {(suma_aprobados/aprobados)}")

prom_repro=suma_reprobados/repro
print(f"cantidad de reprobados: {repro} y su promedio es: {prom_repro}")