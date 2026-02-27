while True:

    a = float(input("Digite el primer numero: "))
    b = float(input("Digite el segundo numero: "))

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division real")
    print("5. Division entera")
    print("6. Modulo")
    print("7. Salir")

    op = int(input("Seleccione una opcion: "))

    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    elif op == 4:
        print(a / b)
    elif op == 5:
        print(a // b)
    elif op == 6:
        print(a % b)
    elif op == 7:
        break