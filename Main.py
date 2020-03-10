import os
import time
from automata import Automata,Transicion,Estado

ayuda = """\n
----------------------------------------
| Lenguajes formales y de programacion |
|              Seccion: B-             |
|   Catedratico: Inga. Zulma Aguirre   |
|          Auxiliar: Luis Yela         |
|           Ultimo digito: 5           |
----------------------------------------
\n"""

#arreglos para almacenar los AFD y las gramaticas
automatas = []
gramaticas = []

#mostrar datos, recibir un enter y enviar al menu principal
print(" ")
print("----------Datos del estudiante----------")
print("|                                      |")
print("| Lenguajes formales y de programacion |")
print("|              Seccion: B-             |")
print("|           Carne: 201700965           |")
print("|                                      |")
print("----------------------------------------")
print(" ")
input("Presione enter para continuar")


def graphviz(afd,nombre):
    #inicio 
    dot = "digraph G{\nrankdir=LR\n"

    for estados in afd.estados:
        if estados.aceptacion == "1":
            dot = dot + estados.nombre + " [ label = "+ '"' + estados.nombre + '" shape = "doublecircle" ] \n'
        else:
            dot = dot + estados.nombre + " [ label = "+ '"' + estados.nombre + '" shape = "circle" ] \n'
    
    for transiciones in afd.transiciones:
        dot = dot + transiciones.inicial + "->" + transiciones.final + "[ label = " + '"' + transiciones.valor + '" ]\n'

    dot = dot + "init [label = " + '"' + "inicio" + '" shape =' + '"' + "plaintext" + '" ]\n' 
    dot = dot + "init ->" + afd.estado_inicial + "\n"
    dot = dot + "\n}"

    
    #cambiar los nombre de los dots y la imagen
    path_dot = "C:\\Users\\chepe\\Desktop\\" + nombre +".dot"
    path_imagen = "C:\\Users\\chepe\\Desktop\\" + nombre +".png"
    archivo_dot = open(path_dot,"w")
    archivo_dot.write(dot)
    archivo_dot.close()

    comando = "dot " + path_dot + " -Tpng -o " + path_imagen
    os.system(comando)

    os.system(path_imagen)

def modo1(automata,inicio,fin,terminal):
    #variable para validar
    validar = True
    validar1 = False
    validar2 = False
    validar3 = False

    #estados[0] inicio estados[1] final div[1] terminal
                    
    #recorrido para validar la existencia de los estados
    for valor in automata.estados:
        if inicio.upper() == valor.nombre:
            validar1 = True
                    
    for valor in automata.estados:
        if fin.upper() == valor.nombre:
            validar2 = True

    #validacion de la existencia de los estados
    if validar1== False or validar2 == False:
        print("\nLos estados ingresados no se encuentran en el AFD\n")
    else:
        #recorrido para validar la existencia del terminal
        for valor in automata.terminales:
            if valor == terminal.lower():
                validar3 = True
                                
            #validacion del terminal
            if validar3 == False:
                print("\nEl terminal no se encuentra en el AFD\n")
            else:
                #recorrido para validar que no exista una transicion desde un estado con el mismo terminal 
                for tran in automata.transiciones:
                    if tran.valor == terminal and inicio == tran.inicial:
                        validar = False

        #retorno de la validacion final
        if validar == True:
            transicion = Transicion(inicio.upper(),fin.upper(),terminal.lower())
            automata.transiciones.append(transicion)
            print("\nSe ha agregado la transicion\n")
        else:
            print("\nLos estados solo pueden tener una transicion con cada terminal\n")    


def menuAFD():
    #limpiar pantalla
    os.system("cls")

    #captura del nombre que tendra el automata
    nombre = input("Ingrese un nombre para el AFD: ")
    
    #verificacion del nombre del automata
    for valor in automatas:
        if valor.nombre == nombre:
            print("\nEl nombre del AFD ya existe, ingrese otro\n")
            time.sleep(1)
            menuAFD()

    #creacion del automata
    nuevo_automata = Automata(nombre,[],[],"",[])
    
    #agregando el automata al arreglo
    automatas.append(nuevo_automata)

    #impresion del menu
    print(" ")
    print("-------------Menu AFD------------")
    print("|                               |")
    print("| 1. Ingresar estados           |")
    print("| 2. Ingresar alfabeto          |")
    print("| 3. Estado inicial             |")
    print("| 4. Estados de aceptacion      |")
    print("| 5. Transiciones               |")
    print("| 6. Ayuda                      |")
    print("| 0. Regresar al menu principal |")
    print("|                               |")
    print("---------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            for valor in nuevo_automata.estados:
                print(str(valor.nombre) + " " + str(valor.aceptacion))
            
            if lectura == 1:
                #capturar el nombre del estado
                estado = input("\nIngrese el estado: ")

                #declaracion de la variable para validar su existencia
                aux = True

                #verificar si el valor del estado ingresado ya se encuentra en el AFD
                for validar in nuevo_automata.estados:
                    if validar.nombre == estado.upper():
                        aux = False
                for validar in nuevo_automata.terminales:
                    if validar.upper() == estado.upper():
                        aux = False

                #retorno de la verificacion del estado
                if aux == True:
                    estado = Estado(estado.upper(),"0")
                    nuevo_automata.estados.append(estado)
                    print("\nSe ha agregrado el estado al AFD\n")
                else:
                    print("\nEl estado ingresado ya se encuentra en el AFD\n")
            elif lectura == 2:
                #capturar el nombre del terminal
                terminal = input("\nIngrese el terminal: ")

                #declaracion de la variable para validar su existencia
                aux = True

                #verificar si el nombre del terminal ya se encuentra en el AFD
                for validar in nuevo_automata.estados:
                    if validar.nombre.lower() == terminal.lower():
                        aux = False
                for validar in nuevo_automata.terminales:
                    if validar == estado.lower():
                        aux = False

                #retorno de la validacion del terminal
                if aux == True:
                    nuevo_automata.terminales.append(terminal.lower())
                    print("\nSe ha agregrado el terminal al AFD\n")
                else:
                    print("\nEl terminal ingresado ya se encuentra en el AFD\n")
            elif lectura == 3:
                #capturar el estado inicial
                inicial = input("\nIngrese el estado inicial: ")

                #variable para verificar si el estado existe
                aux = False

                #verificar si el estado existe
                for verificar in nuevo_automata.estados:
                    if verificar.nombre == inicial.upper():
                        aux = True
                
                #retorno de la validacion del estado inicial
                if aux == True:
                    nuevo_automata.estado_inicial = inicial.upper()
                    print("\nSe a establecido el estado inicial\n")
                else:
                    print("\nEl estado ingresado no se encuentra en el AFD\n")
            elif lectura == 4:
                #capturar el estado de aceptacion
                aceptacion = input("\nIngrese el estado de aceptacion: ")

                #variable para verificar si el estado existe
                aux = False

                #verificar si el estado existe y cambiarlo a estado de aceptacion
                for valor in nuevo_automata.estados:
                    if valor.nombre == aceptacion.upper():
                        valor.aceptacion = "1"
                        aux = True
                
                #retorno de la validacion del estado de aceptacion
                if aux == True:
                    print("\nSe a establecido el estado de aceptacion\n")
                else:
                    print("\nEl estado ingresado no se encuentra en el AFD\n")
            elif lectura == 5:
                modo = input("\nSeleccione el numero del modo 1 o 2: ")
                if modo == "1":
                    #captura de la transicion
                    transicion = input("\nIngrese la transicion: ")
                    #division en estado inicial, estado final y terminal (EI,EF;T)
                    div = transicion.split(";")
                    estados = div[0].split(",")
                    modo1(nuevo_automata,estados[0],estados[1],div[1])

                elif modo == "2":
                    #declaracion de la matriz que almacenara la tabla de transiciones
                    matriz_transiciones = []

                    #declaracion de la fila de cabeceras para la matriz de transiciones  
                    columnas = []

                    #captura de los terminales de la cabecera
                    terminales = input("\nIngrese los terminales: ")

                    #agregando un valor cualquiera para empezar desde 1 la fila de cabeceras
                    columnas.append("NT/T")

                    #agregando los terminales a la fila de cabeceras
                    for valor in terminales.split(","):
                        columnas.append(valor.lower())

                    #agregando la cabecera a la matriz de transiciones
                    matriz_transiciones.append(columnas)

                    #captura de los no terminales que son cabeceras de las filas
                    no_terminales = input("Ingrese los no terminales: ")

                    #captura de los valores internos de la matriz
                    interior = input("Ingrese los simbolos de destino: ")

                    #division de los valores internos de la matriz
                    aux = no_terminales.split(",")
                    particion = interior.split(";")
                    
                    #declaracion de la variable iterativa para recorrer la division
                    it = 0

                    #recorrido de las cabeceras de las filas
                    for noTerminal in aux:
                        
                        #declaracion del arreglo auxiliar que almacenara las filas
                        temp = []
                        
                        #agregando el valor de la cabecera de la fila
                        temp.append(noTerminal.upper())
                        
                        #validando que la variable iterativa no exceda la longitud del arreglo
                        if it < len(particion):

                            #recorriendo los valores internos de la matriz
                            for interior in range(it,len(particion)):
                                valor = particion[it].split(",")
                                for iterador in valor:
                                    temp.append(iterador.upper())
                                it = it + 1
                                break
                        #agregando la nueva fila a la matriz
                        matriz_transiciones.append(temp)

                    for i in range(0,len(matriz_transiciones)):
                        for j in range(0,len(matriz_transiciones[i])):
                            print(str(matriz_transiciones[i][j]) + "\t",end=" ")
                        print("\n") 
                else:
                    print("\nIngrese unicamente el numero 1 o 2\n")
            elif lectura == 6:
                print(ayuda)
            elif lectura == 0:
                graphviz(nuevo_automata,nuevo_automata.nombre)
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def menuGramatica():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("-----------Menu Gramatica------------")
    print("|                                   |")
    print("| 1. Ingresar NT                    |")
    print("| 2. Ingresar terminales            |")
    print("| 3. NT inicial                     |")
    print("| 4. Producciones                   |")
    print("| 5. Mostrar gramatica transformada |")
    print("| 6. Ayuda                          |")
    print("| 0. Regresar al menu principal     |")
    print("|                                   |")
    print("-------------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                pass
            elif lectura == 2:
                pass
            elif lectura == 3:
                pass
            elif lectura == 4:
                pass
            elif lectura == 5:
                pass
            elif lectura == 6:
                print(ayuda)
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def menuEvaluarCadenas():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("-------Menu evaluar cadenas------")
    print("|                               |")
    print("| 1. Solo validar               |")
    print("| 2. Ruta en AFD                |")
    print("| 3. Expandir con gramatica     |")
    print("| 4. Ayuda                      |")
    print("| 0. Regresar al menu principal |")
    print("|                               |")
    print("---------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                pass
            elif lectura == 2:
                pass
            elif lectura == 3:
                pass
            elif lectura == 4:
                print(ayuda)
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def menuArchivos():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("-------Menu manejo de archivos------")
    print("|                                  |")
    print("| 1. Abrir AFD                     |")
    print("| 2. Abrir gramatica               |")
    print("| 3. Guardar AFD                   |")
    print("| 4. Guardar gramatica             |")
    print("| 0. Regresar al menu principal    |")
    print("|                                  |")
    print("------------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                pass
            elif lectura == 2:
                pass
            elif lectura == 3:
                pass
            elif lectura == 4:
                pass
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def menuReportes():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("----------Menu reportes----------")
    print("|                               |")
    print("| 1. Ver detalle                |")
    print("| 2. Generar reporte            |")
    print("| 3. Ayuda                      |")
    print("| 0. Regresar al menu principal |")
    print("|                               |")
    print("---------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                pass
            elif lectura == 2:
                pass
            elif lectura == 3:
                print(ayuda)
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")   

def menuPrincipal():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("---------Menu Principal---------")
    print("|                              |")
    print("| 1. Crear AFD                 |")
    print("| 2. Crear Gramatica           |")
    print("| 3. Evaluar cadenas           |")
    print("| 4. Reportes                  |")
    print("| 5. Cargar archivo de entrada |")
    print("| 0. Salir                     |")
    print("|                              |")
    print("--------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                menuAFD()
            elif lectura == 2:
                menuGramatica()
            elif lectura == 3:
                menuEvaluarCadenas()
            elif lectura == 4:
                menuReportes()
            elif lectura == 5:
                menuArchivos()
            elif lectura == 0:
                print("\nHasta la proxima c:\n")
                exit(0)
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()
