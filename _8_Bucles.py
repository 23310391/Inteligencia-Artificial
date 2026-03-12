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

#LAB 3
palabra = input("Ingrese una palabra: ")
palabra = palabra.upper()
#hacemos un barrido por cada letra de la palabra
#si la letra es una vocal, no la imprimimos
for letra in palabra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    print(letra)

#LAB 4
word = ""
palabra = input("Ingrese una palabra: ")
palabra = palabra.upper()

#vamos a hacer un barrido por cada letra de la palabra
#si la letra es una vocal, no la agregamos a la cadena
for letra in palabra: 
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        word = word + letra
print(word)


#LAB 5 creo
bloques = int(input("Ingrese la cantidad de bloques que contiene la piramide: "))
i = 1
altura = 0
while bloques >= i:
    bloques -= i
    altura +=1
    i += 1
print(altura)



#LAB 6
x = int(input("Ingrese un numero positivo mayor a 0: "))
pasos = 0
while x != 1:
    if x % 2 == 0:
        x /= 2
    else:
        x = (x*3)+1
    print(x)
    pasos += 1
print("pasos: ",pasos)