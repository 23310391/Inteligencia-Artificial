''' BUCLES
while -> mientras se cumpla una condicion, se ejecuta
while True -> bucle infinito
'''

#LAB
secret_number = 777

print("""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+ """)

num = int(input("Ingresa el numero secreto: "))
while num != secret_number:
    print("MUAJAJAJA, estas atrapado en mi bucle")
    num = int(input("Intentalo de nuevo: "))
print("Escapaste esta vez...")


#lab inventado por mi para que vea que si soy proactivo
#este codigo es 2x1, muestro el ciclo for y el break
a,b = 0,1
lista_fibonacci = [0]
n_max = int(input("Ingrese el numeor maximo de la sucesion de fibonacci al que quiere llegar: "))

for x in range(n_max): #se ejecuta desde 0 hasta el numero que le pasemos
    if b > n_max: 
        break
    else:
        lista_fibonacci.append(b)
        a,b = b,a+b
print(lista_fibonacci)

