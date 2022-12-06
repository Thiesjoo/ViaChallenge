n = int(input())

strng = input().split()
toremove = []
# print(strng)

while True:
    current = input()

    if current == "wat drinkt de nieuwe viaan?":
        break
    else:
        [name, item] = current.split(" drinkt ")
        # print(name, item)
        toremove.append(item)
        # strng.remove(item)
        # strng = strng.replace(item, "")

print(" ".join(filter(lambda x: x not in toremove, strng)))
