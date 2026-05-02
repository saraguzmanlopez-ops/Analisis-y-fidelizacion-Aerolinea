


 Características principales -> Customer Loyalty History.csv :
 
        Formato CSV

        Consta de 16737 filas , 15 columnas

        Duplicados: No me da duplicados puesto que tiene la columna Loyalty Number que es el indice o identificador unico (PK),   
                 misma columna que en el segundo documento.

        Nulos : las columnas 'Cancellation Year','Cancellation Month' dan tan solo  filas por lo que hay que observar si son      
                 nulos o categórica o falsa categórica.
                 la columna ' Salary' sólo tiene 12499 filas lo que me indica posibles nulos 

        Tipo son String, Float e Int
                Float:
                     Salary, normalmente es Float para hacer calculos matematicos
                     CLV: valor estimado de client y empresa por lo que se usa para calculos matematicos
                     'Cancellation Year','Cancellation Month', investigar si estas dos columnas no son completamente 
                INT :  
                    'Enrollment Year', 'Enrollment Month'
                
                STRING: Country,Province, City, Postal Code,Gender,Education , Marital Status ,Loyalty Card ,Enrollment Type

Características por columnas :

    COUNTRY  -> País de residencia del cliente
    
          columna candidata a ser eliminada, ya que sólo tiene un valor Canada, por lo tanto no es relevante
          16737  filas por lo tanto sin nulos 
          un solo valor 'Canada', por lo tanto no aporta informacion relevante y es candidata a ser eliminada

    PROVINCE -> Provincia o estado de residencia del cliente
    
          16737  filas por lo tanto sin nulos 
          tipo String
          11 provincicias diferentes introducidas , canad tiene 10 provincias y 3 territorios, YUkon lo han metido como       
          provincia y no como territorio
          Bien escrito los nombres mayusculas y sin objetos raros

               Ontario: 32.29%
               British Columbia: 26.34%
               Quebec: 19.72%
               Alberta: 5.79%
               Manitoba: 3.93%
               New Brunswick: 3.8%
               Nova Scotia: 3.09%
               Saskatchewan: 2.44%
               Newfoundland: 1.54%
               Yukon: 0.66%
               Prince Edward Island: 0.39%


    City -> Ciudad de residencia del cliente.

          16737  filas por lo tanto sin nulos 
          tipo String
          29 ciudades diferententes que se han introducido
          bien escrito los nombres mayusculas y sin objetos raros


    Postal Code -> Código postal del cliente.

          tipo ship, por lo que se valora que tenga que separar los datos o fusionarlos
          Sin nulos
          tipo string 


    Gender ->  Género del cliente.

          sin nulos porque hay 16737 filas
          tipo string
          Cateórica ,dos categorias, Male y Fameles
               49.75% de los clientes son hombres
               50.25% de las clientas son mujeres     


     Education -> Nivel educativo alcanzado por el cliente

          sin nulos porque hay 16737 filas
          tipo string
          Categoricas con 5 categorias (Bachelor,College,High School or Below,Doctor,Master)
               Bachelor: 62.59%
               College: 25.32%
               High School or Below: 4.67%
               Doctor: 4.39%
               Master: 3.04%

     Salary ->Ingreso anual estimado del cliente

          25,32 % de valores nulos
          0,12 % de valores negativos, en esta columna es erroneo que se encuentre valores negativos 


     Marital Status ->  Estado civil del cliente 

          Tipo String
          Categorica con 3 categorias ('Married', 'Divorced', 'Single')
               Casados: 58.16%
               Solteros: 26.79% 
               Divorciados: 15.04%


     Loyalty Card -> tipo de tarjeta de lealtad que posee el cliente

          Categorica con 3 categorias ('Star', 'Aurora', 'Nova')
               Star: 45.63%%
               Nova: 33.88%
               Aurora: 20.49


     CLV -> Valor total estimado que el cliente aporta a la empresa durante toda la relación que mantiene con ella.

          Tipo Float, lo esperado por que es un valor
          la media es : 7988.9
          sin nulos

     Enrollment Type-> Tipo de inscripción del cliente en el programa de lealtad 

          Tipo string 
          No nulos
          Categorica 2 categorias (Standar,2018 Promotion)
               Standard : 94.2 %
               2018 Promotion : 5.8 %


     Enrollment Type-> Año en que el cliente se inscribió en el programa de lealtad.

          Tipo int que para años esta perfercto
          van en un intervalo de años de 2012 a 2017
               2012 : 10.07 %
               2013 : 14.32 %
               2014 : 14.16 %
               2015 : 13.93 %
               2016 : 14.67 %
               2017 : 14.86 %
l

     Enrollment Month -> Mes en que el cliente se inscribió en el programa de lealtad.
          Tipo int, 
          mes por número
          no nulos 

     Cancellation Year -> Año en que el cliente canceló su membresía en el programa de lealtad, si aplica.
          87.65 % de nulos
          quiere decir que el cliente no se ha dado de baja , es decir aun esta dado de alta
          tipo float

          
     Cancellation Month -> Mes en que el cliente canceló su membresía en el programa de lealtad, si
          87.65 % de nulos
          quiere decir que el cliente no se ha dado de baja , es decir aun esta dado de alta
          tipo float
          columna exactamente igual que cancellation Year, una dice el mes y otro año , valorar fusionar
                                        
Columnas Categoricas:
          Loyalty Card
           Marital Status
            Education
            Gender

Columnas que se deben valorar eliminar:
     COUNTRY ,ya que sólo tiene un valor Canada, por lo tanto no es relevante y puede ser eliminada.

Columnas a estudias los nulos 
     Saraly , con un 25,32%  de valores nulos  y un 0,12% de valores negativos


Columnas a fusionar : Cancellation Year , Cancellation Month 
                                        





Características principales -> Customer Loyalty Activit.csv :
        Formato CSV

        Consta de 405624 Filas , 9 columnas

        Nulos : No hay nulos 

        Tipo son String, Float e Int
                Float:
                    Points Accumulated  
                INT :  
                    Year, Month, Flights Booked, Flights with Companions,Total Flights, Distance,Points Redeemed,Dollar Cost Points Redeemed

       Duplicados 56.38 %

Exploracion por columnas :

     Year-> Indica el año en el cual se registraron las actividades de vuelo para el cliente.
          Solo 2 valores 
                    2017: 50.0%
                    2018: 50.0%
          tipo int
          sin nulos
     
     Month -> Representa el mes del año (de 1 a 12) en el cual ocurrieron las actividades de vuelo.
          Tipo int 
          sin nulos
          Se puede fusionar con la columna year

     Flights Booked -> Número total de vuelos reservados por el cliente en ese mes específico.
          Int 
          no hay nulos
          
     Flights with Companions ->Número de vuelos reservados en los cuales el cliente viajó con acompañantes
          Int
          No hay nulos
          Maximo es 11
          Minimo es 0
          Media es 1.03
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna
     
     Total Flights ->El número total de vuelos que el cliente ha realizado, que puede incluir vuelos reservados en meses     anteriores.
          Int 
          No nulos
          media es de 5.15 vuelos totales
          Maximo es de 32
          Minimi es de 0
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna

     Distance-> La distancia total (presumiblemente en millas o kilómetros) que el cliente ha volado durante el mes.
          Int 
          No nulos
          media es de 1208.88 millas o km , no me dicen si es millas o km
          Maximo es de 6293
          Minimi es de 0
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna



     Points Accumulated ->Puntos acumulados por el cliente en el programa de lealtad durante el mes, con base en la distancia volada u otros factores.
          Float
          No nulos
          media es de 676.5  puntos
          Maximo es de 123.69 puntos
          Minimi es de 0
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna

     Points Redeemed ->Puntos que el cliente ha redimido en el mes, posiblemente para obtener beneficios como vuelos gratis, mejoras, etc.
          Int 
          no nulos 
        
          media es de 30.7   puntos
          Maximo es de 876 puntos
          Minimi es de 0
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna

     Dollar Cost Points Redeemed -> El valor en dólares de los puntos que el cliente ha redimido durante el mes.
          Int 
          no nulos 
        
          media es de 2.8  Dolar en puntos
          Maximo es de 71  Dolar en puntos
          Minimi es de 0
          * estudiar si ese 0 puede ser eliminado ya que no tiene vuelos o es que esta anidado a otra columna


columnas posible fusion Year, Month
Columnas estudiar que significa el 0 :Flights with Companions,Total Flights , Distance,  Points Accumulated,  Points Redeemed