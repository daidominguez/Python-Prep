# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var1=20
print(var1)

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a=20
b=21.8
if (type(a) == type(b)):
    print('las variables son del mismo tipo de dato')
else:
    print('las variables son de distintos tipos de datos')

    # 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
    for i in range(6):
        print(i , ' elevado a la potencia 3 da como resultado: ', (i**3))

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
n=7
for i in range (0,n):
    pass
print(i)

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
var1=6
if (var1 > 0) and (type(var1) == int):
    n=var1
    factorial=1
    while (n>0):
        factorial=factorial*n
        n-=1
    print('Factorial de ',var1,' es ',factorial)
else: 
    print('ingrese un numero entero positivo')

# 8) Crear un ciclo while dentro de un ciclo for
n=5
j=1
for i in range (1,n+1):
    while (j <= n):
       print('ciclo while',j,' del ciclo for ',i)
       j+=1
    j=1

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n=99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')