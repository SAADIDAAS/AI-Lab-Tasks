n5.children = [Node('L5', 2), Node('L6', 1)]

env_ab_mod = AlphaBetaEnvironment(root)
env_ab_mod.alpha_beta_search(root, 3, -math.inf, math.inf, True)

print("Modified Tree Alpha-Beta Pruning")
print(f"Updated Minimax values -> Root: {root.minmax_value}, N1: {n1.minmax_value}, N2: {n2.minmax_value}")
print("Nodes Pruned:", env_ab_mod.pruned_nodes)
print("Optimal path for Max: Root -> N1 -> N3 -> L2")
