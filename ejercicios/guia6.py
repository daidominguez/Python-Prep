## Funciones

#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def num_primo(num):
    primo= True
    for i in range (2,num):
        if (num % i == 0):
            primo= False
            break
    return primo

print(num_primo(10))

#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def primos_lista(lista):
    lista_primos=[]
    for i in lista:
        if (num_primo(i)):
            lista_primos.append(i)
    return lista_primos

print(primos_lista([1,3,5,8,10]))

#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
def num_rep_lista(lista):
    max=0
    rep=0
    for i in lista:
        num_rep=lista.count(i)
        if (num_rep > 1):
            max=i
            rep=num_rep
    return max,rep

lista=[1,7,8,10,9]
print(num_rep_lista(lista))

#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def num_rep_lista2(lista,men):
    max=0
    rep=0
    if (men):
        lista.sort(reverse=True)
    else:
        lista.sort()
    for i in lista:
        num_rep=lista.count(i)
        if (num_rep > 1):
            max=i
            rep=num_rep
    return max,rep

lista=[1,7,8,10,9,8,10]
print(num_rep_lista2(lista,True))

#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def Temperatura(val,med_origen,med_dest):
    if (med_origen == 'Celsius'):
        if (med_dest == 'Kelvin'):
            return val+273.15
        elif (med_dest == 'Farenheit'):
            return val*(9/5)+32
        elif (med_dest == 'Celsius'):
            return val
        else: 
            return None
    elif (med_origen == 'Kelvin'):
        if (med_dest == 'Celsius'):
            return val-273.15
        elif (med_dest == 'Farenheit'):
            return (val-273.15)*(9/5)+32
        elif (med_dest == 'Kelvin'):
            return val
        else: 
            return None
    elif (med_origen == 'Farenheit'):
        if (med_dest == 'Kelvin'):
            return (val-32)*5/9 +273.15
        elif (med_dest == 'Celsius'):
            return (val-32)*5/9
        elif (med_dest == 'Farenheit'):
            return val
        else: 
            return None
    else:
        return None

print(Temperatura(5,'Celsius','Farenheit'))

#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

lis=['Celsius','Kelvin','Farenheit']
num=20
for j in range(3):
    for i in range(3):
        print(num,' grado ',lis[j],' a ',lis[i],': ', round(Temperatura(num,lis[j],lis[i]),2))

#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(num):
    if (num>1):
        if (type(num) != int):
            return None
        else:
            num=num*factorial(num-1)
    if (num<0):
        return None
    return num

print(factorial(0))