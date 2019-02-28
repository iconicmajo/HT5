#Maria Jose Castro Lemus 181202
#Andres Berthet 171504
#Estructura de datos
#Lab 5
#Programa de simulacion

import simpy
import random

cpu = 1
ram = 1

def simular(nombre,env,wait_time,space):
    global totalPro  # :( mala practica, pero ni modo

       yield env.timeout(wait_time)
    
    
    posLlegada = env.now

    
    tiempoPro = random.randint(1, 7)
    #tiempoPro = (1, 7)
    print ('%s empieza en %f necesita %d para proceso' % (nombre,posLlegada,tiempoPro))
    
    
    with space.request() as turno:
        yield turno     
        yield env.timeout(tiempoPro) 
        print ('%s proceso termina a las %f' % (nombre, env.now))
        
        
    tiempoTotal = env.now - posLlegada
    print ('%s se tardo %f' % (nombre, tiempoTotal))
    totalPro = totalPro + tiempoTotal
0           

# ----------------------

env = simpy.Environment() #ambiente de simulación
space:cpu = simpy.Container(env,capacity = 1)#Cantidad de CPU
random.seed(10) # fijar el inicio de random

totalPro = 0
for i in range(25):
    env.process(simular('proceso %d'%i,env,random.expovariate(1.0/10),space))

env.run()  #correr la simulación en tiempo infinito

print ("tiempo promedio por proceso es: ", totalPro/25.0)


