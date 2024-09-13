print("Funciones Version 2")
print("Nancy Lara")
# Zona de listas tuplas conjuntos y diccionario
celulares=["Samsung a52", "iphone 11", "Chafa"]
Album=["Las 3 torres", "El problema", "Contingente"]
canciones={"Veneno", "Cologne", "15 besos", "Pienso en ella"}
cantantes={"Cornelio Vega","Antonio","Edwin Luna"}
thisdict={
    "Cornelio vega" : "Cornelio Vega y su Dinastia",
    "Antonio" : "Junior H",
    "Edwin Luna" : "La tracalosa de Monterrey"
}
# Zona de funciones
# este es una lista
def verlista(telefonos):
    for uncelular in telefonos:
        print (uncelular)
        
# este ees una tupla
def vertupla(Album):
    for unAlbum in Album:
        print (unAlbum)

# este es un set
def verset(canciones):
    for cancioness in canciones:
        print(cancioness)
        
# este es un diccionario
def verdiccionario(cantantes):
    for uncantantes in cantantes:
        print(cantantes)
                
# Llamadas a funciones
print ("Imprime celulares de una lista")
verlista(celulares)

print ("Imprime Album de una tuplas")
vertupla(Album)

print ("Imprime Canciones de un set")
verset(canciones)

print ("Imprime cantates de un diccionario")
verdiccionario(cantantes)