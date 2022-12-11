n = int(input())

huizen = [int(x) for x in input().split()]

m = int(input())

adjlist = [[] for _ in range(n)]

for _ in range(m):
    [a, b, d] = [int(x) for x in input().split()]

    adjlist[a - 1].append((b - 1, d))
    adjlist[b - 1].append((a - 1, d))

from queue import PriorityQueue

queue = PriorityQueue()
queue.put((0, huizen[0], [0]))

visited = [False] * n
visited[0] = True

max_kids = 0
shortest_paths = []

while not queue.empty():
    distance, kids, path = queue.get()
    node = path[-1]

    if node == n - 1:
        if kids > max_kids:
            max_kids = kids
            shortest_paths = [path]
        elif kids == max_kids:
            shortest_paths.append(path)

    for neighbor in adjlist[node]:
        if not visited[neighbor[0]]:
            visited[neighbor[0]] = True
            queue.put(
                (
                    distance + neighbor[1],
                    kids + huizen[neighbor[0]],
                    path + [neighbor[0]],
                )
            )


if len(shortest_paths) > 0:
    # Print total distance
    path = shortest_paths[0]
    distance = 0
    for i in range(len(path) - 1):
        for neighbor in adjlist[path[i]]:
            if neighbor[0] == path[i + 1]:
                distance += neighbor[1]
                break
    print(distance, max_kids)
else:
    print("impossible")
