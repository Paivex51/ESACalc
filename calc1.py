import math, os, sys

# nivel de optimizaçao pretendido 100% obtido ???
# escreva "exit" em qualquer momento para sair
# nao acha que esta optimizado o suficiente ?? :( -> ver calc0.py por favor XD

# sys.set_int_max_str_digits(999999999) #se quiser numeros MUITO grandes :)
validOps = ["+", "-", "*", "/", "%", "sqrt", "pwr"]  # array para poder efetuar mudanças futuras se quiser :)


def start():
    end = 0
    while end != 1:
        n1 = getNumber()
        op = getOperator()
        if op == validOps[5]:
            result = justDoIt(n1, op, "")
            print("Result: " + op + " of " + str(n1) + " = " + str(result))
        else:
            n2 = getNumber()
            result = justDoIt(n1, op, n2)
            print("Result: " + str(n1) + " " + op + " " + str(n2) + " = " + str(result))
        checkExit(input("..."))
        os.system('cls')


def checkExit(var):
    return exit() if var == "exit" else var


def inputCheck(var):
    var = var.split()
    return checkExit(var[0].lower()) if len(var) >= 1 else "invalid"


def isFloat(var):
    try:
        return float(var)
    except ValueError:
        return False


def getNumber():
    var = inputCheck(input("Number: "))
    return float(var) if isFloat(var) else getNumber()


def getOperator():
    var = inputCheck(input("Operator (+ - * / % sqrt pwr): "))
    for x in validOps:
        if var == x:
            return var
    return getOperator()


def justDoIt(n1, op, n2):
    match op:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2
        case "%":
            return (n2 * n1) / 100
        case "sqrt":
            return "Error" if n1 < 0 else math.sqrt(n1)
        case "pwr":
            return pow(n1, n2)
        case _:
            return "¯\_(ツ)_/¯"  # se chegar aqui ta de parabens pq eu n consegui


start()
