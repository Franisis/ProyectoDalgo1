import sys
import time

"""
FRANCISCO JOSÉ GUZMÁN ÁNGEL
202012332
"""

def reorganizar_torres(n,torres):    
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


def main():
    if len(sys.argv)<2:
        print("ERROR: Número incorrecto de paramétros para ejecutar el programa")
        pass
    entrada= sys.argv[1]
    salida = sys.argv[2]
    with open(entrada, 'r') as archive:
        with open(salida,'w') as output:

            m=archive.readline()
            m=int(m)
            for linea in archive:
                linea=linea.replace('\n','').split(" ")
                n=int(linea[0])
                del linea[0]
                linea=[int(i) for i in linea]
                start=time.time()
                output.write(str(reorganizar_torres(n, linea))+"\n")
                end=time.time()
                print(linea)
                print(end-start)
main()