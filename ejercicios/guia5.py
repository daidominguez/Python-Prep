## Iteradores e iterables

#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
i=-15
lista=[]
while (i <= -1):
    lista.append(i)
    i+=1
print(lista)

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
i=0
while (i<len(lista)):
    if ((lista[i]) % 2 == 0):
        print(lista[i])
    i+=1


#3) Resolver el punto anterior sin utilizar un ciclo while
for i in lista:
    if (i % 2 == 0):
        print(i)

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
for i in lista[:3]:
    print(i)

#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for i,j in enumerate(lista):
    print(i, j)

#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: 
lista = [1,2,5,7,8,10,13,14,15,17,20]
for i in range (1,21):
    if (not(i in lista)):
        lista.insert(i-1,i)
print(lista)

#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n<sub>0</sub> = 0<br>
#n<sub>1</sub> = 1<br>
#n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
#Crear una lista con los primeros treinta números de la sucesión.<br>

lista=[0,1]
i=2
while (i < 30):
    lista.append(lista[i-1] + lista[i-2])
    i+=1
print(lista)

#8) Realizar la suma de todos elementos de la lista del punto anterior
suma=sum(lista)
print(suma)

#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. 
# El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos<br>
#n<sub>i-1</sub> / n<sub>i</sub><br>
#n<sub>i-2</sub> / n<sub>i-1</sub><br>
#n<sub>i-3</sub> / n<sub>i-2</sub><br>
#n<sub>i-4</sub> / n<sub>i-3</sub><br>
#n<sub>i-5</sub> / n<sub>i-4</sub><br>
primeros = 15
n = primeros - 5
while(n < primeros):
    print(lista[n]/lista[n-1])
    n += 1

#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i,j in enumerate(cadena):
    if (j == 'n' ):
        print(i)


#11) Crear un diccionario e imprimir sus claves utilizando un iterador
diccionario={'ciudades':['caracas','buenos aires','bogota','berlin','paris'], 'pais':['venezuela','argentina','colombia','argentina','alemania','francia','venezuela','ecuador','francia']}
for i in diccionario:
    print(i)

#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
lista=list(cadena)
marca=iter(lista)
for i in range (0,len(lista)):
    print(next(marca))

#13) Crear dos listas y unirlas en una tupla utilizando la función zip
lista1=[1,2,5,7,8]
lista2=['uno','dos','cinco','siete','ocho']
tupla=zip(lista1, lista2)
print(list(tupla))

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
listnew=[]
for i in lis:
     if (i % 7 == 0):
        listnew.append(i)
print(listnew)

#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, 
# teniendo en cuenta que un elemento de la lista podría ser otra lista
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cant=0
for i in range (0,len(lis)):
    if (type(lis[i]) == list):
        cant= len(lis[i]) + cant
    else:
        cant+=1
print(cant)

#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i in range (0,len(lis)):
    if (type(lis[i]) != list):
        lis[i]=list(lis[i])
    print(type(lis[i]))