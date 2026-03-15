'''
Una tupla es una lista que no se puede modificar (es inmutable)
'''

tupla = (True, "Santiago", 10) 
print(tupla)
print(tupla[0])

conjunto = {True, "Santy", 10, "Santy"} #tambien llamado "set", no tienen un orden fijo
# no almacena datos duplicados, no tiene un orden, no se puede acceder a los datos por el indice
# #print(conjunto[0]) 
print(conjunto) #unicamente lo podemos mostrar completo

#el diccionario tiene keys y tiene valores
diccionario = {
    "nombre" : "Santiago",
    "Es ingeniero?" : False,
    "Estatura" : 1.85
}

print(diccionario["nombre"])
print(diccionario["Estatura"]+.02)

#mostramos las keys
claves = diccionario.keys()
print("keys: ",claves)

#eliminamos elementos del diccionario
diccionario.pop("nombre") #saca un elemento de el diccionario, la key y el valor, pueden ser varios, separados por comas
print(diccionario)

#mostramos las respuestas de las keys (items)
dicc_iterables = diccionario.items()
print(dicc_iterables)

#elimina todos los valores del diccionario
diccionario.clear() 
print(diccionario)


#agregamos elementos al diccionario
diccionario.update({"apellido":"Lomas"})
print(diccionario)
