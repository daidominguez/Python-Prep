
class funciones:
    def __init__(self,lista):
        if (type(lista)!= list):
            self.lista=[]
            raise ValueError ('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')
        else:
            self.lista=lista
    
    def Verificar_primo(self):
        for i in self.lista:
            if (self.__Verificar_primo(i)):
                print('el numero',i,' es primo')
            else:
                print('el numero ',i,'NO es primo')
    
    def Conversion_grados(self,med_origen,med_dest):
        lis=['Celsius','Kelvin','Farenheit']
        lista_conversion=[]
        if (str(med_origen) not in lis):
            print('los parametros esperados son: ',lis)
            return lista_conversion
        if (str(med_dest) not in lis):
            print('los parametros esperados son: ',lis)
            return lista_conversion
        for n in self.lista:
            lista_conversion.append(round(self.__Conversion_grados(n,med_origen,med_dest),2))
        return lista_conversion

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


