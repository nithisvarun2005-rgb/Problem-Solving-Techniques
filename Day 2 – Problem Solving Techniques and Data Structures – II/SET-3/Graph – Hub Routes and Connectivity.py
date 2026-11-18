from collections import deque

graph = {
    "H1": ["H2", "H3"],
    "H2": ["H1", "H4", "H5"],
    "H3": ["H1", "H6"],
    "H4": ["H2", "H7"],
    "H5": ["H2", "H7"],
    "H6": ["H3", "H8"],
    "H7": ["H4", "H5", "H9"],
    "H8": ["H6", "H10"],
    "H9": ["H7", "H10"],
    "H10": ["H8", "H9"]
}


# BFS
def bfs_shortest_route(graph, start, destination):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


# DFS
def dfs_reachable(graph, start):

    visited = set()

    def dfs(hub):

        visited.add(hub)

        for neighbor in graph[hub]:

            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)

    return visited


print("DELIVERY HUB ROUTE MANAGEMENT")


route = bfs_shortest_route(graph, "H1", "H10")

print("\nShortest Route from H1 to H10:")
print(" -> ".join(route))

print("Number of Hops:", len(route) - 1)


reachable = dfs_reachable(graph, "H1")

print("\nHubs Reachable from Central Depot H1:")
print(sorted(reachable))

print("Total Reachable Hubs:", len(reachable))
