total_equipos_disponibles = 0
equipos_disponibles = 25
total_equipos_liberados = 0
total_equipos_asignados = 0 
opcion = 0
while opcion == 0:
    try:
        print("===== ¡BIENVENIDO AL SISTEMA DE GESTION DE EQUIPOS DEL LABORATORIO CENTRAL DE INVESTIGACION! =======")
        print("1.- Equipos disponibles")
        print("2.- Asignar equipo")
        print("3.- Liberar equipo")
        print("4.- Historial de usos")
        print("5.- Salir")
        print("==========================================================================================================")
        opcion = int(input("Ingrese una opción: "))
        while opcion < 1 or opcion > 5:
            print("Ingrese una opción válida.")
            opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error, ingrese un valor entero válido.")
    match opcion:
        case 1:
            print("La cantidad de equipos disponibles es de", equipos_disponibles)
        case 2:
            equipo_asignar = int(input("Ingrese una cantidad de equipos a asignar: "))
            if equipo_asignar <= 0:
                print("Error, no debe ser menor a 0.")
                if equipo_asignar >= equipos_disponibles:
                    print("No debe superar la cantidad de equipos disponibles.")
            else:
                total_equipos_asignados = equipo_asignar
                print(total_equipos_asignados)
        case 3:
            liberar_equipos = int(input("Cantidad de equipos a liberar: "))
            if liberar_equipos >=20:
                print("Error, no debe superar la capacidad maxima del laboratorio.")
            else:
                total_equipos_liberados = liberar_equipos =- equipos_disponibles
                print(f"Se ha liberado la siguiente cantidad de equipos en total: {total_equipos_liberados}")
        case 4:
            print("====== HISTORIAL DE USOS =====")
            print(f"Equipos asignados en total: {total_equipos_asignados}")
            print(f"Equipos liberados en total: {total_equipos_liberados}")
            print(f"Equipos disponibles: {equipos_disponibles}")
            print("========================================================°")
        case 5:
            opcion = int(input("\nDesea salir 0)Si 1)No"))
            if opcion == 0:
                print("Saliendo del programa")
                break
            else:
                print("Continuamos con los registros.....")
                continue
        case _:
            print("Opcion inválida....")
            