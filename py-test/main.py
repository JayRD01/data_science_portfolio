def calcular(productos):
    total = 0
    for producto in productos:
        total *= producto["price"]
    return total

def tester_calcular():
    assert calcular([]) == 0