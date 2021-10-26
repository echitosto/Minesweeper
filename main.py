from minesweeper import MineSweeper
from cell import Cell
import time
from clint.textui import colored
LIMITE = range(8,17)
def pedir_dimensiones():
    print("\n")
    return input("Para comenzar, seleccione unas dimensiones (>= 8 y <= 16): ")

def pedir_accion():
    print("\n")
    return input("Seleccione una casilla para revelar (Formato: fila columna)")

def main():
    print(str(colored.yellow("====================================")))
    print(str(colored.yellow("||                                ||")))
    print(str(colored.yellow("||    Bienvenido a Buscaminas     ||")))
    print(str(colored.yellow("||                                ||")))
    print(str(colored.yellow("====================================")))
    game = True
    while game:
        dimensiones = pedir_dimensiones()
        try: 
            if int(dimensiones) not in LIMITE:
                continue
        except:
            continue
        dimensiones = int(dimensiones)
        ms = MineSweeper(dimensiones)
        while True:
            if(ms.gano()):
                ms.reveal_all()
                print("You won! yaay")
                time.sleep(5)
                quit()
            ms.show()
            casilla = pedir_accion()
            try:
                columna = int(casilla.split()[0])
                fila = int(casilla.split()[1])
                if len(casilla.split()) != 2 or columna > dimensiones or columna < 1 or fila > dimensiones or fila < 1:
                    continue
            except:
                continue
            columna,fila = casilla.split()
            columna = int(columna)
            fila = int(fila)
            casilla = ms.game[columna-1][fila-1]
            ms.reveal_cell(fila-1,columna-1,casilla)
            
           
main()