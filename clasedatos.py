class informacion:

    def mi_lista(self):
        lista_Nomperros=["bobby", "dollar", "fany"]
        for x in lista_Nomperros:
            print(x)
#----------------------------------------------------
    def mi_tupla(self):
        tupla =["verde", "blanco", "azul"]
        for c in tupla:
            print(c)
#----------------------------------------------------
    def mi_diccionario(self):
        diccionario = {
        "raza:": "husky",
        "color:": "cafe",
        "edad:": 3
        }
        for x,y in diccionario.items():
            print(x,y)
#----------------------------------------------------
    def mi_conjuntos(self):
        conjuntos=[89, 67, 45]
        for x in conjuntos:
            print(x)
# creando el objeto
datos=informacion()
print("listado de nombre de perros")
datos.mi_lista()
print("listado de colores")
datos.mi_tupla()
print("listado de caracteristicas de un perro")
datos.mi_diccionario()
print("listado de numeros")
datos.mi_conjuntos()