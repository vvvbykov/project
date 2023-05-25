while True:
    n = 2 # Ввести от 1 до 10
    choice = int(input('Угадай число от 1 до 10: '))
    if choice == n:
        print('Поздравляю, ты угадал число:', '>>>', n, '<<<')
    else:
        print('Попробуй еще раз')