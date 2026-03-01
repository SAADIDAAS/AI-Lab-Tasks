graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def uniform_cost_search(self, start):

        frontier = [[0, start, [start]]]
        visited = []

        while frontier:
            frontier.sort()
            current = frontier.pop(0)

            cost = current[0]
            node = current[1]
            path = current[2]

            print("Visiting:", node, "Cost:", cost)

            if node == self.goal:
                print("Goal found!")
                print("Least Cost Path:", path)
                print("Total Cost:", cost)
                return

            if node not in visited:
                visited.append(node)

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        total_cost = cost + graph[node][neighbour]
                        frontier.append([total_cost, neighbour, path + [neighbour]])

        print("Goal not found.")


start_node = 'S'
goal_node = 'G'

agent = GoalBasedAgent(goal_node)
agent.uniform_cost_search(start_node)
