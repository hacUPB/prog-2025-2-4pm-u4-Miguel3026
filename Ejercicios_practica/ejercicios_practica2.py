
# Ejercicio: Comparar dos numeros 
a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))
if a > b:
        print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{b} es mayor que {a}")
else:
    print("los numeros son iguales")
        
    
       
# Ejercicio: Calcular factorial de un número
    n = int(input("ingrese un numero entero positivo:"))
    factorial = 1
    for i in range (1, n + 1):
        factorial = factorial * i
        print(f" el factorial de {n} es {factorial}")
    
  
  
 
# Ejercicio: Sumar dos numeros
    num1 = float(input("ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    suma = num1 + num2
    print(f"la suma de {num1} y {num2} es {suma}")
    
    
    
# Ejercicio: Costo envio 
compra = float(input("ingrese el monto total de la compra:"))
if compra > 100000:
    print("el envio es gratis")
elif compra < 100000:
    print("el envio tiene un costo de 9000$")
    valor_total = compra + 9000
    print(f"el valor total de la compra es de {valor_total}$")
    
    
# Ejercicio: Numero par o impar
n = int(input("ingrese un numero entero:"))
if n % 2 == 0:
    print(f"el numero {n} es par")
else:
    print(f"el numero {n} es impar")
    
