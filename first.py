from random import *
n = randint(1, 100)
print(n)
print('Добро пожаловать в числовую угадайку')
def is_valid(text):
    return text.isdigit() and 100>= int(text) >= 1
again = 0
count = 0
while again != n:
    print('Введите число от 1 до 100')
    again = input()
    while not is_valid(again):
        print('А может быть все-таки введем целое число от 1 до 100?')
        again = input()
    count += 1
    again = int(again)
    if again > n: print('Ваше число больше загаданного, попробуйте еще разок')
    elif again < n: print('Ваше число меньше загаданного, попробуйте еще разок')
    else: print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print('Количество попыток:', count)
