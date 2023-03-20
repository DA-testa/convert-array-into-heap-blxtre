# python3


import math

def sift_down(data, i, swaps):
    min_index = i
    n = len(data)
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(math.floor(n/2), -1, -1):
        sift_down(data, i, swaps)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
