lista1 = [1,2,3,4,5,6,7]
print(lista1)

lista2 = lista1 #copiamos toda la lista 1
print(lista2)

lista2[0] = 0 #cambiamos el primer elemento por "0"
lista2[-1] = 9 #cambiamos el ultimo elemento por "9"
print(lista2)

lista1 = [1,2,3,4,5,6,7]

#slicing            lista[inicio:paro]
lista2 = lista1[2:4] #copiamos los elementos en las posiciones 2 y 3
print(lista2)

#negative slicing
#copiamos los elementos desde la posicion 1 hasta la penultima(-1 significa ultimo elemento, pero al ser el paro, no lo toma en cuenta)
lista2 = lista1[1:-1] 
print(lista2)

lista2 = lista1[-1:1] #no se copia ningun elemento
print(lista2)

lista2 = lista1[:4] #copiamos desde el inicio, para en la posicion 4, copia hasta la posicion 3
print(lista2)

lista2 = lista1[3:] #copiamos desde la posicion 3 hasta que acabe la lista
print(lista2)

lista2 = lista1[:]
print(lista2)


del lista2[:3] #eliminamos los primeros 3 elementos de la lista
print(lista2)

del lista2[:] #borramos toda la lista
print(lista2)

#in y not in (regresan true o false)
print(5 in lista1)
print(9 in lista1)
print(8 not in lista1)


#------------------------LAB-------------------------
lista = [1,2,4,4,5,7,8,1,3,9,9,0,2,4,6,6,2,3,6,5]
lista_no_repeat = []

for x in range(len(lista)):
    if lista[x] not in lista_no_repeat:
        lista_no_repeat.append(lista[x])

print(lista_no_repeat)
