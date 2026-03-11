x = 1 #variable llamada "x" de tipo entero, con valor 1
print(x)

balance_cuenta = 100000.00 #variable de tipo flotante
nombre_cliente = 'Jhon Doe' #variable de tipo caracter
print(x,balance_cuenta,nombre_cliente)

x = 2 #reasignamos un valor a la variable x
print(x)

#LAB
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")

total_apples = john + mary + adam
print(total_apples)


#operadores abreviados
# x+=1    ->   se le suma el valor de la derecha a la variable
# var/=2   ->   se divide la variable y se guarda el resultado en la misma
# rem %=10   ->  se le aplica modulo 10 y se guarda el resultado en rem
# x **=2    -> se eleva x a la 2 y se guarda en x


#LAB 2
km = 12.25
mi = 7.38
mi_to_km = mi * 1.61
km_to_mi = km/1.61

print(mi, "millas son", round(mi_to_km,2),"km")
print(km, "kilometros son", round(km_to_mi,2),"mi")


#LAB 3
x1 = 0
x2 = 1
x3 = -1

y1 = 3*x1**3-2*x1**2+3*x1-1
y2 = 3*x2**3-2*x2**2+3*x2-1
y3 = 3*x3**3-2*x3**2+3*x3-1

print("y1 = ",y1)
print("y2 = ",y2)
print("y3 = ",y3)

