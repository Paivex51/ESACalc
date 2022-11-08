import math, os

# nivel de optimizaçao pretendido 200% obtido ???

vO = ["+", "-", "*", "/", "%", "s", "p"]


def cE(v):
    return exit() if v == "exit" else v


def iC(v):
    v = v.split()
    return cE(v[0].lower()) if len(v) >= 1 else "inv"


def iF(v):
    try:
        return float(v)
    except ValueError:
        return False


def gN():
    v = iC(input("Number: "))
    return float(v) if iF(v) else gN()


def gO():
    v = iC(input("(+ - * / % s p): "))
    for x in vO:
        if v == x:
            return v
    return gO()


def c(n1, op, n2):
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
        case "s":
            return "Error" if n1 < 0 else math.sqrt(n1)
        case "p":
            return pow(n1, n2)


while 1:
    n1 = gN()
    op = gO()
    if op == vO[5]:
        r = c(n1, op, "")
        print("R: " + op + " of " + str(n1) + " = " + str(r))
    else:
        n2 = gN()
        r = c(n1, op, n2)
        print("R: " + str(n1) + " " + op + " " + str(n2) + " = " + str(r))
    cE(input("..."))
    os.system('cls')
