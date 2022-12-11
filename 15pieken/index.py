from itertools import permutations
import math

# Compute the area of a polygon with the given vertices
def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area


# Compute the probability that the blindfolded player will win
def win_probability(heptagon):
    # Compute the area of the heptagon
    heptagon_area = polygon_area(heptagon)

    # Compute the probability that a piek thrown by the blindfolded player will land within the heptagon
    p = heptagon_area / 4

    # Compute the probability that the blindfolded player will win
    probability = p**3

    return probability


# Read the number of games to be played
n = int(input())

# Play each game
for _ in range(n):
    # Read the locations of the 7 pieken
    heptagon = []
    for _ in range(7):
        x, y = map(float, input().split())
        heptagon.append((x, y))

    # Read the probability that the blindfolded player will win
    p = float(input())
    print("huh")
    # Find the order of the pieken that gives the probability that matches the given probability
    for order in permutations(heptagon):
        print("diff: ", abs(win_probability(order) - p))
        if math.isclose(win_probability(order), p):
            print("found answer")
            print(order)
            break
