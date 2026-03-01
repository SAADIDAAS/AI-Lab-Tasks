import random

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}

class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def a_star(self, start):

        open_list = [[heuristic[start], 0, start, [start]]]
        closed_list = []

        while open_list:

            open_list.sort()
            current = open_list.pop(0)

            f = current[0]
            g = current[1]
            node = current[2]
            path = current[3]

            print("Visiting:", node, "g:", g, "h:", heuristic[node], "f:", f)

            if node == self.goal:
                print("Goal found!")
                print("Optimal Path:", path)
                print("Total Cost:", g)
                return path, g

            if node not in closed_list:
                closed_list.append(node)

                for neighbour in graph[node]:
                    new_g = g + graph[node][neighbour]
                    new_f = new_g + heuristic[neighbour]
                    open_list.append([new_f, new_g, neighbour, path + [neighbour]])

        print("Goal not found.")
        return None, None


def change_random_edge():

    all_edges = []

    for node in graph:
        for neighbour in graph[node]:
            all_edges.append((node, neighbour))

    edge = random.choice(all_edges)

    old_cost = graph[edge[0]][edge[1]]

    change = random.randint(-5, 5)
    new_cost = max(1, old_cost + change)

    graph[edge[0]][edge[1]] = new_cost

    print("\nEdge cost changed:", edge[0], "->", edge[1],
          old_cost, "→", new_cost)


start_node = 'A'
goal_node = 'G'

agent = GoalBasedAgent(goal_node)

print("\nInitial A* Run\n")
agent.a_star(start_node)

change_random_edge()

print("\nRecomputing After Dynamic Change\n")
agent.a_star(start_node)
