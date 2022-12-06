def distance(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_shortest_route(stores, gifts, stores_selling):
    purchased_gifts = set()
    total_distance = 0
    current_location = (0, 0)

    while len(purchased_gifts) != len(gifts):
        nearest_stores = sorted(
            stores,
            key=lambda x: distance(current_location, (x[0], x[1]))
            + (1 if x[2] in purchased_gifts else 0) * 1000000,
        )

        if len(nearest_stores) > 0:
            nearest_store = nearest_stores[0]
            nearest_store_distance = distance(
                current_location, (nearest_store[0], nearest_store[1])
            )

            total_distance += nearest_store_distance

            for x in stores_selling[(nearest_store[0], nearest_store[1])]:
                purchased_gifts.add(x)

            current_location = (nearest_store[0], nearest_store[1])

    total_distance += distance(current_location, (0, 0))
    return total_distance


n = int(input())

stores = []
stores_selling = {}
gifts = set()

for i in range(n):
    x, y, g = input().split()

    x = int(x)
    y = int(y)

    stores.append((x, y, g))
    if (x, y) not in stores_selling:
        stores_selling[(x, y)] = []
    stores_selling[(x, y)].append(g)
    gifts.add(g)

shortest_route = find_shortest_route(stores, gifts, stores_selling)

print(shortest_route)
