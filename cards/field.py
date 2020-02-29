from random import randrange

class Field:
    def __init__(self, size):
        self.list = []
        for _ in range(size):
            self.list.append(str(randrange(2)))
    
    def get_moves(self):
        self.moves = []
        for index, v in enumerate(self.list):
            if v == '1':
                self.moves.append(str(index))
        return self.moves
    
    def to_array(self):
        return self.list
    
    def to_string(self):
        return ''.join(self.list)
