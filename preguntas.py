
"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


import csv

def lectura_de_documento():
        
    
# leo el documento csv

    archivo_csv="data.csv"
    with open (archivo_csv,"r") as file:
        lista_texto=file.readlines()

# organizar los datos, reemplazar sonido de carro por espacio y separar en una lista de listas
    lista_texto=[i.replace("\n","") for i in lista_texto]
    lista_texto=[i.split("\t") for i in lista_texto]
    
    return lista_texto

lectura_de_documento()

def pregunta_01():

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Variable para la función de lectura del csv
    lectura = lectura_de_documento()

    # Creación de:
    # 1. Lista para almacenar los datos de la segunda columna
    # 2. Variable que me permtirá sumar los valores
    # Nota: los valores en la lista ingresarán como tipo número 

    suma=0
    lista_columna2=[]

    for lista_interna in lectura:
        lista_columna2.append(int(lista_interna[1]))

    # Iteración para sumar los números 

    for i in lista_columna2:
        suma+=i
        
    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista_texto=lectura_de_documento()

    # Creación de una lista y un diccionario vacío

    lista=[]
    diccionario={}

    # Conformar la lista con una tupla que contiene la letra y un valor 1
    # Ordenar la lista con base en el primer elemento de la tupla x[0] a través de una función anónima

    for i in lista_texto:
        lista.append((i[0],1))
        lista= sorted(lista, key=lambda x:x[0])

    # A partir de la tupla conformada por clave, valor, lleno el diccionario.
    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
    
# realizo la sumatoria de los valores, a partir de una lista vacía
    respuesta=[]

    for key, valor in diccionario.items():
        respuesta.append((key,sum(valor)))
    
    return respuesta



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista_texto=lectura_de_documento()

# creamos una lista y un diccionario vacio

    lista=[]
    diccionario={}

# llenamos la lista creada con una tupla, conformada por columna 1 y columna 2
# la columna dos debe convertirse en número entero. 

    for i in lista_texto:
        lista.append((i[0],int(i[1])))
        lista=sorted(lista,key=lambda x:x[0])

# llenamos el diccionario con las tuplas, con clave, valor
## preguntarle a Alejo la parte del append

    for key, value in lista:
        if key not in diccionario:
            diccionario[key]=[]
        diccionario[key].append(value)

    respuesta=[]

# realizo la sumatoria a partir del método items, el cual permite iterar sobre diccionarios

    for key, value in diccionario.items():
        respuesta.append((key,sum(value)))

    return respuesta



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    lista_texto=lectura_de_documento()

    lista=[]

    for i in lista_texto:
        lista.append((i[2].split("-")[1]))

    lista_mes=[]   

    for i in lista:
        lista_mes.append((i,1))
        lista_mes= sorted(lista_mes,key=lambda x:x[0])

    diccionario={}

    for key, value in lista_mes:
        if key not in diccionario:
            diccionario[key]=[]
        diccionario[key].append(value)

    respuesta=[]

    for key, value in diccionario.items():
        respuesta.append((key,sum(value)))

    return respuesta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    lista_texto=lectura_de_documento()

    lista=[]

    for i in lista_texto:
        lista.append((i[0],int(i[1])))
        lista=sorted(lista,key= lambda x:x[0])

    diccionario={}

    for key, value in lista:
        if key not in diccionario:
            diccionario[key]=[]
        diccionario[key].append(value)

    respuesta=[]

    for key, value in diccionario.items():
        respuesta.append((key,max(value),min(value)))

    return respuesta

# respuesta_05= pregunta_05()
# print(respuesta_05)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista_texto=lectura_de_documento()

# lista = [i[4].split(",") for i in lista_texto[0:]]
    lista=[]

    for i in lista_texto:
        lista.append(i[4].split(","))

    lista_2 = []
    lista_3= []
    
    for i in lista:
        for j in i:
            lista_2 = tuple(j.split(":"))
            lista_3.append(lista_2)

    lista_3=sorted(lista_3,key=lambda x:x[0])

    diccionario={}

    for key, value in lista_3:
        if key not in diccionario.keys(): 
            diccionario[key]=[]
        diccionario[key].append(int(value))

    respuesta=[]

    for key, value in diccionario.items():
        respuesta.append((key,min(value),max(value)))

    return respuesta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista_texto=lectura_de_documento()

    lista=[]

    for i in lista_texto:
        lista.append((int(i[1]),i[0]))
        lista = sorted(lista, key=lambda x: x[0])
    
    diccionario= {}

    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)

    respuesta=[]

    for key, value in diccionario.items():
        respuesta.append((key, value))
        

    return respuesta

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista_texto=lectura_de_documento()

    lista=[]

    for i in lista_texto:
        lista.append((int(i[1]),i[0]))
        lista = sorted(lista, key=lambda x: x[0])
    
    diccionario= {}

    for key, value in lista:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)

    respuesta=[]

    for key, value in diccionario.items():
        value=list(set(value))
        values= "".join(value)
        values= sorted(values)
    
        respuesta.append((key, values))

    return respuesta



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista_texto=lectura_de_documento()

    lista=[i[4].split(",") for i in lista_texto]

    lista_3=[]

    for i in lista:
        for j in i:
            lista_2= tuple(j.split(":"))
            lista_3.append(lista_2)

    lista_3= sorted(lista_3, key=lambda x: x[0])

    diccionario={}

    for key, value in lista_3:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(len(value))
    
    lista_4=[]

    for key, value in diccionario.items():
        lista_4.append((key,len(value)))

    respuesta={key:value for key,value in lista_4}

    return respuesta



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_texto=lectura_de_documento()

    respuesta=[]

    for i in lista_texto:
        respuesta.append((i[0],len(i[3].split(",")), len(i[4].split(","))))

    return respuesta



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    lista_texto=lectura_de_documento()

    lista=[]

    for i in lista_texto:
        lista.append((i[3].split(","), int(i[1])))

    lista_tupla=[]


    for key, value in lista:
        for j in key:
            lista_tupla.append((j,value))

    lista_ordenada= sorted(lista_tupla,key= lambda x:x[0])

    diccionario={}

    for key, value in lista_ordenada:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
    
    Lista_prueba=[]

    for key, value in diccionario.items():
        Lista_prueba.append((key, sum(value)))

    respuesta={key:value for key, value in Lista_prueba}

    return respuesta




def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lista_texto=lectura_de_documento()
    
    lista = []
    diccionario ={}

    for i in lista_texto:
        
        lista.append((i[0], i[4].split(",") ))         

    list_tupla = []
    list_tupla_2 = []
    
    for key, value in lista:        
        for i in value:
            list_tupla.append((key, i.split(":")))
            
    for key, value in list_tupla:
        list_tupla_2.append((key, int(value[1])))

    list_tupla_2 = sorted(list_tupla_2, key=lambda x: x[0])

    for key, value in list_tupla_2:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)
        
    list_Prob = []

    for key, value in diccionario.items():
            list_Prob.append((key, sum(value)))

    respuesta = {key:value for key, value in list_Prob}    

    return respuesta