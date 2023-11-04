money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

total_of_month = 0
total_of_money = money_capital + salary
difference = spend - salary

while total_of_money > difference:
    total_of_month += 1
    difference = spend - salary
    total_of_money = money_capital + salary - spend
    money_capital += (salary - spend)
    spend *= 1.05

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", total_of_month)
