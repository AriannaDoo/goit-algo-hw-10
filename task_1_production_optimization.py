import pulp

# Створення моделі лінійного програмування
model = pulp.LpProblem("Drink_Production_Optimization", pulp.LpMaximize)

# Змінні — кількість вироблених продуктів
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("Juice", lowBound=0, cat="Integer")

# Цільова функція — максимізація загальної кількості напоїв
model += lemonade + juice, "Maximize_total_drinks"

# Обмеження ресурсів
model += 2 * lemonade + 1 * juice <= 100   # Вода
model += 1 * lemonade <= 50                # Цукор
model += 1 * lemonade <= 30                # Лимонний сік
model += 2 * juice <= 40                   # Фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Лимонад:", lemonade.varValue)
print("Фруктовий сік:", juice.varValue)
print("Загальна кількість:", lemonade.varValue + juice.varValue)
