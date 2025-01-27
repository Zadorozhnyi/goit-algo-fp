import heapq

def dijkstra(graph, start):
    # Ініціалізація найкоротших шляхів та черги
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]  # (вага, вузол)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Якщо поточна відстань більша, ніж записана, пропускаємо
        if current_distance > shortest_paths[current_node]:
            continue
        
        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Створення зваженого графа
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Вивід результатів
print("Найкоротші шляхи від вершини", start_node, ":")
for node, distance in shortest_paths.items():
    print(f"Від {start_node} до {node}: {distance}")
