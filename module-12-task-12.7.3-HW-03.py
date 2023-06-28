per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Ввод суммы money с клавиатуры
money = float(input("Введите сумму, которую планируете положить под проценты: "))

# Вычисление накопленных средств за год вклада в каждом банке
deposit = [round(money * percent / 100, 2) for percent in per_cent.values()]

for bank, amount in zip(per_cent.keys(), deposit):
    print(f"Сумма вклада в банке {bank}: {amount}")

# Поиск максимального значения в списке deposit
max_deposit = max(deposit)

# Вывод максимального значения на экран
print("Максимальная сумма, которую вы можете заработать:", max_deposit)
