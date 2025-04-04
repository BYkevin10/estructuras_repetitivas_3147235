##Ciclo for
# Especial para recorrer estructuras de datos 
# Todo lo que esta [ ] se denomina lista

# Funcion range(python)
# Crea una lista de numeros en el rango definido 
# por el usuario 

numeros = int(input("Ingrese un numero: "))

for i in range(1, 11):
    resultado = numeros * i
    print(numeros, "X", i,  "=", resultado)
    