n = int(input())

# Thanks aoc2021 day 22 (:

allboxes = []


def volume(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)


def overlap(x1, y1, x2, y2, boxes):
    temp = 0
    for i, box in enumerate(boxes):
        overlapping = [
            [max(x1, box[0]), max(y1, box[1])],
            [min(x2, box[2]), min(y2, box[3])],
        ]

        if (
            overlapping[0][0] < overlapping[1][0]
            and overlapping[0][1] < overlapping[1][1]
        ):
            temp += volume(
                overlapping[0][0],
                overlapping[0][1],
                overlapping[1][0],
                overlapping[1][1],
            ) - overlap(
                overlapping[0][0],
                overlapping[0][1],
                overlapping[1][0],
                overlapping[1][1],
                boxes[i + 1 :],
            )

    return temp


count = 0

for _ in range(n):
    [x1, y1, x2, y2] = [int(x) for x in input().split()]
    count += volume(x1, y1, x2, y2) - overlap(x1, y1, x2, y2, allboxes)
    allboxes.append([x1, y1, x2, y2])

print(count)
