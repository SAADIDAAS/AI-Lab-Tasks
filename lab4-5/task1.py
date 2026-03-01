building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

graph = {}

rows = len(building)
cols = len(building[0])

for r in range(rows):
    for c in range(cols):
        if building[r][c] == 1:
            node = str(r) + "," + str(c)
            graph[node] = []

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if building[nr][nc] == 1:
                        neighbour = str(nr) + "," + str(nc)
                        graph[node].append(neighbour)



class GoalBasedAgent:

    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):

        visited = []
        queue = []   
        parent = {}   

        visited.append(start)
        queue.append(start)

        print("\nFollowing is the Breadth-First Search (BFS):")

        while queue:
            node = queue.pop(0)
            print("Visiting:", node)

            if node == goal:
                print("Goal found!")
                break

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    parent[neighbour] = node
                    queue.append(neighbour)

        path = []
        current = goal

        while current in parent or current == start:
            path.append(current)
            if current == start:
                break
            current = parent[current]

        path.reverse()

        print("\nShortest Path:")
        print(path)

        return "Search Complete"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)

        if goal_status == "Goal reached":
            return "Goal already reached!"
        else:
            return self.bfs_search(graph, percept, self.goal)


class Environment:

    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)
    print(action)


start_node = "0,0"
goal_node = "3,3"

agent = GoalBasedAgent(goal_node)
environment = Environment(graph)

run_agent(agent, environment, start_node)
