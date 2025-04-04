#Ejercicio 1
# Imprimir la tabla de multiplicar del numero que un usuario 
# ingrese por teclado utilizando un ciclo while 
numero = int(input("Ingrese un numero: "))

i=10
while i >=10:
    resultado = numero * i
    print(numero, "X" , i, "=", resultado)
    ##intruccion de incremento
    i = i - 1
    