'''
a este codigo si le eché ganitas, es de la 4.3 a la 4.5
'''

#funcion con 2 parametros
def nombre2 (name, gender):
    gender = gender.lower() #aun que eswcribamos con mayusculas, lo va a detectar bien
    if (gender == "mujer"):
        adjetivo = "reina"
    elif (gender == "hombre"):
        adjetivo = "Perro"
    else:
        adjetivo = "amor"

    print(f"Hola mi {adjetivo}, cómo estás {name}?")

#ejecutamos la funcion con 2 parametros
nombre2("Santy", "HOMBRE")

#-------------------------------------------------------
#definimos un parametro por default, es opcional ponerlo o no
def frase2(nombre, apellido, adjetivo = "tonoto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

res = frase2("pedro", "ortiz")
print(res)

res2 = frase2("pablo", "vegas", "inteligente") #aun que un parametro estè definido, lo podemos modificar
print(res2)

#------------------------------------------------
def sum_args(*numeros): #con el asterisco le decimos que va a ser una lista
    return sum(numeros)   

resultado = sum_args(4,5,6,7,8,9)
print(resultado)

#-----------------------------------------------------
"""crear una funcion que muestre la serie de fibonacci entre 0 
y el numero dado"""

def fibonacci(num):
    a,b = 0,1
    lista_fibonacci = [0]
    for x in range(num): #se ejecuta desde 0 hasta el numero que le pasemos
        if b > num: return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b,a+b
    return lista_fibonacci

resultado = fibonacci(39)
print(resultado)

        