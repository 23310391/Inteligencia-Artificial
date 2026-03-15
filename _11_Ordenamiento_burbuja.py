'''
Algoritmo de ordenamiento burbuja (Bubble Sort)
Es de los más básicos, pero de los más lentos tambien
'''

lista = []
cambio = True
num = int(input("Cuantos numeros tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print(lista)

while cambio:
    #variable "cambio", mientras se sigan haciendo cambios, el bucle sigue
    cambio = False 
    for x in range(len(lista)-1):
        if lista[x] > lista[x + 1]: #comparamos el elemento actual con el siguiente
            cambio = True
            lista[x], lista[x + 1] = lista[x + 1], lista[x] #intercambiamos los numeros de la posicion actual con la anterior

print(lista)


#aqui es donde me pregunto, para que hice lo de arriba?
lista2 = [100,24,3,0.5,84,-4] 
print(lista2)
lista2.sort() #grande python, ahorrando 20 lineas de codigo (sort significa acomodar)
print (lista2)
