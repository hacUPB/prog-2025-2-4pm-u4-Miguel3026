import random

lista = []
lista.append(56 )
print(lista)
numero = int(input("Ingrese un número: "))
lista.append(numero)
print(lista)
#Ingresar 10 numeros aleatorios a la lista
for i in range(10):
    aleat = random.randint(0,100)
    lista.append(aleat)

print(lista)