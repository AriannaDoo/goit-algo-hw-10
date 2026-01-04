import random
import scipy.integrate as spi

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

def monte_carlo_integral(func, a, b, n=100_000):
    max_y = func(b)
    count = 0

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= func(x):
            count += 1

    rectangle_area = (b - a) * max_y
    return (count / n) * rectangle_area

# Метод Монте-Карло
mc_result = monte_carlo_integral(f, a, b)

# Аналітичне обчислення через quad
quad_result, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {mc_result}")
print(f"Аналітичне (quad): {quad_result}")
print(f"Абсолютна різниця: {abs(mc_result - quad_result)}")
