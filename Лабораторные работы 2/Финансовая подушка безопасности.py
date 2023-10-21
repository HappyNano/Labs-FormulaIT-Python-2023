money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0
while True:
    dolg_1 = salary - spend
    money_capital += dolg_1
    spend *= 1.05
    if money_capital < 0:
        break
    count += 1


print("Количество месяцев, которое можно протянуть без долгов:", count)
