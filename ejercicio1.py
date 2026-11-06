print("===== BIENVENIDO AL REGISTRO DE CIENTIFICOS DEL INSTITUTO DE INVESTIGACION AVANZADA =====")

total_cientificos = int(input("Ingresa el total de cientificos a registrar: "))

while total_cientificos < 0:
    print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar: ")
    total_cientificos = int(input("Ingrese el total de cientificos a registrar: "))

    cant_principales = 0
    cant_asistentes = 0

    for i in range(1, total_cientificos + 1):
        print(f"\n ==== Registrando cientifico {i} de {total_cientificos}")

        id_Cientifico = input("Ingresa un ID de cientifico por favor:")
        if len(id_Cientifico) >= 12:
            print("Ingresaste un ID válido.....")
        else:
            print("La cantidad de caracteres debe ser al menos 12.")

    num_publicaciones = int(input("Ingresa el numero de publicaciones: "))
    while num_publicaciones < 0:
        print("Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
        num_publicaciones = int(input("Ingresa el numero de publicaciones: "))

        if num_publicaciones >= 12:
            print("Eres investigador principal.....")
            cant_principales += 1
        else:
            print("Eres investigador asistente....")
            cant_asistentes += 1


print("\n======================================================================================================================")
print(f"El Instituto cuenta con {cant_principales} Investigadores principales y {cant_asistentes} Investigadores asistentes.")
print("\n======================================================================================================================")
