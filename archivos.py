from Clases import *
from listasenlazadas import *
from ListaObjetos import *

def lista_enlazada_txt(lista, archivo):
# abrir el archivo para escritura
    with open(archivo, 'w') as archivo:
        # recorrer la lista enlazada y escribir cada elemento en el archivo
        nodo_actual = lista.head
        while nodo_actual:
            archivo.write(str(nodo_actual.dato.__dict__))
            nodo_actual = nodo_actual.prox
            archivo.write('\n')
            #if nodo_actual:
                #archivo_salida.write('\n')

def lista_normal_txt(lista, archivo):
    with open(archivo, 'w') as archivo:
        for objeto in lista:
            archivo.write(str(objeto.__dict__))
        
def txt_lista_enlazada(lista,clase,archivo):
    # abrir el archivo para lectura
    with open(archivo, 'r') as archivo:
        # recorrer cada línea del archivo
        for linea in archivo:
            # convertir la línea en un diccionario
            diccionario = eval(linea)
            # crear una instancia de la clase Avion a partir del diccionario
            nodo=Nodo()
            nodo.dato = clase(**diccionario)
            # agregar el avión a la lista enlazada
            lista.append(nodo)
    # retornar la lista enlazada
    return lista

def txt_lista_normal(lista, clase,archivo):
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            diccionario = eval(linea)
            objeto=clase(**diccionario)
            lista.append([objeto])
    return lista


lista_enlazada_txt(lista_persona,"Persona.txt")
txt_lista_enlazada(lista_persona,Clases.persona,'Persona.txt')