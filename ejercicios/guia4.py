# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades=['caracas','buenos aires','bogota','berlin','paris']
print(ciudades)
print(type(ciudades))

# 2) Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])

#4) Visualizar el tipo de dato de la lista
print(type(ciudades))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[2:])

#6) Visualizar los primeros 4 elementos de la lista
print(ciudades[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append('caracas')
ciudades.append('quito')
print(ciudades)

#8) Agregar otra ciudad, pero en la cuarta posición 
ciudades.insert(3,'cordoba')

#9) Concatenar otra lista a la ya creada 
ciudades.extend(['mendoza','santiago'])

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad? 
print(ciudades.index('caracas'))
#encuentra solo la primera posicion encontrada

#11) ¿Qué pasa si se busca un elemento que no existe? indica ERROR
#print(ciudades.index('mexico'))

#12) Eliminar un elemento de la lista 
ciudades.remove('santiago')

#13) ¿Qué pasa si el elemento a eliminar no existe? indica que el elemento no se encuentra en la lista
#ciudades.remove('mexico')

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
#extraer implica eliminar ese elemento de la lista y gardarlo aparte
ultimo=ciudades.pop()
print(ultimo)
print(type(ultimo))

#15) Mostrar la lista multiplicada por 4 
print(ciudades*4)

#16) Crear una tupla que contenga los números enteros del 1 al 20
num=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#17) Imprimir desde el índice 10 al 15 de la tupla
print(num[10:16])

#18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in num)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
verd='Paris' in ciudades
print(verd)
if (verd == True):
    print('la ciudad Paris ya se encuentra en la lista')
else:
    ciudades.append('Paris')
    print('se ha ahregado la ciudad Paris a la lista')

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(num.count(25))
print(ciudades.count('caracas'))

#21) Convertir la tupla en una lista
lista=list(num)
print(lista)

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
v1, v2, v3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = num
print(v1)
print(v2)
print(v3)

#23) Crear un diccionario utilizando la lista creada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario={'ciudades':ciudades, 'pais':['venezuela','argentina','colombia','argentina','alemania','francia','venezuela','ecuador','francia']}

#24) Imprimir las claves del diccionario
print(diccionario.keys())

#25) Imprimir las ciudades a través de su clave
print(diccionario['ciudades'])