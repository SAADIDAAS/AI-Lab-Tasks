import math

class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.minmax_value = None

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value if node.value is not None else node.name)
            return node.value if node.value is not None else 0

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.name)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.name)
            return value

root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]

n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]

n3.children = [Node('L1', 4), Node('L2', 7)]
n4.children = [Node('L3', 2), Node('L4', 5)]
n5.children = [Node('L5', 1), Node('L6', 8)]
n6.children = [Node('L7', 3), Node('L8', 6)]

env = Environment(root)
env.compute_minimax(root, 3, True)

print("Standard Minimax")
print("Computed Nodes Order:", env.computed_nodes)
print(f"Minimax values -> Root: {root.minmax_value}, N1: {n1.minmax_value}, N2: {n2.minmax_value}")
print(f"N3: {n3.minmax_value}, N4: {n4.minmax_value}, N5: {n5.minmax_value}, N6: {n6.minmax_value}")

for n in [root, n1, n2, n3, n4, n5, n6]: n.minmax_value = None
env_depth2 = Environment(root)
env_depth2.compute_minimax(root, 2, True)
print()
print("Depth-Limited Minimax (depth=2)")
print(f"Minimax values -> Root: {root.minmax_value}, N1: {n1.minmax_value}, N2: {n2.minmax_value}")
