class AlphaBetaEnvironment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
        self.pruned_nodes = []

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value if node.value is not None else node.name)
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    self.pruned_nodes.append(child.name if child.name else child.value)
                    break
            node.minmax_value = value
            self.computed_nodes.append(node.name)
            return value
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    self.pruned_nodes.append(child.name if child.name else child.value)
                    break
            node.minmax_value = value
            self.computed_nodes.append(node.name)
            return value

env_ab = AlphaBetaEnvironment(root)
env_ab.alpha_beta_search(root, 3, -math.inf, math.inf, True)

print("Alpha-Beta Pruning")
print(f"Minimax value for root: {root.minmax_value}")
print("Nodes Pruned:", env_ab.pruned_nodes)
