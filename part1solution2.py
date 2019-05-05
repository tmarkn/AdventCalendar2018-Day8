def peek(arr):
    size = len(arr)
    if size == 0:
        return None
    return arr[size-1]

def tryStack(stack):
    value = 0
    top = peek(stack)
    if top == None:
        return value
    if top[0] == 0:
        stack.pop()
        for i in range(top[1]):
            value += int(arr.pop(0))
        if len(stack) > 0:
            lastEntry = stack[len(stack)-1]
            newLE1 = lastEntry[0] - 1
            stack[len(stack)-1] = (newLE1, lastEntry[1])
        print("stack:", stack)
        value += tryStack(stack)
        return value
    return value

with open("input.txt", "r") as inFile:
    for line in inFile:
        input = line
## delimit values and store in array
arr = input.split(" ") 

stack = []
value = 0

while len(arr) > 0 or len(stack) > 0:
    numChild = int(arr.pop(0))
    numMeta = int(arr.pop(0))

    stack.append((numChild, numMeta))
    print("stack:", stack)
    value += tryStack(stack)

print(value)


## try using stack with (1, 1) first is children, second is metadata
## when top of stack is (0, x) pop stack, decrease next by one, and add metadata