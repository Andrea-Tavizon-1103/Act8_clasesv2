print("Clases version 2 el constructor")

class perro:
# funcion constructor
    def __init__(self,color, edad):
        self.color = color
        self.edad = edad
# funciones creadas por el usuario
    def morder(self):
        print("chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self,mmensaje):
        print(f"Chat perra: {mmensaje}")
    def datos(self):
        print(f"color: {self.color} edad: {self.edad}")
# crear el objeto
chihuas = perro("cafe", 4)
#llamadas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola bobby")
chihuas.chatperro("quieres ser mi guauguau?")
chihuas.chatperra("grrru.......")
