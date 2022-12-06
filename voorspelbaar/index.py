n = int(input())

strng = input()

while True:
    current = input()

    if current == "wat drinkt de nieuwe viaan?":
        break
    else:
        [name, item] = current.split(" drinkt ")
        # print(name, item)
        if strng.startswith(item):
            strng = strng.replace(item + " ", "")
        else:
            strng = strng.replace(" " + item, "")

print(strng, end="")
