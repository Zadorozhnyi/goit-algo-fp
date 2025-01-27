import random
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_dice_simulation(num_rolls=100000):
    sums_count = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильника для кожної можливої суми
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1
    
    probabilities = {key: (value / num_rolls) * 100 for key, value in sums_count.items()}
    
    return sums_count, probabilities

# Запускаємо симуляцію
num_rolls = 100000
sums_count, probabilities = monte_carlo_dice_simulation(num_rolls)

# Побудова таблиці результатів
data = pd.DataFrame({"Сума": list(probabilities.keys()), "Ймовірність (%)": list(probabilities.values())})
print(data)

def plot_results(probabilities):
    plt.figure(figsize=(8, 5))
    plt.bar(probabilities.keys(), probabilities.values(), color='blue', alpha=0.7)
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків (Монте-Карло)")
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Побудова графіку
plot_results(probabilities)

# Теоретичні ймовірності для порівняння
theoretical_probabilities = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
                             7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}

diff = {key: abs(probabilities[key] - theoretical_probabilities[key]) for key in probabilities}

diff_data = pd.DataFrame({"Сума": list(diff.keys()), "Різниця (%)": list(diff.values())})
print("Порівняння з теоретичними значеннями:")
print(diff_data)
