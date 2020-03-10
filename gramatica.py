class Gramatica():
    def __init__(self,nombre,terminales,no_terminales,no_terminal_inicial,producciones):
        self.nombre = nombre
        self.terminales = terminales 
        self.no_terminales = no_terminales
        self.no_terminal_inicial = no_terminal_inicial
        self.producciones = producciones

class Produccion():
    def __init__(self,inicio,siguiente,terminal):
        self.incio = inicio
        self.siguiente = siguiente
        self.terminal = terminal