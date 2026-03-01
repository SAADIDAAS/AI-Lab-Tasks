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

    def act(self, start, depth_limit):
        path = []
        print("\nRunning Depth-Limited Search with depth =", depth_limit)
        found = self.depth_limited_search(start, self.goal, depth_limit, path)

        if found:
            print("Goal found!")
            print("Path:", path)
        else:
            print("Goal not found within depth limit.")


start_node = 'A'
goal_node = 'H'

agent = GoalBasedAgent(goal_node)

agent.act(start_node, 2)
agent.act(start_node, 3)
