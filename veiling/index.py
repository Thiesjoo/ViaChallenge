[n, s] = [int(x) for x in input().split()]

bids = []

for _ in range(n):
    [name, amount] = input().split()
    bids.append([int(amount), name])

bids.sort(key=lambda i: i[0], reverse=True)

selected = []
for [bid, name] in bids:
    if s - bid >= 0:
        s -= bid
        selected.append(name)

if s == 0:
    print(len(selected))
    for i in selected:
        print(i)
else:
    print(0)
