graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def depth_limited_search(self, node, goal, depth, path):
        print("Visiting:", node, "Depth:", depth)
        path.append(node)

        if node == goal:
            return True

        if depth <= 0:
            path.pop()
            return False

        for neighbour in graph[node]:
            if self.depth_limited_search(neighbour, goal, depth - 1, path):
                return True

        path.pop()
        return False

    def iterative_deepening(self, start, max_depth):
        for depth in range(max_depth + 1):
            print("\nDepth Level:", depth)
            path = []
            if self.depth_limited_search(start, self.goal, depth, path):
                print("Goal found!")
                print("Final Path:", path)
                return
        print("Goal not found.")


start_node = 'A'
goal_node = 'G'

agent = GoalBasedAgent(goal_node)
agent.iterative_deepening(start_node, 5)
