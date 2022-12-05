n = int(input())
state = [False if x == "F" else True for x in input().split()]
postfix = input().split()

# Parsed
stack = []
operation_stack = []

operation = {
    "*": lambda: stack.pop() and stack.pop(),
    "+": lambda: stack.pop() or stack.pop(),
    "-": lambda: not stack.pop(),
}

for c in postfix:
    if c in operation:
        operation_stack.insert(0, c)
    else:
        stack.insert(0, state[ord(c) - 65])

while operation_stack:
    stack.append(operation[operation_stack.pop()]())

print("T" if stack.pop() else "F")
