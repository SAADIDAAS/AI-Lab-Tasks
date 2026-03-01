graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {}, 'F': {}, 'G': {},
    'J': {}, 'K': {}, 'L': {}, 'M': {}
}

class GoalBasedAgent:

    def __init__(self, goals):
        self.goals = goals

    def best_first_search(self, start):

        frontier = [[0, start, [start]]]
        visited = []
        found_goals = []
        final_path = []

        print("\nBest First Search Starting...\n")

        while frontier and len(found_goals) < len(self.goals):

            frontier.sort()
            current = frontier.pop(0)

            cost = current[0]
            node = current[1]
            path = current[2]

            print("Visiting:", node)

            if node not in visited:
                visited.append(node)

                if node in self.goals and node not in found_goals:
                    print("Goal found:", node)
                    found_goals.append(node)
                    final_path = path

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        priority = graph[node][neighbour]
                        frontier.append([priority, neighbour, path + [neighbour]])

        if len(found_goals) == len(self.goals):
            print("\nAll Goals Visited!")
            print("Final Path Covering All Goals:", final_path)
        else:
            print("\nCould not reach all goals.")


class Environment:

    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.best_first_search(percept)


start_node = 'S'
goals = ['G', 'K', 'J']

agent = GoalBasedAgent(goals)
environment = Environment(graph)

run_agent(agent, environment, start_node)
