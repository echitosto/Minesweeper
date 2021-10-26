from clint.textui import colored
class Cell:
    def __init__(self,is_mine=0):
        self.is_mine = is_mine
        self.is_revealed = False
        self.mines_surrounding = 0
    
    def __repr__(self):
        if not self.is_revealed:
            return str(colored.cyan('■'))
        if self.mines_surrounding == 0 and not self.is_mine:
            return str(colored.blue("Ø"))
        elif self.is_mine:
            return str(colored.black("×"))
        return str(colored.green(str(self.mines_surrounding)))

    def reveal(self):
        self.is_revealed = True