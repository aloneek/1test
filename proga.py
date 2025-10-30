import time
WHITE = '\u001b[47m'
RED = '\u001b[41m'
BLUE = '\u001b[44m'
JPNRED = '\x1B[48;5;160m'
END = '\u001b[0m'
C = '\u001b[0m'
line = ' ' * 4

def flag(o):
    height = lenght = o*3
    k = 0
    for i in range(height):
        if i < 10/100*height:
            print(f'{WHITE}{line*lenght}{END}')
        elif i < 33/100*height:
            print(f'{WHITE}{line*(lenght//3-k)}{JPNRED}{line*(lenght//3+2*k)}{WHITE}{line*(lenght//3-k)}{END}')
            k+=lenght//lenght
        elif i < 61/100*height:
            print(f'{WHITE}{line*(lenght//3-k)}{JPNRED}{line*(lenght//3+2*k)}{WHITE}{line*(lenght//3-k)}{END}')
        elif i < 86/100*height:
            print(f'{WHITE}{line*(lenght//3-k)}{JPNRED}{line*(lenght//3+2*k)}{WHITE}{line*(lenght//3-k)}{END}')
            k-=lenght//lenght
        else: print(f'{WHITE}{line*lenght}{END}')
    print('\n')

def flag2(o):
    height = lenght = o*3
    k = 0
    for i in range(height):
        if i < lenght*(2/10): print(f'{WHITE}{line*lenght}{END}')
        elif i <= lenght*(8/10): print(f'{WHITE}{line*(height//3)}{RED}{line*(lenght//3)}{WHITE}{line*(height//3)}{END}')
        else: print(f'{WHITE}{line*lenght}{END}')

def flag3(o):
    height = lenght = o
    for i in range(height):
        
        if i < height/3:
            print(f'{WHITE}{line*height}{END}')
        elif i < 2*height/3:
            print(f'{WHITE}{line*(lenght//3)}{JPNRED}{line*(lenght//3)}{WHITE}{line*(lenght//3)}{END}')
        else:
            print(f'{WHITE}{line*height}{END}')

def drawG(ID=231):
    print(f'\u001b[{22};{0}H')
    color = f'\x1B[48;5;{ID}m'
    height = 15
    center = height//2
    offset = height//1
    step = -1
    lenght = 1
    
    for i in range(height):
        print(f'{' '*offset}{color}{'  '*lenght}{C}{'  '*step}{color}{'  '*(step>0)}{C}{' '*(offset*2-4)}{color}{'  '*(i!=center)}{C}{'  '*step}{color}{'  '*(step>0)}{END}')
        if i < center:
            offset-=2
            step+=2
        else:
            offset+=2
            step-=2
    time.sleep(0.3)
    


def genfunc():
    step = 3
    height = 15
    k = 19
    j = 11
    print('y = 3x')
    print(f'Step is {step}')
    for i in range(height,-1,-1):
        print(f'{i*step}{'\u001b[10G'}{'---'*16}')
    print('\u001b[9G',end='')
    for i in range(16):
        if i < 10:
            print(' ',i,end='')
        else:
            print('',i,end='')
    print('\n')
    for x in range(height+1):
        print(f'\u001b[{k};{j}H/')
        k-=1
        j+=3
    print(f'\u001b[{22};{10}H')
        
def getfunction():
    plot_list = [[0 for i in range(10)] for i in range(10)]
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = i * 3

    step = round(abs(result[0] - result[9]) / 9, 2)
    
    print(f'func is y = 3x\nstep is {step}')
    for i in range(10):
        for j in range(10):
            if j == 0:
                plot_list[i][j] = step * (8-i) + step

    for i in range(9):
        for j in range(10):
            if abs(plot_list[i][0] - result[9 - j]) < step:
                for k in range(9):
                    if 8 - k == j:
                        plot_list[i][k+1] = 1

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(int(plot_list[i][j])) + '\t'
            if plot_list[i][j] == 0:
                line += '--'
            if plot_list[i][j] == 1:
                line += '!!'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')
    

def fil():
    file = open ('sequence.txt', 'r')
    list = []
    list2 = []
    for line in file:
        list.append(float(line))
        if float(line) != 5 and float(line) <= 0: list2.append(float(line)) 
    print(list[3:10])
    print(f'just list           {'-'*(len(list)//3)}\u001b[110G{len(list)}')
    print(f'list with condition {'-'*(len(list2)//3)}\u001b[110G{len(list2)}')





genfunc()

for ID in range(10):
    drawG(ID)
    print('\n')

flag(4)

getfunction()

fil()
print('\n')


