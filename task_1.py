money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
current_spend = spend
while money_capital + salary >= current_spend:
    money_capital = money_capital + salary - current_spend
    months += 1
    current_spend *= increase + 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
