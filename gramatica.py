class Gramatica():
    def __init__(self,nombre,terminales,no_terminales,no_terminal_inicial,producciones,transformacion):
        self.nombre = nombre
        self.terminales = terminales 
        self.no_terminales = no_terminales
        self.no_terminal_inicial = no_terminal_inicial
        self.producciones = producciones
        self.transformacion = transformacion

class Produccion():
    def __init__(self,inicio,ladoDerecho,recursividad):
        self.inicio = inicio
        self.ladoDerecho = ladoDerecho
        self.recursividad = recursividad
        
class LadoDerecho():
    def __init__(self,terminal,siguiente):
        self.siguiente = siguiente
        self.terminal = terminal