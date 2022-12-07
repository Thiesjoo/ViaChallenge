# Read input
n, d = map(int, input().split())
vians = []
for i in range(n):
    l, w, h = map(int, input().split())
    vians.append((l, w, h))

# Sort vians in descending order of jump capacity
vians.sort(key=lambda x: -x[0])

# Keep track of the number of vians that can jump out of the debris pile
num_vians = 0

# Keep forming stacks of vians until there are no more vians left in the input
while len(vians) > 0:
    stack = []
    total_weight = 0
    for vian in vians:
        # If the vian's weight doesn't exceed the weight of the vian at the bottom of the stack, add it to the stack
        if total_weight + vian[1] <= vians[0][1]:
            stack.append(vian)
            total_weight += vian[1]

    # If the height of the stack plus the jump capacity of the vian at the top of the stack is less than or equal to the height of the debris pile,
    # add the vians in the stack to the total number of vians that can jump out of the debris pile
    if vians[0][2] + stack[-1][0] <= d:
        num_vians += len(stack)

    # Remove the vians in the stack from the list of vians
    for vian in stack:
        vians.remove(vian)

# Print the total number of vians that can jump out of the debris pile
print(num_vians)
