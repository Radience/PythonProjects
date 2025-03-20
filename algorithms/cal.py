import random
import os

point = True

while point:
    choice = random.randint(1,4)
    a = random.randint(0,100)
    b = random.randint(1,100)
    ans = 0
    match(choice):
        case 1: #сложение
            ans = a + b
            print(f'\n{a} + {b} = ')
        case 2: #минус
            ans = a - b
            print(f'\n{a} - {b} = ')
        case 3: #умножение
            ans = a * b
            print(f'\n{a} * {b} = ')
        case 4: #деление
            a = random.randint(0,1000)
            b = random.randint(1,10)
            ans = a / b
            print(f'\n{a} / {b} = ')

    answer = input('\nВведите ответ: ')
    print(f'\nОтвет: {ans}')
    if(answer == 'stop'):
        point = False
    elif float(answer) == float('{:.2f}'.format(ans)):
        print('\nВерно')
    else:
        print('\nНе верно!')

    input('\nНажмите, чтобы продолжить')
    os.system('cls' if os.name == 'nt' else 'clear')
