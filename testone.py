import random

print('Добро пожаловать в числовую угадайку!')

def is_value(s):
    if s.isdigit() and 1 < int(s) < 101:
        return True
    else:
        return False
random_num = random.randint(1, 101)

while True:
    stroka = input('Введите число: ')

    if not is_value(stroka):
        print('Введите чисЛО в диапазаоне от 1 до 101')
        continue


    if is_value(stroka):
        stroka = int(stroka)


        if stroka == random_num:
            print('Вы угадали!')
            break

        elif stroka > random_num:
            print('Введите число поменьше')

        elif stroka < random_num:
            print('Введите число побольше')

print('До новых встреч в числовой угадайке!')
