lista=[51,15,3,9,8,2,4,99,105]
contador_de_impares = 0
for i in range (len(lista)):#el len nos da la cantidad de algo 
    if lista[i] % 2 == 1 : 
        contador_de_impares+=1
print (f"la cantidad de impares es: {contador_de_impares} ")
