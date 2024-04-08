"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
def pregunta_01():
    """Retorne la suma de la segunda columna.

    Rta/
    214
    """

    total = 0 #crear variable total que es la que va a sumar
    with open('data.csv','r') as file: #abrir archivo CSV
        for line in file: #crear bucle for itera sobre cada linea del archivo
            parts = line.strip().split('\t') #divide cada linea en partes
            if len(parts)>=2: #verificar si hay suficientes partes
                numbers=parts[1].split(',') #Extraer el segundo componente
                for number in numbers: #Iterar sobre los numeros
                    total+=int(number) #y sumarlos
    return total #despues de realizar todas las iteraciones devuelve el valor de total
print (pregunta_01()) #muestra la respuesta


def pregunta_02(): 
    """Retorne la cantidad de registros por cada letra de la primera columna como la lista
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
    
    conteo = {} #Lista para almacenar el conteo por letra
    with open('data.csv', 'r') as file: # Abrir archivo CSV
        for line in file: # Iterar sobre cada línea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letra = parts[0][0] # Obtener la primera letra de la línea
            conteo[letra] = conteo.get(letra, 0) + 1 #Condicional de conteo
    orden = sorted(conteo.items(), key=lambda x: x[0]) #convierte la lista en una (tuplas) lista ordenada alfabeticamente
    return orden # Retornar la lista de tuplas ordenada
resultado = pregunta_02() # Llamar a la función para obtener la cantidad de registros por cada letra
print(resultado) # Imprimir el resultado


def pregunta_03():
    """Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
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
    suma_conteo = {} #Lista para almacenar la suma correspondiente a cada letra
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letra = parts[0][0] # Obtener la primera letra de la línea
            if letra in dict(conteo).keys(): #Condiional si la letra esta en la lista de conteo
                columnados = int(parts[1]) #Obtener el valor
                suma_conteo[letra] = suma_conteo.get(letra,0) + columnados #suma
    orden = sorted(suma_conteo.items(), key=lambda x: x[0]) #convierte la lista en una (tuplas) lista ordenada alfabeticamente
    return orden #Retornar la lista de tuplas ordenada
conteo = pregunta_02() #calcular el conteo de registros por letra
suma_conteo = pregunta_03() #calcular la suma de la columna 2 por letra
print(suma_conteo) # imprimir el resultado 





def pregunta_04(): 
    """La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
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
    
    registro = [] #Lista para almacenar los registros por mes
    conteo = {}
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            if len(parts) >= 3: #Condicional de que la linea tiene o superas las 3 partes
                fecha = parts[2] #selecciona lo que hay en la columna 3
                parts_fecha = fecha.split('-') 
                mes = parts_fecha[1]
                conteo[mes] = conteo.get(mes, 0) + 1 #Condicional de conteo
    orden = sorted(conteo.items(), key=lambda x: x[0]) #convierte la lista en una (tuplas) lista ordenada alfabeticamente
    registro.append(orden)
    return registro
registro = pregunta_04()
print(registro) 


def pregunta_05():
    """Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
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

    maximo = {} #Lista para almacenar maximos
    minimo = {} #Lista para almacenar minimos
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letra = parts[0][0] # Obtener la primera letra de la línea
            columna_2 = int(parts[1]) #Convertir el numero en un entero
            if letra not in maximo:
                maximo[letra] = columna_2
                minimo[letra] = columna_2
            else:
                maximo[letra] = max(maximo[letra], columna_2)
                minimo[letra] = min(minimo[letra], columna_2)
    orden_maximo = sorted(maximo.items(), key=lambda x: x[0]) #convierte la lista en una (tuplas) lista ordenada alfabeticamente
    orden_minimo = sorted(minimo.items(), key=lambda x: x[0]) #convierte la lista en una (tuplas) lista ordenada alfabeticamente
    return orden_maximo, orden_minimo #Retornar la lista de tuplas ordenada
maximo, minimo = pregunta_05()
for (letra_max, maximo), (letra_min, minimo) in zip(maximo, minimo):
    print(f'("{letra_max}", {maximo}, {minimo})')


def pregunta_06(): 
    """La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
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
    clave = {} #Lista para almacenar maximos y minimos
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            diccionario = dict(item.split(':') for item in parts[4].split(','))
            for cla, valor in diccionario.items():
                valor = int(valor)
                if cla in clave:
                    clave[cla].append(valor)
                else:
                    clave[cla] = [valor]
    minimo = {cla: min(valores) for cla, valores in clave.items()}
    maximo = {cla: max(valores) for cla, valores in clave.items()}
    return minimo, maximo
minimo, maximo = pregunta_06()
for cla in sorted(minimo.keys()):
    valorminimo = minimo[cla]
    valormaximo = maximo[cla]
    print(f" {cla}, {valorminimo}, {valormaximo}") 

       

def pregunta_07():
    """Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
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
    lista_letras = {} #Lista para almacenar las letras en f(#)
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            numero = parts[1] #Obtener los numeros en la columna 2
            letras = parts[0] #Obtener las letras em la columna 1
            if numero in lista_letras:
                lista_letras[numero].extend(letras.split(','))
            else:
                lista_letras[numero] = letras.split(',')
    orden = sorted(lista_letras.keys())
    lista_tuplas = [(num, lista_letras[num]) for num in orden]
    return lista_tuplas
resultado = pregunta_07()
print(resultado) 


def pregunta_08(): 
    """Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
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
    lista_letras = {} #Lista para almacenar las letras en f(#)
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            numero = parts[1] #Obtener los numeros en la columna 2
            letras = sorted(set(parts[0].split(','))) #Obtener las letras em la columna 1
            if numero in lista_letras:
                lista_letras[numero].extend(letra for letra in letras if letra not in lista_letras[numero])
            else:
                lista_letras[numero] = letras
    orden = sorted(lista_letras.keys())
    for num in orden:
        lista_letras[num] = sorted(lista_letras[num])
    lista_tuplas = [(num, lista_letras[num]) for num in orden]
    return lista_tuplas
resultado = pregunta_08()
print(resultado)  


def pregunta_09(): 
    """Retorne un diccionario que contenga la cantidad de registros en que aparece cada
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
    clave = {} #Lista para almacenar maximos y minimos
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            diccionario = dict(item.split(':') for item in parts[4].split(','))
            for clave_reg in diccionario:
                if clave_reg in clave:
                    clave[clave_reg] += 1
                else:
                    clave[clave_reg] = 1
    orden = {k: v for k, v in sorted(clave.items())}
    return orden
resultado = pregunta_09()
print(resultado) 

def pregunta_10(): 
    """Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
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
    lista = []
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letra = parts[0][0] # Obtener la primera letra de la línea
            c4 = len(parts[3].split(','))
            c5_dict = dict(item.split(':') for item in parts[4].split(','))
            c5 = len(c5_dict)
            lista.append((letra, c4, c5))
    return lista
resultado = pregunta_10()
print(resultado)


def pregunta_11():
    """Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
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
    suma = {} #Lista para almacenar la suma de la columna 2
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letras = parts[3].split(',')
            numero = int(parts[1])
            for letra in letras:
                if letra in suma:
                    suma[letra] += numero
                else:
                    suma[letra] = numero
    orden = dict(sorted(suma.items()))
    return orden
resultado = pregunta_11()
print(resultado)


def pregunta_12():
    
    """Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
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
    suma_fila = {}
    with open('data.csv','r') as file: #Abrir archivo CSV
        for line in file: #Iterar sobre cada linea
            suma = 0
            parts = line.strip().split('\t') # Dividir la línea en componentes
            letra = parts[0]
            pares = parts[4].split(',')
            for par in pares:
                clave, valor = par.split(':')
                suma += int(valor)
            if letra in suma_fila:
                suma_fila[letra].append(suma)
            else:
                suma_fila[letra] = [suma]  # Crear una nueva lista para la primera aparición de la letra
    
    return suma_fila

resultado = pregunta_12()
for letra, sumas in sorted(resultado.items()):
    print(f"{letra}: {sum(sumas)}")