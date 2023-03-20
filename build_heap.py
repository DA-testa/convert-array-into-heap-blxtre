def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps += sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    left_child = 2*i+1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2*i+2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps += sift_down(data, min_index, swaps)
    return swaps

def main():
    input_type = input().strip()
    if input_type == '0':
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    else:
        # input from file
        with open(input_type, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
