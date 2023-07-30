"""  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)  """

import random
ATTEMPTS = 10
guess_number = random.randint(1, 1000)
count = 1
while count <= ATTEMPTS:
    my_number = int(input('Введите число: '))
    if my_number < guess_number:
        print('Больше')
    elif my_number > guess_number:
        print('Меньше')
    else:
        print(f'Ты укадал с {count} раза')
        break
    count += 1 
else:
    print(f'Извини, ты не угадал даже за {ATTEMPTS} попыток')