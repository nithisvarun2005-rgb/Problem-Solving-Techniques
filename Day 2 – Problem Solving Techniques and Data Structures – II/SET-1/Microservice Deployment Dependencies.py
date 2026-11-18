
from collections import deque

graph = {
    "Inventory": ["Pricing"],
    "Pricing": ["Cart"],
    "Cart": ["Payment"],
    "Payment": ["Notification"],
    "Notification": []
}


# BFS 
def bfs_deployment(graph):

    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == len(graph):
        print("Valid Deployment Order:", order)
    else:
        print("Circular Dependency Detected!")


# DFS 
def dfs_cycle_detection(graph):

    visited = set()
    path = set()

    def dfs(node):
        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:

            if neighbor in path:
                return True

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        path.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


print("MICROSERVICE DEPLOYMENT")

print("\nBFS:")
bfs_deployment(graph)

print("\nDFS:")
print("Circular Dependency:", dfs_cycle_detection(graph))



graph["Notification"].append("Inventory")

print("\nAFTER INTRODUCING CIRCULAR DEPENDENCY")

print("BFS:")
bfs_deployment(graph)

print("\nDFS:")
print("Circular Dependency:", dfs_cycle_detection(graph))
