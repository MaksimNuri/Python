list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_number_of_players = len(list_players)  # Общее количество игроков
middle_index = total_number_of_players // 2  # Индекс середины

first_team = list_players[:middle_index]  # Первая команда
second_team = list_players[middle_index:]  # Вторая команда

print(first_team)
print(second_team)

# TODO Разделите участников на две команды
