import os
import time
from automata import Automata,Transicion,Estado
from gramatica import Gramatica,Produccion,LadoDerecho

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

#valor de la repeticion
repeticion = 0

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

def removerRecursividad(gramatica,inicial,final,siguiente):
    nuevoNoTerminal = inicial+"_P"
    aux = False

    for produccion in gramatica.producciones:
        if produccion.inicio == nuevoNoTerminal:
            aux = True 
            break

    if aux == False:
        prod = Produccion(nuevoNoTerminal,[LadoDerecho(siguiente,nuevoNoTerminal),LadoDerecho("epsilon","epsilon")],"1")
        gramatica.producciones.append(prod)
        gramatica.transformacion.append(Produccion(inicial,[LadoDerecho(inicial,siguiente)],"0"))
        for valor in gramatica.producciones:
            if valor.inicio == inicial:
                gramatica.transformacion.append(valor)
        for valor in gramatica.producciones:
            if valor.inicio == inicial:
                for derecha in valor.ladoDerecho:
                    derecha.siguiente = nuevoNoTerminal
                break
    else:
        aux = False
        for valor in produccion.ladoDerecho:
            if valor.terminal == siguiente:
                aux = True
                break
        if aux == False:
            produccion.ladoDerecho.append(LadoDerecho(siguiente,nuevoNoTerminal))
            for valor in gramatica.transformacion:
                if valor.inicio == inicial:
                    valor.ladoDerecho.append(LadoDerecho(inicial,siguiente))
                    break
        else:
            print("\nLa produccion ya se encuentra en la gramatica\n")
    """
    A -> A b
        | c
        | d
    
    quitando recursividad:

    A -> c A_P
        |d A_P
    A_P -> b A_P
          | epsilon

    """

def crearTerminalGramatica(gramatica,terminal):
    #variable para validar la existencia del no terminal
    validar = False

    #recorrido para validar la existencia del no terminal
    for valor in gramatica.no_terminales:
        if valor == terminal.upper():
            validar = True
                
    for valor in gramatica.terminales:
        if valor == terminal.lower():
            validar = True
                
    #retorno de la validacion
    if validar == False:
        gramatica.terminales.append(terminal.lower())
        return"\nSe ha agregado el terminal a la gramatica\n"
    else:
        return"\nEl valor del terminal ya se encuentra en la gramatica\n"

def crearNoTerminalGramatica(gramatica,noTerminal):
    #variable para validar la existencia del no terminal
    validar = False

    #recorrido para validar la existencia del no terminal
    for valor in gramatica.no_terminales:
        if valor == noTerminal.upper():
            validar = True
                
    for valor in gramatica.terminales:
        if valor == noTerminal.lower():
            validar = True
                
    #retorno de la validacion
    if validar == False:
        gramatica.no_terminales.append(noTerminal.upper())
        return"\nSe ha agregado el no terminal a la gramatica\n"
    else:
        return"\nEl valor del no terminal ya se encuentra en la gramatica\n"

def crearProduccion(gramatica,produccion):
    #separacion de la produccion 
    valor = produccion.split(">")
                
    #variable para validar la existencia del no terminal
    aux = False

    #validando existencia del no terminal inicial
    for noTerminal in gramatica.no_terminales:
        if valor[0].upper() == noTerminal:
            aux = True

    if aux == True:
        #revisar que el valor producido sea o no epsilon
        if valor[1].lower() == "epsilon":
                       
            aux = False
            #verificando que la produccion no este ya en la gramatica
            for veri in gramatica.producciones:
                if veri.inicio == valor[0].upper():
                    for derecho in veri.ladoDerecho:
                        if derecho.terminal == "epsilon": 
                            aux = True
                            break

            if aux == True:
                return"\nLa produccion ya se encuentra en la gramatica\n"
            else:
                aux = False
                aux1 = False
                            
                #verificando si ya existe una produccion con el no terminal inicial
                for produccion in gramatica.producciones:
                    if produccion.inicio == valor[0].upper():
                        aux = True
                        break
                for trans in gramatica.transformacion:
                    if trans.inicio == valor[0].upper():
                        aux1 = True
                        break
                            
                if aux1 == True:
                    trans.ladoDerecho.append(LadoDerecho("epsilon","epsilon"))
                else:
                    gramatica.transformacion.append(Produccion(valor[0].upper(),[LadoDerecho("epsilon","epsilon")],"0"))
                if aux == True:
                    produccion.ladoDerecho.append(LadoDerecho("epsilon","epsilon"))
                else:
                    gramatica.producciones.append(Produccion(valor[0].upper(),[LadoDerecho("epsilon","epsilon")],"0"))
                    return"\nLa produccion se ha agregado a la gramatica\n"
        else:
            aux = False

            #dividiendo el lado derecho de la produccion
            derecho = valor[1].split(" ")

            #verificando si existe recursividad por la izquierda
            for noTerminal in gramatica.no_terminales:
                if noTerminal == derecho[0].upper():
                    aux = True
                    break

            if aux == True and len(derecho)>1:
                            
                aux = False

                #verificando que el terminal exista en la gramatica
                for terminal in gramatica.terminales:
                    if terminal == derecho[1].lower():
                        aux = True
                        break
                        
                if aux == True:
                    removerRecursividad(gramatica,valor[0].upper(),"no",derecho[1].lower())
                else:
                    return"\nEl terminal no se encuentra en la gramatica\n"
            else:
                            
                aux = False

                if len(derecho) == 1:
                    aux = False

                    #verificando la existencia del terminal en la gramatica
                    for terminal in gramatica.terminales:
                        if terminal == derecho[0].lower():
                            aux = True
                            break

                    if aux == True:
                                    
                        aux = False

                        #verificando que exista una produccion con el no terminal inicial
                        for produccion in gramatica.producciones:
                            if produccion.inicio == valor[0].upper():
                                aux = True
                                break
                        for tran in gramatica.transformacion:
                            if tran.inicio == valor[0].upper():
                                break

                        #Si existe una produccion verificar si la que existe es recursiva por la izquierda
                        if aux == True:
                            aux = False
                            nuevoNoTerminal = valor[0].upper()+"_P"
                                        
                            #verificando si existe una produccion recursiva asociada
                            for prod in gramatica.producciones:
                                if prod.inicio == nuevoNoTerminal:
                                    aux = True
                                    break
                                    
                            if aux == True:
                                aux = False

                                #verificando si ya esta la produccion en la gramatica
                                for val in produccion.ladoDerecho:
                                    if val.terminal ==  derecho[0].lower() and val.siguiente == nuevoNoTerminal:
                                        aux = True
                                        break

                                if aux == False:
                                    produccion.ladoDerecho.append(LadoDerecho(derecho[0].lower(),nuevoNoTerminal))
                                    produccion.recursividad = "1"
                                    tran.ladoDerecho.append(LadoDerecho(derecho[0].lower(),"no"))
                                else:
                                    return"\nLa produccion ya se encuentra en la gramatica\n"
                            else:
                                aux = False

                                #verificando si la produccion ya esta en la gramatica
                                for val in produccion.ladoDerecho:
                                    if val.terminal ==  derecho[0].lower() and val.siguiente == "no":
                                        aux = True
                                        break

                                if aux == False:
                                    produccion.ladoDerecho.append(LadoDerecho(derecho[0].lower(),"no"))
                                    tran.ladoDerecho.append(LadoDerecho(derecho[0].lower(),"no"))
                                else:
                                    return"\nLa produccion ya se encuentra en la gramatica\n"
                        else:
                            aux = False
                            nuevoNoTerminal = valor[0].upper()+"_P"
                                        
                            #verificando si existe una produccion recursiva asociada
                            for prod in gramatica.producciones:
                                if prod.inicio == nuevoNoTerminal:
                                    aux = True
                                    break

                            if aux == True:
                                gramatica.producciones.append(Produccion(valor[0].upper(),[LadoDerecho(derecho[0].lower(),nuevoNoTerminal)],"1"))
                                tran.ladoDerecho.append(LadoDerecho(derecho[0].lower(),"no"))
                            else:
                                gramatica.producciones.append(Produccion(valor[0].upper(),[LadoDerecho(derecho[0].lower(),"no")],"0"))
                                gramatica.transformacion.append(Produccion(valor[0].upper(),[LadoDerecho(derecho[0].lower(),"no")],"0"))
                    else:
                        return"\nEl terminal no existe en la gramatica\n"
                else:
                    aux = False

                    #verificando la existencia del no terminal en la gramatica
                    for noTerminal in gramatica.no_terminales:
                        if noTerminal == derecho[1].upper():
                            aux = True
                            break

                    if aux == True:

                        aux = False

                        #verificando la existencia del terminal en la gramatica
                        for termi in gramatica.terminales:
                            if termi == derecho[0].lower():
                                aux = True
                                break

                        if aux == True:
                            aux = False
                            
                            #verificando que no se repita la produccion
                            for produccion in gramatica.producciones:
                                if produccion.inicio == valor[0].upper():
                                    for val in produccion.ladoDerecho:
                                        if val.terminal == derecho[0].lower() and val.siguiente == derecho[1].upper():
                                            aux = True
                                            break
                                        
                            if aux == True:
                                return"\nLa produccion ya se encuentra en la gramatica\n"
                            else:
                                aux = False
                                
                                #verificando si existe una produccion con el no terminal inicial
                                for produccion in gramatica.producciones:
                                    if produccion.inicio == valor[0].upper():
                                                    
                                        #agregando el lado derecho a la produccion existente
                                        produccion.ladoDerecho.append(LadoDerecho(derecho[0].lower(),derecho[1].upper()))
                                        aux = True
                                        break
                                            
                                for tran in gramatica.transformacion:
                                    if tran.inicio == valor[0].upper():
                                        tran.ladoDerecho.append(LadoDerecho(derecho[0].lower(),derecho[1].upper()))
                                        break

                                if aux == True:
                                    return"\nSe ha agregado la produccion a la gramatica\n"
                                else:
                                    gramatica.producciones.append(Produccion(valor[0].upper(),[LadoDerecho(derecho[0].lower(),derecho[1].upper())],"0"))
                                    gramatica.transformacion.append(Produccion(valor[0].upper(),[LadoDerecho(derecho[0].lower(),derecho[1].upper())],"0"))
                                    return"\nSe ha agregado la produccion a la gramatica\n"                                   
                        else:
                            return"\nEl terminal ingresado no existe en la gramatica\n"
                    else:
                        return"\nEl no terminal ingresado no existe en la gramatica\n"
    else:
        return"\nEl no terminal inicial no exite en la gramatica\n"

def traduccionHaciaGramatica(automata):
    #creando el nombre de la gramatica traducida
    nombre = automata.nombre+"_GramaticaTraducida"

    #obteniendo los no terminales
    noTerminales = []
    for valor in automata.estados:
        noTerminales.append(valor.nombre)

    #creando el objeto gramatica
    nueva_gramatica = Gramatica(nombre,automata.terminales,noTerminales,automata.estado_inicial,[],[])

    #transformando las transiciones en producciones
    for transicion in automata.transiciones:
        #NT>T NT(Gramatica) ; de NT1 a NT2 con T (AFD) 
        
        aux = False

        for producciones in nueva_gramatica.producciones:
            if producciones.inicio == transicion.inicial:
                aux = True
                break
        
        if aux == True:
            producciones.ladoDerecho.append(LadoDerecho(transicion.valor,transicion.siguiente))
        else:
            nueva_gramatica.producciones.append(Produccion(transicion.inicial,[LadoDerecho(transicion.valor,transicion.final)],"0"))
    
    #transformando el estado de aceptacion en una produccion que deriva en epsilon
    for estado in automata.estados:
        if estado.aceptacion == "1":
            for producciones in nueva_gramatica.producciones:
                if producciones.inicio == estado.nombre:
                    break
        
            producciones.LadoDerecho.append(LadoDerecho("epsilon","epsilon"))

    #validando si ya se realizo la traduccion    
    aux = False

    for it in range(0,len(gramaticas)):
        if gramaticas[it].nombre == nombre:
            gramaticas[it] = nueva_gramatica
            aux = True
            break 
    
    if aux == False:
        gramaticas.append(nueva_gramatica)

def traduccionHaciaAutomata(gramatica):
    #creando el nombre del nuevo automata
    nombre = gramatica.nombre+"_AutomataTraducido"

    #convirtiendo los no terminales a estados
    estados = []
    for noTerminal in gramatica.no_terminales:
        estados.append(Estado(noTerminal,"0"))

    #creando el objeto AFD
    nuevo_automata = Automata(nombre,gramatica.terminales,estados,gramatica.no_terminal_inicial,[])
   

    #variable para validar la creacion de un estado sumidero
    iterador = 0

    #transformando las producciones que sean disntinas de epsilon y un solo terminal a transiciones
    for producciones in gramatica.producciones:
        for derecha in producciones.ladoDerecho:
            if derecha.siguiente != "no" and derecha.siguiente != "epsilon":
                nuevo_automata.transiciones.append(Transicion(producciones.inicio,derecha.siguiente,derecha.terminal))
            else:
                if derecha.siguiente=="no":
                    iterador = iterador + 1
    
    #verificando la existencia del estado sumidero y creandolo de ser necesario
    if iterador > 0:
        nuevo_automata.estados.append(Estado("Sumidero","1"))
    
    #transformando las producciones que sean de un solo terminal a transiciones hacia el estado sumidero
    for producciones in gramatica.producciones:
        for derecha in producciones.ladoDerecho:
            if derecha.siguiente == "no":
                nuevo_automata.transiciones.append(Transicion(producciones.inicio,"Sumidero",derecha.terminal))
    
    #transformando las producciones que sean epsilon a estados de aceptacion
    for producciones in gramatica.producciones:
        for derecha in producciones.ladoDerecho:
            if derecha.siguiente == "epsilon":
                for estado in nuevo_automata.estados:
                    if estado.nombre == producciones.inicio:
                        estado.aceptacion = "1"
                        break
    
    #validando si ya se realizo la traduccion    
    aux = False

    for it in range(0,len(automatas)):
        if automatas[it].nombre == nombre:
            automatas[it] = nuevo_automata
            aux = True
            break 
    
    if aux == False:
        automatas.append(nuevo_automata)
    
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

    #recorrido para validar la existencia de los estados
    for valor in automata.estados:
        if inicio.upper() == valor.nombre:
            validar1 = True
                    
    for valor in automata.estados:
        if fin.upper() == valor.nombre:
            validar2 = True

    #validacion de la existencia de los estados
    if validar1== False or validar2 == False:
        return"\nLos estados ingresados no se encuentran en el AFD\n"
    else:
        #recorrido para validar la existencia del terminal
        for valor in automata.terminales:
            if valor == terminal.lower():
                validar3 = True
                                
        #validacion del terminal
        if validar3 == False:
            return"\nEl terminal no se encuentra en el AFD\n"
        else:
            #recorrido para validar que no exista una transicion desde un estado con el mismo terminal 
            for tran in automata.transiciones:
                if tran.valor == terminal and inicio == tran.inicial:
                    validar = False

            #retorno de la validacion final
            if validar == True:
                transicion = Transicion(inicio.upper(),fin.upper(),terminal.lower())
                automata.transiciones.append(transicion)
                return"\nSe ha agregado la transicion\n"
            else:
                return"\nLos estados solo pueden tener una transicion con cada terminal\n"    

def crearEstado(automata,valor,aceptacion):

    #declaracion de la variable para validar su existencia
    aux = True

    #verificar si el valor del estado ingresado ya se encuentra en el AFD
    for validar in automata.estados:
        if validar.nombre == valor.upper():
            aux = False
    for validar in automata.terminales:
        if validar == valor.lower():
            aux = False

    #retorno de la verificacion del estado
    if aux == True:
        automata.estados.append(Estado(valor.upper(),aceptacion))
        return"\nSe ha agregrado el estado al AFD\n"
    else:
        return"\nEl estado ingresado ya se encuentra en el AFD\n"

def cambiarAceptacion(automata,noTerminal,estado):
    #variable para verificar si el estado existe
    aux = False

    #verificar si el estado existe y cambiarlo a estado de aceptacion
    for valor in automata.estados:
        if valor.nombre == noTerminal.upper():
            valor.aceptacion = estado
            aux = True
                
    #retorno de la validacion del estado de aceptacion
    if aux == True:
        return"\nSe a establecido el estado de aceptacion\n"
    else:
        return"\nEl estado ingresado no se encuentra en el AFD\n"

def crearTerminalAFD(automata,terminal):
    #declaracion de la variable para validar su existencia
    aux = True

    #verificar si el nombre del terminal ya se encuentra en el AFD
    for validar in automata.estados:
        if validar.nombre.lower() == terminal.lower():
            aux = False
    for validar in automata.terminales:
        if validar == terminal.lower():
            aux = False

    #retorno de la validacion del terminal
    if aux == True:
        automata.terminales.append(terminal.lower())
        return"\nSe ha agregrado el terminal al AFD\n"
    else:
        return"\nEl terminal ingresado ya se encuentra en el AFD\n"

def menuAFD(nuevo_automata): 
    #limpiar pantalla
    os.system("cls")

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

                #llamada al metodo para crear un estado
                print(crearEstado(nuevo_automata,estado,"0"))
            elif lectura == 2:
                #capturar el nombre del terminal
                terminal = input("\nIngrese el terminal: ")

                #llamada al metodo para crear terminales
                print(crearTerminalAFD(nuevo_automata,terminal))
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

                #llamada del metodo para cambiar la aceptacion del estado
                print(cambiarAceptacion(nuevo_automata,aceptacion,"1"))
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

                    #[fila][columna] len(matriz_transiciones) = filas , len(matriz_transiciones[0]) = columnas

                    for i in range(1,len(matriz_transiciones)):
                        for j in range(1,len(matriz_transiciones[0])):
                            if matriz_transiciones[i][j] != "":
                                if matriz_transiciones[i][j] != "-":
                                    #print("cabecera " +  matriz_transiciones[0][j]+" izquierda "+matriz_transiciones[i][0]+" interior "+ matriz_transiciones[i][j])
                                    modo1(nuevo_automata,matriz_transiciones[i][0],matriz_transiciones[i][j],matriz_transiciones[0][j])
                else:
                    print("\nIngrese unicamente el numero 1 o 2\n")
            elif lectura == 6:
                print(ayuda)
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def menuGramatica(nueva_gramatica):
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
            """
            for prod in nueva_gramatica.producciones:
                print(prod.inicio+" -> ",end="  ")
                for derecho in prod.ladoDerecho:
                    print(derecho.terminal+" "+derecho.siguiente,end="      \n      ")
                print("\n")
            """
            lectura = int(lectura)
            if lectura == 1:
                #captura del no terminal
                noTerminal = input("\nIngrese el nombre del no terminal: ")

                #invocando al metodo para la creacion del no terminal
                print(crearNoTerminalGramatica(nueva_gramatica,noTerminal))
            elif lectura == 2:
                #captura del no terminal
                terminal = input("\nIngrese el nombre del terminal: ")
                
                #llamando al metodo para crear el terminal
                print(crearTerminalGramatica(nueva_gramatica,terminal))
            elif lectura == 3:
                #captura del no terminal inicial
                inicial = input("\nIngrese el valor del no terminal inicial: ")

                #variable para validar la existencia del no terminal
                validar = False

                #recorrido para validar la existencia del no terminal
                for valor in nueva_gramatica.no_terminales:
                    if valor == inicial.upper():
                        validar = True
                
                #retorno de la validacion
                if validar == True:
                    nueva_gramatica.no_terminal_inicial = inicial.upper()
                    print("\nSe ha agregado el no terminal inicial\n")
                else:
                    print("\nEl no terminal ingresado no existe en la gramatica\n")
            elif lectura == 4:
                #captura de la produccion
                produccion = input("\nIngrese la produccion: ")
                
                crearProduccion(nueva_gramatica,produccion)
            elif lectura == 5:
                aux = False
                for valor in nueva_gramatica.producciones:
                    if valor.recursividad=="1":
                        aux = True

                if aux == True:
                    print("\nGramatica sin transformar:\n")
                    for valor in nueva_gramatica.transformacion:
                        print(valor.inicio+" ->",end=" ")
                        for derecha in valor.ladoDerecho:
                            if derecha.siguiente!="no" and derecha.siguiente!="epsilon": 
                                print(derecha.terminal+" "+derecha.siguiente,end="\n     ")
                            else:
                                print(derecha.terminal,end="\n     ")
                        print("\n")
                    print("\nGramatica transformada:\n")
                    for valor in nueva_gramatica.producciones:
                        print(valor.inicio+" ->",end=" ")

                        for derecha in valor.ladoDerecho:
                            if len(valor.inicio) >= 3: 
                                if derecha.siguiente!="no" and derecha.siguiente!="epsilon": 
                                    print(derecha.terminal+" "+derecha.siguiente,end="\n       ")
                                else:
                                    print(derecha.terminal,end="\n       ")
                            else:
                                if derecha.siguiente!="no" and derecha.siguiente!="epsilon": 
                                    print(derecha.terminal+" "+derecha.siguiente,end="\n     ")
                                else:
                                    print(derecha.terminal,end="\n     ")

                        print("\n")
                else:
                    print("\nNo hay recursividad\n")
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

def menuArchivos(repeticion):
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
                #capturando la ruta del archivo
                path_inicial = input("Ingrese la direccion del archivo .afd: ")
                
                #validando que la extension del archivo sea la correcta
                while True:
                    ruta,nombre = os.path.split(path_inicial)
                    division = nombre.split(".")
                    if division[1] == "afd":
                        break
                    else:
                        path_inicial = input ("\nIngrese la ruta del archivo .afd: ")

                #verificacion del nombre del automata
                for valor in automatas:
                    if valor.nombre == division[0]:
                        division[0] = division[0]+"-copia("+repeticion+")"
                        repeticion = repeticion + 1
                
                #creacion del automata
                nuevo_automata = Automata(division[0],[],[],"",[])
    
                #agregando el automata al arreglo
                automatas.append(nuevo_automata)

                #abriendo el archivo y obteniendo su contenido
                archivo_afd = open(path_inicial,"r")
                contenido = archivo_afd.read()

                #recorrido del archivo .afd
                for linea in contenido.split("\n"):

                    #division de la linea en EI,EF,Terminal;aceptacionEI,aceptacionEF
                    valor = linea.split(";")
                    transicion = valor[0].split(",")
                    aceptacion = valor[1].split(",")

                    #validar si el estado inicial ya se encuentra con un valor 
                    if nuevo_automata.estado_inicial == "":
                        nuevo_automata.estado_inicial = transicion[0].upper()
                    
                    #validar existencia del estado creandolo de ser necesario o cambiarle su estado de aceptacion
                    if aceptacion[0].lower() == "true": 
                        validar = crearEstado(nuevo_automata,transicion[0].upper(),"1")
                        if validar == "\nSe ha agregrado el estado al AFD\n":
                            pass
                        else:
                            cambiarAceptacion(nuevo_automata,transicion[0].upper(),"1")
                    else:
                        validar = crearEstado(nuevo_automata,transicion[0].upper(),"0")
                        if validar == "\nSe ha agregrado el estado al AFD\n":
                            pass
                        else:
                            cambiarAceptacion(nuevo_automata,transicion[0].upper(),"0")
                    
                    if aceptacion[1].lower() == "true": 
                        validar = crearEstado(nuevo_automata,transicion[1].upper(),"1")
                        if validar == "\nSe ha agregrado el estado al AFD\n":
                            pass
                        else:
                            cambiarAceptacion(nuevo_automata,transicion[1].upper(),"1")
                    else:
                        validar = crearEstado(nuevo_automata,transicion[1].upper(),"0")
                        if validar == "\nSe ha agregrado el estado al AFD\n":
                            pass
                        else: 
                            cambiarAceptacion(nuevo_automata,transicion[0].upper(),"0")

                    #agregando el terminal al automata
                    crearTerminalAFD(nuevo_automata,transicion[2].lower())

                    #creando la transicion y agregandola al terminal
                    modo1(nuevo_automata,transicion[0].upper(),transicion[1].upper(),transicion[2].upper())
                graphviz(nuevo_automata,division[0])
            elif lectura == 2:
                
                #capturando la ruta del archivo
                path_inicial = input("Ingrese la ruta del archivo .grm: ")

                #validando que la extension del archivo sea la correcta
                while True:
                    ruta,nombre = os.path.split(path_inicial)
                    division = nombre.split(".")
                    if division[1] == "grm":
                        break
                    else:
                        path_inicial = input ("\nIngrese la ruta del archivo .grm: ")
                
                #verificacion del nombre del automata
                for valor in gramaticas:
                    if valor.nombre == division[0]:
                        division[0] = division[0]+"-copia("+repeticion+")"
                        repeticion = repeticion + 1
                
                #creando la gramatica
                nueva_gramatica = Gramatica(division[0],[],[],"",[],[])

                #agregando la gramatica al arreglo 
                gramaticas.append(nueva_gramatica)

                #abriendo el archivo y obteniendo su contenido
                archivo_gramatica = open(path_inicial,"r")
                contenido = archivo_gramatica.read()
                
                #leyendo el contenido del archivo
                for linea in contenido.split("\n"):

                    #dividiendo la produccion en parte izquierda y derecha
                    produccion = linea.split(">")

                    #creando los no terminales y terminales de la gramatica
                    crearNoTerminalGramatica(nueva_gramatica,produccion[0])
                    
                    derecha = produccion[1].split(" ")
                    if len(derecha) == 1:
                        if derecha[0] == "epsilon":
                            pass
                        else:
                            crearTerminalGramatica(nueva_gramatica,derecha[0])
                    else:
                        if derecha[0].lower() == True or derecha[0].isdigit() == True:
                            crearTerminalGramatica(nueva_gramatica,derecha[0])
                            crearNoTerminalGramatica(nueva_gramatica,derecha[1])
                        elif derecha[1].lower() == True or derecha[1].isdigit() == True:
                            crearTerminalGramatica(nueva_gramatica,derecha[1])
                            crearNoTerminalGramatica(nueva_gramatica,derecha[0])
                    
                    #agregando la produccion inicial
                    if nueva_gramatica.no_terminal_inicial == "":
                        nueva_gramatica.no_terminal_inicial = produccion[0].upper()

                    #creando la produccion
                    crearProduccion(nueva_gramatica,linea)
            elif lectura == 3:
                #mostrando los nombres de los AFD disponibles
                print("\nAutomatas disponibles: ",end="\n  ")
                for it in range(0,len(automatas)):
                   print(str(it)+ ". "+ automatas[it].nombre,end="\n  ")
                
                #capturando el nombre del automata a guardar
                nombre = input("\nIngrese el nombre del automata a guardar: ")

                automata = None

                for valor in automatas:
                    if valor.nombre == nombre:
                        automata = valor

                transicionInicial = ""

                for transi in automata.transiciones:
                    if transi.inicial == automata.estado_inicial:
                        transicionInicial = transi.inicial+","+transi.final+","+transi.valor+";"
                        break

                for estado in automata.estados:
                    if transi.inicial == estado.nombre:
                        if estado.aceptacion == "1":
                            transicionInicial = transicionInicial+"true"+","
                            break
                        else:
                            transicionInicial = transicionInicial+"false"+","
                            break
                
                for estado in automata.estados:
                    if transi.final == estado.nombre:
                        if estado.aceptacion == "1":
                            transicionInicial = transicionInicial+"true\n"
                            break
                        else:
                            transicionInicial = transicionInicial+"false\n"
                            break

                path_afd = "C:\\Users\\chepe\\Desktop\\"+ automata.nombre +".afd"
                archivo_afd = open(path_afd,"w")

                validar = transi.inicial+","+transi.final+","+transi.valor

                for tran in automata.transiciones:
                    actual = tran.inicial+","+tran.final+","+tran.valor
                    if validar != actual:
                        transicionInicial = transicionInicial + tran.inicial+","+tran.final+","+tran.valor+";"

                        for estado in automata.estados:
                            if tran.inicial == estado.nombre:
                                if estado.aceptacion == "1":
                                    transicionInicial = transicionInicial+"true"+","
                                else:
                                    transicionInicial = transicionInicial+"false"+","
                
                        for estado in automata.estados:
                            if tran.final == estado.nombre:
                                if estado.aceptacion == "1":
                                    transicionInicial = transicionInicial+"true\n"
                                else:
                                    transicionInicial = transicionInicial+"false\n"
                archivo_afd.write(transicionInicial.rstrip("\n"))
                archivo_afd.close()
            elif lectura == 4:
                #mostrando los nombres de las gramaticas disponibles
                print("\nGramaticas disponibles: ",end="\n  ")
                for it in range(0,len(gramaticas)):
                   print(str(it)+ ". "+ gramaticas[it].nombre,end="\n  ")
                
                #capturando el nombre de la gramatica a guardar
                nombre = input("\nIngrese el nombre del automata a guardar: ")

                gramatica = None

                for valor in gramaticas:
                    if valor.nombre == nombre:
                        gramatica = valor

                contenido = ""

                for valor in gramatica.producciones:
                    if valor.inicio == gramatica.no_terminal_inicial:
                        for derecha in valor.ladoDerecho:
                            if contenido == "":
                                if derecha.siguiente != "epsilon" and derecha.siguiente!="no":
                                    contenido = valor.inicio+">"+derecha.terminal+" "+derecha.siguiente+"\n"
                                else:
                                    contenido = valor.inicio+">"+derecha.terminal+"\n"
                            else:
                                if derecha.siguiente != "epsilon" and derecha.siguiente!="no":
                                    contenido = contenido+valor.inicio+">"+derecha.terminal+" "+derecha.siguiente+"\n"
                                else:
                                    contenido = contenido+valor.inicio+">"+derecha.terminal+"\n"
                        break

                for valor in gramatica.producciones:
                    if valor.inicio!=gramatica.no_terminal_inicial:
                        for derecha in valor.ladoDerecho:
                            if derecha.siguiente!="epsilon" and derecha.siguiente!="no":
                                contenido = contenido+valor.inicio+">"+derecha.terminal+" "+derecha.siguiente+"\n"
                            else:
                                contenido = contenido+valor.inicio+">"+derecha.terminal+"\n"

                path_gramatica = "C:\\Users\\chepe\\Desktop\\"+ gramatica.nombre +".grm"
                archivo_gramatica = open(path_gramatica,"w")
                archivo_gramatica.write(contenido.rstrip("\n"))
                archivo_gramatica.close()
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
                print("\nListado de automatas existentes: ",end="\n  ")
                
                if len(automatas) == 0:
                    print("Aun no existen automatas en el sistema\n")
                else:
                    for valor in automatas:
                        print("- "+valor.nombre,end="\n  ")

                #captura del nombre del automata
                nombre = input("\nEscriba el nombre de un AFD del listado, o un nombre distinto para crear un nuevo AFD: ")
    
                automata = None

                #verificacion del nombre del automata
                for valor in automatas:
                    if valor.nombre == nombre:
                        automata = valor
                        break

                if automata == None:
                    #creacion del automata
                    nuevo_automata = Automata(nombre,[],[],"",[])
    
                    #agregando el automata al arreglo
                    automatas.append(nuevo_automata)
                    menuAFD(nuevo_automata)
                else:
                    menuAFD(automata)
            elif lectura == 2:
                print("\nListado de gramaticas existentes: ",end="\n  ")
                
                if len(gramaticas) == 0:
                    print("Aun no existen gramaticas en el sistema\n")
                else:
                    for valor in gramaticas:
                        print("- "+valor.nombre,end="\n  ")

                #captura del nombre del automata
                nombre = input("\nEscriba el nombre de una gramatica del listado, o un nombre distinto para crear una nueva gramatica: ")
    
                gramatica = None

                #verificacion del nombre del automata
                for valor in gramaticas:
                    if valor.nombre == nombre:
                        gramatica = valor
                        break

                if gramatica == None:
                    #creacion de la gramatica
                    nueva_gramatica = Gramatica(nombre,[],[],"",[],[])
    
                    #agregando el automata al arreglo
                    gramaticas.append(nueva_gramatica)
                    menuGramatica(nueva_gramatica)
                else:
                    menuGramatica(gramatica)
            elif lectura == 3:
                menuEvaluarCadenas()
            elif lectura == 4:
                menuReportes()
            elif lectura == 5:
                menuArchivos(repeticion)
            elif lectura == 0:
                print("\nHasta la proxima c:\n")
                exit(0)
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()