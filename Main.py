import os

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

def menuAFD():
    #limpiar pantalla y mostrar menu
    os.system("cls")
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
                pass
            elif lectura == 0:
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
                pass
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
                pass
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
                pass
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
