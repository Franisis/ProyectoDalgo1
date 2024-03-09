def reorganizar_torres(torres):
    n = len(torres)
    cambios = True
    movimientos = 0
    while cambios:
        cambios = False
        for i in range(n - 1):
            if torres[i] < torres[i + 1]:
                torres[i] += 1
                torres[i + 1] -= 1
                cambios = True
                movimientos += 1
    return movimientos


lista="36 38 14 7 7 7 2 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0".split(" ")
lista = [int(i) for i in lista]
print(reorganizar_torres(lista))
print(lista)