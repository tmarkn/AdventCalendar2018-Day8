class Node():
    value = 0
    children = []
    def __init__(self):
        self.value = 0
        self.children = []

with open("input.txt", "r") as inFile:
    for line in inFile:
        input = line

## delimit values and store in array
arr = input.split(" ")                                              

## set first index to int
## set second index to value of metadata
for i in range(len(arr)):                                           
    arr[i] = [int(arr[i]), None]

## find the zero values
## zeroes are the values with no children
def extractZeros(arr):
    for i in range(len(arr)):                                       ## for each number
        if arr[i][0] == 0:                                          ## if has no children
            if arr[i][1] is None:                                   ## if not a node / never touched
                arr[i][1] = Node()                                  ## create node
                for j in range(arr[i+1][0]):                        ## value of this node is the sum of metadata
                    arr[i][1].value += arr[i+2+j][0]
            else:                                                   ## touched before but all children were accessed
                for j in range(arr[i+1][0]):                        ## for number of metadata
                    arr[i][1].value += arr[i+2+j][0]                   ## add value of metadata
                for j in arr[i][1].children:
                    arr[i][1].value += j.value
            if i != 0:                                              ## if index is not the first
                arr[i-2][0] -= 1                                    ## decrement child counter of parent
                if arr[i-2][1] is None:                             ## if parent node was not accessed
                    arr[i-2][1] = Node()                            ## create parent node
                arr[i-2][1].children.append(arr[i][1])              ## append current node to parent
            value = arr[i][1].value                                 ## store value of current
            for j in range(arr[i+1][0] + 2):                        ## remove children and metadata from array
                arr.pop(i)
            return value
    raise RuntimeWarning                                            ## if this was reached, you have a problem

value = 0
while(len(arr) > 0):
    value = extractZeros(arr)
print("Your value is: " + str(value))