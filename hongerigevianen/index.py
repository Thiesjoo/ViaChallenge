import math

n = int(input())


def sum_range(a, b):
    # https://en.wikipedia.org/wiki/Arithmetic_progression
    return (b * (b + 1) - a * (a - 1)) // 2


for _ in range(n):
    to_reach = int(input())

    if math.log2(to_reach).is_integer():
        print("IMPOSSIBLE")
        continue

    k = 2
    start = 0
    while True:
        # To sum, we need to have the numbers around to_reach / k
        # We can then have k numbers around that, so offset it by k//2 to get the middle

        start = to_reach // k - k // 2

        help = sum_range(start, start + k - 1)
        if help == to_reach:
            break

        help = sum_range(start + 1, start + k)
        if help == to_reach:
            start = start + 1
            break
        k += 1

    for j in range(start, start + k):
        print(j, end=" ")
    print()
