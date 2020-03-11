class Automata():
    def __init__(self,nombre,terminales,estados,estado_inicial,transiciones):
        self.nombre = nombre
        self.terminales = terminales
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.transiciones = transiciones

class Estado():
    def __init__(self,nombre,aceptacion):
        self.nombre = nombre
        self.aceptacion = aceptacion

class Transicion():
    def __init__(self,inicial,final,valor):
        self.inicial = inicial
        self.final = final
        self.valor = valor
