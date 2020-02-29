import os
from field import Field

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def flip(field, index):
    if field.list[index] == '.':
        pass
    else:
        field.list[index] = '1' if field.list[index] == '0' else '0'

def run():
    msg = ''
    field = Field(int(input('enter field size: ')))
    playing = True
    while playing:
        # game state check
        if not '1' in field.list and not '0' in field.list:
            msg = f'Victory! on field size {len(field.list)}'
            playing = False
        elif not '1' in field.list:
            msg = f'Defeat! remaining: {field.get_remaining()}'
            playing = False
        
        
        # output
        clear()
        print(f': {msg}')
        msg = ''
        print(f'field: \033[7m{field.to_string()}\033[0m')
        print(f'moves: {" ".join(field.get_moves())}')

        # input
        if playing:
            i = input('> ')
            if not i or i == ' ' or not i in field.get_moves():
                move = False
                msg = 'invalid input'
            else: 
                move = True
            
        if move:
            i = int(i)
            
            field.list[i] = '.'
            if i + 1 == len(field.list):
                flip(field, i - 1)
            elif i == 0:
                flip(field, i + 1)
            else:
                flip(field, i + 1)
                flip(field, i - 1)
