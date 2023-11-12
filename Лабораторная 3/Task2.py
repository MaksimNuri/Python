# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=","):
    str1 = str1.split(delimiter)
    str2 = str2.split(delimiter)
    same = list(set(str1).intersection(str2))

    same.sort()
    return same


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))


# TODO Провеьте работу функции с разделителем отличным от запятой
