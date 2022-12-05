test = {
    "a": "9(p",
    "b": "/*",
    "c": "6",
    "d": "%",
    "e": "l",
    "f": ":)",
    "g": "^^",
    "h": "@!",
    "i": ";",
    "j": "[*]",
    "k": "|<",
    "l": "9",
    "m": "y",
    "n": "en",
    "o": '"',
    "p": "<>",
    "q": "'/",
    "r": "+-",
    "s": "-5-",
    "t": "][",
    "u": "L@",
    "v": "(,)",
    "w": '"',
    "x": "=",
    "y": "ij",
    "z": "?",
}

inp = input()
temp = ""

for i, x in enumerate(list(inp.lower())):
    if x in test:
        temp += test[x]
    else:
        temp += inp[i]
print(temp)
