''' Operadores logicos

=  -> igualacion
== -> comparacion de igualdad
!= -> desigualdad
>  -> mayor que
>= -> mayor o igual que
<  -> menor que
<= -> menor o igual que

estas retornan verdadero o falso

'''
'''jerarquia de operaciones

+- (unario)
**
* / // %
+- (binario)
< <= > >=
== !=

'''

#LAB
n = int(input("Ingrese un numero: "))
print(n>=100)

#if, if else y elif
#if - si se cumple la condicion, se ejecuta este codigo
#else - si no se cumple la condicion if, se ejecuta else
#en else no ponemos condiciones, en elif si, agregamos varias condicinoes

#LAB 2
palabra = input("hola \n")
if palabra == "ESPATIFILO":
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif palabra == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else :
    print("¡Espatifilo!, ¡No ",palabra,"!")

#LAB 3
salario = float(input("Ingrese su salario anual:"))
if salario <= 85528:
    ipi = salario * 0.18 - 556.02
else:
    ipi = (salario-85528) * .32 + 14839.02

print(ipi)

#LAB 4
year = int(input("Ingrese un año: "))

if year <=1581: #verificamos que esté dentro del calendario gregoriano
    print("Año fuera del calendario gregoriano")
elif year%4 != 0: #dividimos entre 4, si el resto es 0, es divisible
    print(year," es un año comun")
elif year%100 != 0:
    print(year," es un año bisiesto")
elif year%400 != 0:
    print(year," es un año comun")
else:
    print(year," es un año bisiesto")
