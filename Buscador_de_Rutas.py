import cv2 as cv
import numpy as np
import sys
import math

np.set_printoptions(threshold=sys.maxsize)
img = cv.imread('hilo1.png',cv.IMREAD_GRAYSCALE)
matrix=np.matrix(img)
matrix2=np.where( matrix == 255 ,1,0)
objetivo=[256,256]

def test_objetivo(estado): 
    if estado==objetivo:
        return 1
    else:
        return 0

def funcion_sucesor(estado): 
    i= ciudades.index(estado)
    return vecinos[i]

def costo_entre_dos(estado1, estado2):   
    return 1

def distancia_al_objetivo(estado):
    i= ciudades.index(estado)
    j=ciudades.index(objetivo)
    x1= coordenadas[i][0]
    x2=coordenadas[j][0]
    y1= coordenadas[i][1]
    y2= coordenadas[j][1]
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def en_pantalla(lista_estados):
    for x in lista_estados:
        if (x==objetivo):
            print(x)
        else:
            print("{} ->".format(x), end = ' ')

def reconstruye(nodo):
    sol=[]
    n=list(nodo)
    while n[1]!= 0:
        sol.insert(0,n[0])
        n=nodos[n[2]]
    sol.insert(0,n[0])
    return sol

def dentro_de(estado, lista_de_estados):
    rep=0
    for y in lista_de_estados:
        eq=0
        for i in range(len(estado)):
            if estado[i]!=y[i]:
                break
            eq=eq+1
        if eq==len(estado):    
            return 1
    return 0

print("Escribe la estrategia que quieres seguir para la búsqueda. Elige escribiendo el número que corresponde")
print("1: Búsqueda en Profundidad")
print("2: Búsqueda en Amplitud")
print("3: Búsqueda primero el mejor, por costos")
print("4: Búsqueda A*")
E=input("Tu elección: ")
# print("En esta ocasión se busca el camino:")
# en_pantalla([estado_inicial, objetivo])

visto=[]
nodos =[]
frontera= []
solucion=[]
frontera.append(hacer_nodo(estado_inicial, -1))

while len(frontera)!=0:
    if E=="1": 
        nodo= frontera.pop()
    else: 
        nodo= frontera.pop(0) 
    visto.append(nodo[0])
if test_objetivo(nodo[0])==1:
        print("*****solución encontrada*****")
        print("Pasos para llegar a la solución: {}".format(nodo[3]-1))
        print("Costo total de la solución: {}".format(nodo[4]))
        
        solucion=reconstruye(nodo)
        
        en_pantalla(solucion)
        
        break
    
    else:
        sucesores = funcion_sucesor(nodo[0])
        for x in sucesores:
            if  dentro_de(x,visto)==0: 
                nuevo_nodo= hacer_nodo(x,nodo[1])
                if E=="4":
                    cuenta=len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[5]<frontera[i][5]:
                            frontera.insert(i,nuevo_nodo)
                            break
                    if cuenta== len(frontera):
                        frontera.append(nuevo_nodo)
                if E=="3":
                    cuenta=len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[4]<frontera[i][4]:
                            frontera.insert(i,nuevo_nodo)
                            break
                    if cuenta== len(frontera):
                        frontera.append(nuevo_nodo)
                if E=="1" or E=="2":
                    frontera.append(nuevo_nodo) 
print("búsqueda finalizada con {} nodos explorados".format(len(nodos)))