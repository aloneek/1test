from itertools import *

WHITE = '\u001b[47m'
RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
line = ' ' * 4

height = lenght = 9
for i in range(height):
    if i < height//3 :print(f'{WHITE}{line*lenght}{END}')
    elif i < height*2//3 : print(f'{BLUE}{line*lenght}{END}')
    else: print(f'{RED}{line*lenght}{END}')

