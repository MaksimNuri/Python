# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44  # Объем дискеты в мегабайтах.
memory_in_bytes = memory * 1024 * 1024  # Объем дискеты в байтах
pages = 100
lines = 50
symbols = 25
memory_of_one_symbol = 4  # Байты

memory_of_one_book = pages * lines * symbols * memory_of_one_symbol  # Объем одной книги в байтах

number_of_books = memory_in_bytes // memory_of_one_book

print("Количество книг, помещающихся на дискету:", round(number_of_books))

