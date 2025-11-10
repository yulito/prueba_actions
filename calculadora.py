# ejemplo para aprender github actions
a = 3
b = 8

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def menu():
    print("****************")
    print("----- Menu -----")
    print("1) suma")
    print("2) resta")
    print("3) multiplicacion")
    print("4) division")
    print("5) SALIR")
    print("****************")
    option = input(">")
    return option

def inicio():        
    while True:
        op = menu()
        if op == "1":
            print(str(suma(a,b)))
        elif op == "2":
            print(str(resta(a,b)))
        elif op == 3:
            print(str(multiplicacion(a,b)))
        elif op == "4":
            print(str(division(a,b)))
        elif op == "5":
            break
        else:
            print("")
            print("+++ ERROR +++\n")

inicio()