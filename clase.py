numero1 = 2
numero2 = 2
operacion = "suma"


def calculadora(numero1, numero2, operacion):

    if operacion == "suma":
        resultado = numero1 + numero2
    if operacion == "resta":
        resultado = numero1 - numero2
    if operacion == "multipliacion":
        resultado = numero1 * numero2
    if operacion == "division":
        resultado = numero1 / numero2

    return resultado


calculadora(numero1, numero2, operacion)
