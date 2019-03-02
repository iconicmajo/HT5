#Maria Jose Castro Lemus 181202
#Andres Berthet 171504
#Estructura de datos
#Lab 5
#Programa de simulacion


#El programa esta basado en el ejemplo Gasolinera que esta en CANVAS
#Calculo estadistico obtenido de: https://www.geeksforgeeks.org
#Partes del Codigo extraido del libro http://docs.python.org.ar/tutorial/pdfs/TutorialPython2.pdf
import simpy
import random
#import statistics

  

cpu = []
#ram = []

def simular(nombre,env,wait_time,space,ram):
    global totalPro  #  Tiempo de proceso
    global times

    pro= 3
    #crea el proceso
    yield env.timeout(wait_time)

    #Tiempo que le toma al proceso llegar
    posLlegada = env.now

    
    rameme = random.randint(1,10)#memoria a soliciatar


    tiempoPro = random.randint(1, 10)#Cantidad de instrucciones
    

    print ('%s empieza en %f tiene %d instrucciones' % (nombre,posLlegada,tiempoPro))

    #Definimos ir ala cola
    with ram.get(tiempoPro) as turno:
        print(nombre, "tiemp: ", env.now)
        #ya esperando turno en ram
        yield turno
        #Si tiene mas de dos instrucciones
        while tiempoPro>2:
            with space.request() as simular:
                yield simular
                tiempoPro = tiempoPro-pro
                yield env.timeout(1)
                print(nombre,  "tiempo: ", env.now)
            io = random.randint(1,2)
            if(io == 2):
                yield env.timeout(1)
         #Si se tienen menos de tres       
        if tiempoPro<3:
            yield env.timeout(1)
        ram.put(rameme)

    #Espacio a usar del cpu
    with space.request() as turno:
        yield turno #turno en proesar
        yield env.timeout(tiempoPro)
        print ('%s proceso termina a las %f' % (nombre, env.now))


    tiempoTotal = env.now - posLlegada
    times = list()
    times.append(tiempoTotal)
    print ('%s se tardo %f' % (nombre, tiempoTotal))
    totalPro = totalPro + tiempoTotal
0

# ----------------------

env = simpy.Environment() #ambiente de simulación
space = simpy.Resource(env,capacity = 1)#Cantidad de CPU
ram = simpy.Container(env,capacity= 100, init=100) #Cantidad de RAM
random.seed(10) # fijar el inicio de random

totalPro = 0
procesos=25
for i in range(procesos): #numero de procesos 
    env.process(simular('proceso %d'%i,env,random.expovariate(1.0/10),space,ram))

env.run()  #correr la simulación en tiempo infinito
promedio = totalPro/procesos
print ("tiempo promedio por proceso es: ", promedio)#Divide el tiempo en el num de process

#*****************************************************
#trate de sacar la desviacion con estadisticas pero no me salio :( que sad
#Esto fue lo que intente
#desvest = statistics.stdev(times, xbar=None)
#posLlegada= list() Creo que esto esta demas pero no lo use
#m = statistics.mean(times)
#print("Standard Deviation of Sample set is % s" 
#         %(statistics.stdev(times, xbar =m)))
#print ("desviacion estandar es:  % s" %( statistics.stdev(times, xbar=m)))#Desviacion por proceso
#intento 2:
#importe
#import statistics
#from statistics import stdev 
  
# importing frations as parameter values 
#from fractions import Fraction as fr
#print("The Standard Deviation of Sample4 is % s" 
  #                            %(stdev(times)))
#**********************************************************************
  #de Geeks for geeks
for i in times:
   desvest = ((i-promedio)*(i-promedio))/procesos
print ("desviacion estandar es: ", desvest)#Desviacion por proceso

