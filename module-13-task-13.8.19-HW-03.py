# Запрашиваем количество билетов
num_tickets = int(input("Введите количество билетов: "))

# Генерируем список стоимостей для каждого билета
ticket_prices = []
for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i + 1}: "))
    price = 0 if age < 18 else (1390 if age > 25 else 990)
    ticket_prices.append(price)

# Проверяем, получает ли человек скидку
discount = 0.9 if num_tickets > 3 else 1.0

# Вычисляем общую стоимость билетов с учетом скидки
total_cost = sum(ticket_prices) * discount

# Выводим общую стоимость
print("Общая стоимость билетов:", total_cost, "руб.")
