# -*- coding: utf-8 -*-

import math

#Esta es la información que define el problema de el mapa de Rumania. Si se cambia el problema, esto ya no se necesita. 
ciudades= ["A","B","C","D","E","F","G","H","I","L","M","N","O","P","R","S","T","U","V","Z"]

#esta lista indica que la ciudad x tienen como vecinos a los que están en la lista vecinos[x]
vecinos=[["T", "S", "Z"],["F","G","P","U"],["D","P","R"],["C","M"],["H"],["B","S"],["B"],["E","U"],["N","V"],["M","T"],["D","L"],["I"],["S","Z"],["B","C","R"],["C","P","S"],["A","F","O","R"],["A","L"],["B","H","V"],["I","U"],["A","O"]]

costos_ind=[[118,140,75],[211,90,101,85],[120,138,146],[120,75],[86],[211,99],[90],[86,98],[87,92],[70,111],[75,70],[87],[151,71],[101,138,97],[146,97,80],[140,99,151,80],[118,111],[85,98,142],[92,142],[75,71]]

coordenadas=[[44.82029,279.40248],[401.54287,90.12111] ,[230.46163,43.40744],[129.14757,57.96755],[585.97086,48.86748],[292.34208,231.47547],[371.20931,24.60064],[554.42397,114.99463],[485.87014,295.7826],[129.75424,148.36153],[132.18092,103.46788],[408.21625,331.57619],[91.53396,371.61648],[309.93554,136.22811],[208.0148,185.36847],[178.89459,240.57553],[47.85365,185.97514],[465.85,114.99463],[525.91043,223.58874],[65.44711,326.72282]]
    

#Aquí se consulta al usuario de donde a donde quiere encontrar el camino. 
#Considera que esta consulta podría no ser necesaria pues se puede agregar directo en el código. También al cambiar de problema, esta consulta pierde sentido. 
estado_inicial=input("Escribe la inicial, en mayusculas y sin espacios, del estado del que quieres partir: ")
objetivo= input("Escribe el objetivo: ")


#****************************************************************************#
# Puedes cambiar todas las lineas de arriba por 
#.              -la definión del estado inicial y del objetivo como coordenadas, o sea una lista o vector con dos elementos. Recuerda en en imágenes el origen está arriba, investiga eso bien 
#               -carga la imagen desde archivo. Si queires, puede ser que se pida en pantalla el nombre o el número del archivo
#               - lee los pixeles de la imagen y guardalos en una matriz que tenga el mismo tamaño que la imagen pero que tenga sólo 0s y 1s, yo recomiento 1 sólo en donde sea negro, que es por donde sí se puede buscar camino. Las imagens que les di ya están umbralizadas en sólo blanco y negro

#****************************************************************************#



#Las siguientes funciones son las que hacen el planteamiento del problema para que se puede resolver por búsqueda de árboles. 

#esta función debe de regresar 1 si el estado (que para este problema es una letra) es el objetivo
def test_objetivo(estado): 
    if estado==objetivo:
        return 1
    else:
        return 0
        
#****************************************************************************#
#Cambia la función de arriba pero no le cambies el nombre. Aquí la variable de entrada, "estado", es una coordenada. Entonces sólo de tiene que evaluar si esta coordenada coincide con la esquina inferior derecha, y entonces regresa 1, de lo contrario regresa 0.
 #****************************************************************************#



# esta función recibe como entrada un estado cualquiera (cualqueir letra del problema Arad Bucarest) y regresa una lista de todos los posible estados a los que puede ir después. Para este problema, los sucesores de cada estado ya se conocen y están guardos en una de las listas de arriba.
def funcion_sucesor(estado): 
    i= ciudades.index(estado)
    return vecinos[i]
    
    
#****************************************************************************#
# la función sucesor es muy importante, tienes que cambiarla para que coincida con el problema de laberintos de hilos, pero no le cambies el nombre a la función. Recuerda que aquí, la variable de entrada, "estado" es una coordenada. La función tiene que hacer lo siguiente. A diferencia del problema de Rumania, los caminos posibles a partir de cualqueir posición son siempre "arriba", "abajo", "izquierda", "derecha". Entonces  haz que la función sucesor haga lo siguiente
#.              - inicializa una lista vacía para que guarde a los sucesores
#.              - Verfique si hay pixel arriba, porque si está en el limete de la imagen, puede que no haya. Si hay pixel arriba, que verifique si es un pixel negro, o con valor 1 en la matriz binaria. Si cumple con esas dos, agregas la coordenada que corresponde a "arriba" a la lista.
#.              - Verfique si hay pixel a la derecha, porque si está en el limete de la imagen, puede que no haya. Si hay pixel a la derecha, que verifique si es un pixel negro, o con valor 1 en la matriz binaria. Si cumple con esas dos, agregas la coordenada que corresponde a "derecha" a la lista.
#.              -  se hace lo mismo con abajo
#.              -  se hace lo mismo con izquierda
#.              - la función regresa esa lista
 #****************************************************************************#


# esta función recibe dos estados (letras) y da como salida el costo de la conexión entre esos dos estados, que está guardado en una de las listas del principio
def costo_entre_dos(estado1, estado2):   
    i= ciudades.index(estado1)
    j=vecinos[i].index(estado2)
    return costos_ind[i][j]
    
#****************************************************************************#
# esta es la función más fácil de cambiar, porque esta función sólo se usa en los procedimientos de abajo para calcular el costo entre dos estados vecinos. En el problema de Rumania esos costos eran los numeritos de la arista que los unía, Pero aquí, dos coordenadas, vecinas siempre van a tener de costo 1
#****************************************************************************#
    
    
#esta función es necesaria para el algoritmo A*. Utiliza las coordenadas cartesianas de cada una de las letras. Estas coordenadas también son conocidas por la definición del problema
def distancia_al_objetivo(estado):
    i= ciudades.index(estado)
    j=ciudades.index(objetivo)
    x1= coordenadas[i][0]
    x2=coordenadas[j][0]
    y1= coordenadas[i][1]
    y2= coordenadas[j][1]
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    
#****************************************************************************#
# para cambiar la función de distancia al objetivo, toma en cuenta que tanto la variable de entrada, "estado", como el "objetivo", para el problema de laberintos, ya son coordenadas. Así que sólo tienen que extrar sus valores x  y y y pueden dejar el cálculo de distancia en línea recta que ya tiene este código. 
#****************************************************************************#

# esta función no es parte del planteamiento del problema pero es necesaria para mostrar la solución
def en_pantalla(lista_estados):
    for x in lista_estados:
        if (x==objetivo):
            print(x)
        else:
            print("{} ->".format(x), end = ' ')

#****************************************************************************#
# Esta función, "en_pantalla",  sí requiere un poco más de cambios. Vas a hacer que por cada coordenada en la "lista_estados" sea pinte en la imagen un cuadrito de color amarillo en esa posición. Prueba pintando sólo el pixel, pero verás que la línea es muy delgada y se verá mejor si en su lugar pintas un cuadrito de 2x2 o de 3x3, ahí decide cuál se ve mejor
#****************************************************************************#


#********* si cambias correctamente todo lo que está indicado arriba. A partir de aquí ya no tienes que cambiar nada a menos que quieras hacer la versión PRO: que se vea una imagen que se va actualizando, pintanto la "frontera" en verde y los "vistos" en rojo ***********#


###funciones que se necesitan para el algoritmo de búsqueda,, esto ya es independiente del problema


#Todos los nodos van a estar guardados en una "Lista de nodos" y para tener la relación de paternidad entre ellos, vamos a hacer que dentro del nodo se guarde el indice del nodo padre

#La función de hacer_nodo almacena el índice del nodo actual y el índice del nodo padre
#nodo = [estado, índice de este nodo, índice del padre, profundidad, costo, heurística de A*]
#i_ padre sólo es -1 cuando es el nodo raíz
def hacer_nodo(estado, i_padre):
    d=distancia_al_objetivo(estado)
    if i_padre==-1: 
        n=[estado,0, -1, 1,0,0,d ] 
    else:
        c=nodos[i_padre][4]+costo_entre_dos(estado,nodos[i_padre][0])
        n=[estado,len(nodos), i_padre, nodos[i_padre][3]+1, c, c+d]
    nodos.append(n)
    return n

# esta función reconstruye la lista de acciones en orden para hallar la solución
def reconstruye(nodo):
    sol=[]
    n=list(nodo)
    while n[1]!= 0:
        sol.insert(0,n[0])
        n=nodos[n[2]]
    sol.insert(0,n[0])
    return sol
    

#esta función es util para revisar la lista de estados ya visitados. 
#Dependiendo de la definción del problema, un estado de búsqueda puede ser sólo un elemento o una lista de elementos, o hasta listas de listas, por eso esta función verfica los elementos del estado y si no hay concidencias con los estados guardados en la lista, regresa 0
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


# Aquí la consulta de estrategia de búsqueda
print("Escribe la estrategia que quieres seguir para la búsqueda. Elige escribiendo el número que corresponde")
print("1: Búsqueda en Profundidad")
print("2: Búsqueda en Amplitud")
print("3: Búsqueda primero el mejor, por costos")
print("4: Búsqueda A*")
E=input("Tu elección: ")



####### INICIA PROCEDIMIENTO DE BÚSQUEDA


#Información en pantalla, es opcional
print("En esta ocasión se busca el camino:")
en_pantalla([estado_inicial, objetivo])


# esta lista guarda estados ya vistos. También puede ser llamado closedset
visto=[]
#Para ahorrar memoria hacemos una lista que guarde todos los nodos, así cada nodo no tiene que guardar a su padre como uno de sus elementos
nodos =[]
# se declara la frontera como una lista vacía. También puede ser llamado openset
frontera= []
#Una lista donde estará lo solución
solucion=[]

######INICIA ALGORITMO DE BÚSQUEDA DE ÁRBOLES
# crea nodo a partir del estado incial y lo inserta dentro de la frontera
frontera.append(hacer_nodo(estado_inicial, -1))

#mientras la frontera no esté vacía
while len(frontera)!=0:
    #saca un elemento de la frontera para explorar sus sucesores, esto depende de la estrategia
    if E=="1": 
        nodo= frontera.pop()  # saca al útimo
    else: 
        nodo= frontera.pop(0)  # 0 saca el primero
    
    # guardo el estado que saque de la fronteda en los "vistos" para no volver a explorarlo
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
                    # esta es una insención ordenada de acuerdo al elemento 5 del nodo, que es la heurística
                    cuenta=len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[5]<frontera[i][5]:
                            frontera.insert(i,nuevo_nodo)
                            break
                    if cuenta== len(frontera):
                        frontera.append(nuevo_nodo)
                    #fin de la inseción ordenada
                if E=="3":
                    # esta es una insención ordenada de acuerdo al elemento 4 del nodo, que es el costo del camino
                    cuenta=len(frontera)
                    for i in range(cuenta):
                        if nuevo_nodo[4]<frontera[i][4]:
                            frontera.insert(i,nuevo_nodo)
                            break
                    if cuenta== len(frontera):
                        frontera.append(nuevo_nodo)
                        #fin de la inserción ordenada
                if E=="1" or E=="2":
                    # en el caso de las búsquedas desinformadas, simplemente se inserta cada sucedor al final de la frontera
                    frontera.append(nuevo_nodo) 
print("búsqueda finalizada con {} nodos explorados".format(len(nodos)))