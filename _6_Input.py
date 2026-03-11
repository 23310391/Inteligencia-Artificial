'''no podemos hacer operaciones con la informacion que 
nos de el usuario, de momento, ya que estamos guardando strings'''

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#aqui ya estamos solicitando un numero entero
anything = int(input("Ingresa un numero: "))
something = anything **2
print(anything, "a la potencia de 2 es", something)

#Lo mismo pero con un flotante
anything = float(input("Ingresa un numero: "))
something = anything **2
print(anything, "a la potencia de 2 es", something)

#concatenacion de cadenas
nombre = input("Nombre: ")
apellido = input("Apellido: ")
nc = nombre +" "+ apellido
print("Hola ",nc)

#Replicacion (mostrar varias veces un caracter)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Conversiones
x = 12
y = str(x)
print(y)

#LAB
a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("\n¡Eso es todo, amigos!")

#LAB 2
x = float(input("Ingrese un numero: "))
y = 1/(x+1/(x+1/(x+1/x)))
print(y)

#LAB 3
hora = int(input("Hora de inicio: "))
minut = int(input("Minuto de inicio: "))
duracion = int(input("Duracion del evento (en minutos): "))

mins = minut + duracion
if mins >= 60:
    exc = mins - 60
    hora+=1

print(hora,":",exc)

