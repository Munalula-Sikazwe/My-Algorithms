adjacency_matrix = [[0, 3, 5, 6, 0, 8, 0],
                    [3, 0, 0, 4, 2, 0, 5],
                    [5, 0, 0, 0, 0, 4, 0],
                    [6, 4, 0, 0, 0, 1, 6],
                    [0, 2, 0, 0, 0, 0, 10],
                    [8, 0, 6, 1, 0, 0, 8],
                    [0, 8, 0, 6, 10, 8, 0]
                    ]
def find_min_vertex(distance,visited):
    min_vertex = -1
    for i in range(len(distance)):
        if min_vertex == -1 or distance[min_vertex] > distance[i] and not visited[i]:
            min_vertex = i
    return min_vertex

def dijkstra(adjacency_matrix):
    boundary  = len(adjacency_matrix)

    visited = [False] * boundary
    distance = [0] * boundary

    for i in range(1,boundary):
        distance[i] = float('inf')
    for i in range(boundary-1):
        min_vertex = find_min_vertex(distance,visited)
    for j in range(boundary):
        if adjacency_matrix != 0 and not visited[j]:
            new_dist = distance[min_vertex] + adjacency_matrix[min_vertex][j]
            if new_dist < distance[j]:
                distance[j] = new_dist

    for i in range(boundary):
        print(i, distance[i])

dijkstra(adjacency_matrix)