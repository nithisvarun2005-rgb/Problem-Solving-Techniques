from collections import deque


graph = {
    "Registration": ["Assessment"],
    "Assessment": ["Surveyor"],
    "Surveyor": ["Settlement"],
    "Settlement": []
}


# BFS 
def bfs_shortest_path(graph, start, end):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


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


print("CLAIM APPROVAL PROCESS")

result = bfs_shortest_path(
    graph,
    "Registration",
    "Settlement"
)

print("\nShortest Approval Path:")
print(" -> ".join(result))

print("\nDFS Cycle Detection:")
print(dfs_cycle_detection(graph))


# Introduce a loop
graph["Settlement"].append("Assessment")

print("\nAfter Introducing a Loop:")

print("DFS Cycle Detection:")
print(dfs_cycle_detection(graph))
