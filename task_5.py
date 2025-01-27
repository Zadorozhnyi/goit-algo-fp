import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

def generate_color_gradient(n):
    colors = []
    for i in range(n):
        factor = int(255 * (i / (n - 1))) if n > 1 else 255
        colors.append(f"#{factor:02X}96F0")  # Від темного до світлого синього
    return colors

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def build_heap_tree(heap):
    if not heap:
        return None
    
    nodes = [Node(val) for val in heap]
    
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]  # Повертаємо кореневий вузол купи у вигляді дерева


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def bfs_traversal(tree_root):
    if not tree_root:
        return []
    
    queue = deque([tree_root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_traversal(tree_root):
    if not tree_root:
        return []
    
    stack = [tree_root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def visualize_traversal(tree_root, traversal_order, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = generate_color_gradient(len(traversal_order))
    for i, node in enumerate(traversal_order):
        node.color = colors[i]
        
        # Update visualization at each step
        node_colors = [tree.nodes[n.id]['color'] if n in traversal_order[:i+1] else "#FFFFFF" for n in traversal_order]
        labels = {n.id: n.val for n in traversal_order}
        
        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
        plt.title(title)
        plt.show()
        time.sleep(0.5)  # Pause to visualize step-by-step

# Створення та візуалізація бінарної купи у вигляді дерева
heap = [3, 1, 6, 5, 2, 8, 10]
heapq.heapify(heap)
tree_root = build_heap_tree(heap)

# Візуалізація обходів
bfs_order = bfs_traversal(tree_root)
dfs_order = dfs_traversal(tree_root)
visualize_traversal(tree_root, bfs_order, "Обхід у ширину (BFS)")
visualize_traversal(tree_root, dfs_order, "Обхід у глибину (DFS)")
