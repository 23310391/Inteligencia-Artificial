#LAB
numeros = [1, 2, 3, 4, 5]
#modificamos la posicion 3 (el centro de la lista)
numeros[2] = int(input("Modifica el valor central de la lista: "))
print(numeros)
del numeros[-1] #eliminamos el valor del final de la lista
print(numeros)
print(len(numeros))#mostramos cuantas posiciones tiene la lista


#LAB 2
beatles = []

beatles.append("John Lennon")
beatles.append("Paul Mccartney")
beatles.append("George Harrison")
print(beatles)
beatles.append(input("Agrega a Stu a la lista: "))
beatles.append(input("Agrega a Pete a la lista: "))
print(beatles)
for i in range(2):
    del beatles[-1]
beatles.insert(0, "Ringo Star")
print(beatles)
