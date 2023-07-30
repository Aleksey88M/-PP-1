""" 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на 
единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """

number = int(input('Введите число: '))
if number == 2:
    result = 'Простое'
elif not number%2:
    result = 'Составное'
else:
    for dev in range(3, number//2+1, 2):
        if not number%dev:
            result = 'Составное'
            break
    else:
        result = 'Простое'
print(result)