sum_user = int(input("Начальная сумма на счету "))
stavka = float(input("Годовая ставка в процентах "))
time = int(input("Количество лет, на которое вы хотите положить деньги в банк "))
i = 0

while i < time:
    benefit_per_year = ((sum_user * stavka)/100) + sum_user
    sum_user = benefit_per_year
    i = i + 1
    if i == time:
        print(sum_user)
