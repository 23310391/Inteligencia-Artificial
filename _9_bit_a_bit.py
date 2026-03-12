'''
& and -> arroja true cuando ambas entradas son 1
| or  -> arroja true cuando cualquiera de las entradas es 1
~ not -> niega la entrada
^ XOR -> true cuando una u otra entrada es 1, no ambas
'''

'''jerarquia de operaciones actualizada
~,+,-       (unario)
**
*,/,//,%
+,-         (bianrio)
>>, <<
<, <=, >, >=
==, !=
&
|
=, +=, -=, *=, /=, %=, ^=. |=, <<=, >>=
'''
print(True | False)   #or retorna true
print(True & False)  #and retorna false
print(not True | False) #negamos true, ahora es false or false, retorna false

x = 5 #en binario 5 = 0000 0101
print(x << 1) #nos desplazamos un bit a la izquierda
#ahora en binario sería 0000 1010 = 10

x = 5
print(x>>1) # 0000 0010 = 2

