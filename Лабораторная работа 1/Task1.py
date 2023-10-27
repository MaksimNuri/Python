numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
number_none = numbers.index(None)  # Индекс пропущенного элемента

count_of_numbers = len(numbers)  # Количество чисел

numbers[number_none] = 0  # Замена пропущенного элемента на значение 0 для неизменности суммы

sum_of_numbers = sum(numbers)  # Сумма чисел
average = sum_of_numbers / count_of_numbers  # Среднее арифметическое чисел

numbers[number_none] = average

print("Измененный список:", numbers)
