while True:
    name, age = input(), int(input())
    if age <= 0:
        print('Ошибка, повторите ввод')
    elif age < 10:
        print('Привет, шкет', name)
    elif age <= 18:
        print('Как жизнь?', name)
    elif age < 100:
        print('Что желаете?', name)
    else:
        print(name, 'вы лжете - в наше время столько не живут...')
