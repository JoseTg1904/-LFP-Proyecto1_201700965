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
    pass

def menuPrincipal():
    #limpiar pantalla y mostrar menu
    os.system("cls")
    print(" ")
    print("------------Menu Principal------------")
    print("|                                    |")
    print("| 1. Crear AFD                       |")
    print("| 2. Crear Gramatica                 |")
    print("| 3. Evaluar cadenas                 |")
    print("| 4. Reportes                        |")
    print("| 5. Cargar archivo de entrada       |")
    print("| 0. Salir                           |")
    print("|                                    |")
    print("--------------------------------------")
    print(" ")

    #lectura del teclado para direccionar a otro menu
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                menuAFD()
            elif lectura == 2:
                pass
            elif lectura == 3:
                pass
            elif lectura == 4:
                pass
            elif lectura == 5:
                pass
            elif lectura == 0:
                print("\nHasta la proxima c:\n")
                exit(0)
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()
