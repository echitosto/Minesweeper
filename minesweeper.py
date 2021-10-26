from cell import Cell
import random
import time
from os import system
class MineSweeper:
    def generate(self,n):

        # Creates board
        probability = 0
        self.mines = 10
        if(8 <= n <= 10):
            probability = 0.126
            self.mines = 10
        elif(10 < n <= 16):
            probability = 0.181
            self.mines = 40
        else:
            probability = 0.2
            self.mines = 99    
        for i in range(n):
            self.game.append([Cell()])
            for j in range(n-1):
                self.game[i] += [Cell()]
        
        # Fills with mines
        
        mine_counter = 0
        while mine_counter < self.mines:
            for i in range(n):
                for j in range(n):
                    if(random.random() < probability and mine_counter < self.mines and not self.game[i][j].is_mine):
                        self.game[i][j].is_mine = 1
                        mine_counter += 1

        self.shuffle(n)


        

        # Calculates neighbor mines
        for i in range(n):
            for j in range(n):
                # For each cell, we calculate the offset cells and check if they are mines
                for xoff in range(-1,2):
                    for yoff in range(-1,2):
                        i_n = i + xoff
                        j_n = j + yoff
                        if i_n > -1 and i_n < n and j_n > -1 and j_n < n and self.game[i_n][j_n].is_mine:
                            self.game[i][j].mines_surrounding += 1

    def __init__(self,dimensiones):
        self.game = []
        self.mines = 0
        self.dimensiones = dimensiones
        self.generate(self.dimensiones)
                
    
    def reveal_cell(self,fila,columna,cell):
        if cell.is_revealed:
            return
        if cell.is_mine:
            print("You lost! Better luck next time!")
            time.sleep(3)
            quit()
        if cell.mines_surrounding == 0:
            for fila_vecina in range(-1,2):
                for columna_vecina in range(-1,2):
                    new_fila = fila + fila_vecina
                    new_columna = columna + columna_vecina
                    #print(new_fila,new_columna)
                    if new_fila > -1 and new_fila < self.dimensiones and new_columna > -1 and new_columna < self.dimensiones:
                        cell.reveal()
                        self.reveal_cell(new_fila,new_columna,self.game[new_columna][new_fila])
        cell.reveal()
        return

    def show(self):
        system('cls')
        print("",end="    ")
        for i in range(len(self.game)):
            if i == len(self.game)-1:
                print(str(i+1) + " ")
            elif i >= 9:
                print(str(i+1) + "",end=" ")
            else:
                print(str(i+1) + " ",end=" ")
        for i in range(len(self.game)):
            if i >= 9:
                print(str(i+1) + "",end=" ")
            else:
                print(str(i+1) + " ",end=" ")
            print(self.game[i])

    def how_many_mines(self):
        return self.mines

    def gano(self):
        n = len(self.game)
        for fila in self.game:
            for celda in fila:
                if not celda.is_mine and not celda.is_revealed:
                    return False
        return True
    
    def shuffle(self,n):
        for i in range(n):
            random.shuffle(self.game)
        self.game = [[ self.game[row][col] for row in range(len(self.game))] for col in range(len(self.game))]
        for i in range(n):
            random.shuffle(self.game)
    def reveal_all(self):
        for fila in self.game:
            for celda in fila:
                celda.reveal()
        self.show()

