def build_heap(data):
swaps = []
# build a heap bottom-up by iterating over all non-leaf nodes in the array
for i in range(len(data) // 2 - 1, -1, -1):
# heapify the current node downwards
swaps = heapify_down(data, i, swaps)
return swaps

def heapify_down(data, i, swaps):
# get the indices of the children nodes
left = 2 * i + 1
right = 2 * i + 2
# initialize the index of the minimum value among the node and its children
min_index = i
# compare the node with its left child and update the minimum index if necessary
if left < len(data) and data[left] < data[min_index]:
min_index = left
# compare the node with its right child and update the minimum index if necessary
if right < len(data) and data[right] < data[min_index]:
min_index = right
# if the node is not the minimum, swap it with the minimum and heapify down the swapped node
if i != min_index:
swaps.append((i, min_index))
data[i], data[min_index] = data[min_index], data[i]
swaps = heapify_down(data, min_index, swaps)
return swaps

def main():
# read the input
n = int(input())
data = list(map(int, input().split()))
# build the heap and get the swaps performed
swaps = build_heap(data)
# output the swaps
print(len(swaps))
for i, j in swaps:
print(i, j)

if name == "main":
main()
