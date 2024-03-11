import sys
import time

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
    
    1
    return movimientos


def main():
    if len(sys.argv)<2:
        print("ERROR: Número incorrecto de paramétros para ejecutar el programa")
        pass
    entrada= sys.argv[1]
    salida = sys.argv[2]
    with open(entrada, 'r') as archive:
        with open(salida,'w') as output:

            chmbadas=archive.readline()
            chmbadas=int(chmbadas)
            for linea in archive:
                linea=linea.replace('\n','').split(" ")
                chmbaditas=int(linea[0])
                del linea[0]
                linea=[int(i) for i in linea]
                output.write(str(reorganizar_torres(chmbaditas, linea))+"\n")
                print(linea)
            

main()