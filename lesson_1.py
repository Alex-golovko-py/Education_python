#Задание номер 1
#Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
#Напишите код, который проверяет какая из этих строк длиннее.
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print(len(phrase_1))
print(len(phrase_2))
if len(phrase_1) < len(phrase_2):
    print('Результат Задания 1')
    print('Вторая строка длинее на:', len(phrase_2), '+' 'символов')
else:
    print('Результат Задания 1')
    print('Первая строка длинее', 'на', len(phrase_1) - len(phrase_2), 'символов')

#Задание  номер 2
#Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.
year = int(input('Введите год: '))
print('Весокосный год') if (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0) else print('Это обычный год')

#Задание номер 3
#Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.
month = str(input('Укажите месяц вашего рождения: ')).lower()
birth_day = int(input('Укажите дату вашего рождения: '))
if (birth_day >=21 and birth_day<=31 and month == 'март') or (birth_day >=1 and birth_day <= 20 and  month == 'апрель'):
    print("Ваш знак зодиака - Овен")
elif (birth_day >=21 and birth_day<=30 and month == 'апрель') or (birth_day >=1 and birth_day <= 21 and  month == 'май'):
    print("Ваш знак зодиака - Телец")
elif (birth_day >=22 and birth_day<=31 and month == 'май') or (birth_day >=1 and birth_day <= 21 and  month == 'июнь'):
    print("Ваш знак зодиака - Близнецы")
elif (birth_day >=22 and birth_day<=30 and month == 'июнь') or (birth_day >=1 and birth_day <= 22 and  month == 'июль'):
    print("Ваш знак зодиака - Рак")
elif (birth_day >=23 and birth_day<=31 and month == 'июль') or (birth_day >=1 and birth_day <= 21 and  month == 'август'):
    print("Ваш знак зодиака - Лев")
elif (birth_day >=22 and birth_day<=31 and month == 'август') or (birth_day >=1 and birth_day <= 23 and  month == 'сентябрь'):
    print("Ваш знак зодиака - Дева")
elif (birth_day >=24 and birth_day<=30 and month == 'сентябрь') or (birth_day >=1 and birth_day <= 23 and  month == 'октябрь'):
    print("Ваш знак зодиака - Весы")
elif (birth_day >=24 and birth_day<=31 and month == 'октябрь') or (birth_day >=1 and birth_day <= 22 and  month == 'ноябрь'):
    print("Ваш знак зодиака - Скорпион")
elif (birth_day >=23 and birth_day<=30 and month == 'ноябрь') or (birth_day >=1 and birth_day <= 22 and  month == 'декабрь'):
    print("Ваш знак зодиака - Стрелец")
elif (birth_day >=21 and birth_day<=31 and month == 'январь') or (birth_day >=1 and birth_day <= 19 and  month == 'февраль'):
    print("Ваш знак зодиака - Водолей")
elif (birth_day >=20 and birth_day<=28 and month == 'февраль') or (birth_day >=1 and birth_day <= 20 and  month == 'март'):
    print("Ваш знак зодиака - Водолей")
else:
    print('Некорректно введены данные месяца или даты рождения')

#Задание номер 4
#Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
#Используйте следующие правила:
#если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
#если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
#если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
#во всех остальных случаях выводите "Коробка №3".
width = int(input('Укажите ширину изделия: '))
length = int(input('Укажите длину изделия: '))
height = int(input('Укажите высоту изделия: '))

if width <= 15 and length <= 15 and height <= 15 :
    print('Коробка №1')
elif width >= 200 or length >= 200 or  height >= 200:
  print('Упаковка для лыж')
elif (width > 15 and width < 50) or (length > 15 and length < 50) or  (height > 15 and height < 50):
  print('Коробка №2')
else:
    print('Коробка №3')
#Задание номер 5
#Дана переменная, в которой хранится шестизначное число (номер проездного билета).
#Напишите программу, которая будет определять, является ли данный билет "счастливым".
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.
lucky_tiket = input('Введите номер билета: ')
if int(lucky_tiket[0]) + int(lucky_tiket[1]) + int(lucky_tiket[2]) == int(lucky_tiket[3]) + int(lucky_tiket[4]) + int(lucky_tiket[5]):
  print ('Счастливый билет - ', lucky_tiket)
else:
  print ('Не счастливый билет - ', lucky_tiket)

#Задание номер 6
#доделать