## Clases y Programación Orientada a Objetos

#1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

class Vehiculo:
    def __init__(self,color,tipo,motor):
        self.color=color
        self.tipo=tipo
        self.motor=motor


#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>
class Vehiculo:
    def __init__(self,color,tipo,motor):
        self.color = color
        self.tipo = tipo
        self.motor = motor
        self.velocidad = 0
        self.direccion = 0
    
    def acelerar(self,vel):
        self.velocidad+=vel

    def frenar(self,vel):
        self.velocidad-=vel

    def doblar(self,dir):
        self.direccion+=dir


#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
vehiculo1=Vehiculo('amarillo','moto',5)
vehiculo2=Vehiculo('rojo','auto',7.8)
vehiculo3=Vehiculo('azul','camion',9)

vehiculo1.acelerar(40)
vehiculo2.frenar(80)
vehiculo3.doblar(45)
vehiculo1.doblar(90)
vehiculo2.acelerar(78)
vehiculo3.frenar(90)

#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. 
# Y otro método que muestre color, tipo y cilindrada
class Vehiculo:
    def __init__(self,color,tipo,motor):
        self.color=color
        self.tipo=tipo
        self.motor=motor
        self.velocidad=0
        self.direccion=0
    
    def acelerar(self,vel):
        self.velocidad+=vel

    def frenar(self,vel):
        self.velocidad-=vel

    def doblar(self,dir):
        self.direccion+=dir
    
    def estado(self):
        print('Velocidad: ',self.velocidad,' -Direccion: ',self.direccion)
    
    def caracteristicas(self):
        print('Color: ',self.color,' -Tipo: ',self.tipo,' -Cilindrada: ', self.motor)

vehiculo1=Vehiculo('amarillo','moto',5)
vehiculo1.acelerar(40)
vehiculo1.doblar(90)
vehiculo1.caracteristicas()
vehiculo1.estado()

#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
#Verificar Primo
#Valor modal
#Conversión grados
#Factorial

#no hacemos nada, solo encapsular las funciones
class funciones:
    def __init__(self)-> None:
        pass
    
    def Verificar_primo(self,num):
        primo= True
        for i in range (2,num):
            if (num % i == 0):
                primo=False
                break
        return primo

    def valor_Modal(self,lista,men):
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
    
    def Conversion_grados(self,val,med_origen,med_dest):
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

    def factorial(self,num):
        if (num>1):
            if (type(num) != int):
                return None
            else:
                num=num*self.factorial(num-1)
        if (num<0):
            return None
        return num

#6) Probar las funciones incorporadas en la clase del punto 5

f=funciones()

print(f.Verificar_primo(5))

lista=[1,2,5,5,7,8,9,9,10]
moda,rep=f.valor_Modal(lista,True)
print(moda,rep)

print(f.Conversion_grados(5,'Celsius','Kelvin'))

print(f.factorial(4))

#7) Es necesario que la clase creada en el punto 5 contenga una lista, 
# sobre la cual se apliquen las funciones incorporadas

class funciones:
    def __init__(self,lista):
        self.lista=lista
    
    def Verificar_primo(self):
        for i in self.lista:
            if (self.__Verificar_primo(i)):
                print('el numero',i,' es primo')
            else:
                print('el numero ',i,'NO es primo')
    
    def Conversion_grados(self):
        lis=['Celsius','Kelvin','Farenheit']

        for n in self.lista:
            for j in range(3):
                for i in range(3):
                    print(n,' grado ',lis[j],' a ',lis[i],': ', round(self.__Conversion_grados(n,lis[j],lis[i]),2))

    def factorial(self):
        for i in self.lista:
            print('Factorial de ',i,' es: ', self.__factorial(i))

    
    def __Verificar_primo(self,num):
        primo= True
        for i in range (2,num):
            if (num % i == 0):
                primo=False
                break
        return primo

    def valor_Modal(self,men):
        max=0
        rep=0
        if (men):
            self.lista.sort(reverse=True)
        else:
            self.lista.sort()
        for i in self.lista:
            num_rep=self.lista.count(i)
            if (num_rep > 1):
                max=i
                rep=num_rep
        return max,rep
    
    def __Conversion_grados(self,val,med_origen,med_dest):
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

    def __factorial(self,num):
        if (num>1):
            if (type(num) != int):
                return None
            else:
                num=num*self.__factorial(num-1)
        if (num<0):
            return None
        return num

f = funciones([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
f.Verificar_primo()
f.factorial()
print(f.valor_Modal(True))
f.Conversion_grados()

#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. 
# Luego realizar la importación del módulo y probar alguna de sus funciones
from funciones import *

f = funciones([1,2,5,8,9,11,15,16,18,20])
f.Verificar_primo()
f.factorial()
print(f.valor_Modal(True))
f.Conversion_grados()