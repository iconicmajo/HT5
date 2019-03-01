#Maria Jose Castro Lemus 181202
#Andres Berthet 171504
#Estructura de datos
#Lab 5
#Programa de simulacion

import simpy
import random

cpu = []
#ram = []

def simular(nombre,env,wait_time,space):
    global totalPro  #  Tiempo de proceso
    global times
    status = "entrando"
    pro=1
    #crea el proceso
    yield env.timeout(wait_time)

    #Tiempo que le toma al proceso llegar
    posLlegada = env.now

    
    rameme = random.randint(1,10)#memoria a soliciatar


    tiempoPro = random.randint(1, 10)#Cantidad de instrucciones
    

    print ('%s empieza en %f tiene %d instrucciones' % (nombre,posLlegada,tiempoPro))

    #Definimos ir ala cola
    with ram.get(tiempoPro) as turno:
        status = "Listo"
        print(nombre,"en: ", status, "tiemp: ", env.now)
        #ya esperando turno en ram
        yield turno
        #Si tiene mas de dos instrucciones
        while tiempoPro>2:
            with space.request() as simular:
                yield simular
                status = "procesando"
                tiempoPro = tiempoPro-pro
                yield env.timeout(1)
                print(nombre, "estado  ", status, "tiempo: ", env.now)
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
    print ('%s se tardo %f' % (nombre, tiempoTotal))
    totalPro = totalPro + tiempoTotal
0

# ----------------------

env = simpy.Environment() #ambiente de simulación
space = simpy.Resource(env,capacity = 1)#Cantidad de CPU
ram = simpy.Container(env,capacity= 100, init=100) #Cantidad de RAM
random.seed(10) # fijar el inicio de random

totalPro = 0
for i in range(15):
    env.process(simular('proceso %d'%i,env,random.expovariate(1.0/10),space))

env.run()  #correr la simulación en tiempo infinito
promedio = totalPro/25.0
print ("tiempo promedio por proceso es: ", promedio)#Divide el tiempo en el num de process
desvest =0
times = list()
for i in times:
    desvest = (i-promedio)*(i-promedio)
print ("desviacion estandar es: ", desvest)#Desviacion por proceso


