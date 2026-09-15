usuario_correcto = "usuario"    #
contraseña_correcta = "1234"    # Puedes modificar estos valores
intentos = 3                    #

while intentos > 0:

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"Datos incorrectos. Intentos restantes: {intentos}")

if intentos == 0:
    print("Demasiados intentos. Acceso bloqueado.")

else:

    while True:

        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Calculadora")
        print("2. Bloc de notas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")


        if opcion == "1":

            print("\n===== CALCULADORA =====")

            num1 = float(input("Primer número: "))
            operador = input("Operación (+, -, *, /): ")
            num2 = float(input("Segundo número: "))

            if operador == "+":
                resultado = num1 + num2

            elif operador == "-":
                resultado = num1 - num2

            elif operador == "*":
                resultado = num1 * num2

            elif operador == "/":

                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("No puedes dividir entre 0.")
                    continue

            else:
                print("Operador no válido.")
                continue

            print(f"Resultado: {resultado}")


        elif opcion == "2":

            print("\n===== BLOC DE NOTAS =====")

            nota = input("Escribe tu nota: ")

            print("\n - Tu nota:")
            print(nota)


        elif opcion == "3":

            print("Cerrando programa...")
            break

        else:
            print("Opción no válida.")