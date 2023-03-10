# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

a = 10
if (a < 0):
    print('La variable es menor a cero')
elif (a > 0): 
    print('La varaible es mayor a cero')
else:
    print('La variable es igual a cero')


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

a = 2
b = 'hola'
if (type(a) == type(b)):
    print('Las variables son del mismo tipo de dato')
else:
    print('Las variables son de tipos de dato diferentes')


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for i in range(1, 21):
    if i % 2 == 0:
        print('El número ', str(i), ' es par')
    else:
        print('El número ', str(i), ' es impar')


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(6):
    print('Valor:', str(i), ' Elevado a la 3ra potencia:', str(i**3))


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

n = 12
for i in range(0, n):
    pass
print(i)


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

n = 5
factorial=n
if (type(n) == int) and (n > 0):
    for i in range (1,n):
        factorial=factorial*i 
    print('factorial de',n,' es igual a ',factorial)
else:
    print('La variable no es un entero positivo')
    

# 7) Crear un ciclo for dentro de un ciclo while

n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))


# 8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n=1
prox=1
primo= True
while (prox == 1):
    for i in range (2,n):
        if (n % i == 0):
            primo= False
            break
    if (primo):
        print(i,' es numero primo')
        print('desea encontrar el siguiente numero primo? caso verdadero ingrese 1')
        if (input != '1'):
            print('fin del proceso')
    else:
        Primo= True
    n+=1

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while(n <= 300):
    if (n % 3 == 0) and (type(n / 6) == int):
        print(n, ' es divisible por 3 y ademas multiplo de 6')
        break
    n += 1

