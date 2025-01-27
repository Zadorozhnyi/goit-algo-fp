def greedy_algorithm(items, budget):
    # Сортуємо елементи за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_calories = 0
    total_cost = 0
    
    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.keys())
    costs = [items[item]['cost'] for item in item_list]
    calories = [items[item]['calories'] for item in item_list]
    n = len(items)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_list[i - 1])
            w -= costs[i - 1]
    
    selected_items.reverse()
    return selected_items, dp[n][budget]


# Вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 60

# Виконання алгоритмів
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

# Вивід результатів
print("Жадібний алгоритм: Вибрані страви -", greedy_result[0], "| Загальна калорійність -", greedy_result[1])
print("Динамічне програмування: Вибрані страви -", dp_result[0], "| Загальна калорійність -", dp_result[1])
