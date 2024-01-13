def segregate_elements(n, arr):
    temp = []  # copy array

    # in the starting only copy the non-negative elements
    for i in range(n):
        if arr[i] >= 0:
            temp.append(arr[i])

    # copy the negative elements to the end of the dummy array
    for i in range(n):
        if arr[i] < 0:
            temp.append(arr[i])

    # copy the dummy array to the original array
    for i in range(n):
        arr[i] = temp[i]

    return arr

if __name__ == "__main__":
    # input
    n = int(input())
    arr = list(map(int, input().split()))

    # segregating the array
    arr = segregate_elements(n, arr)

    # output
    for i in range(n):
        print(arr[i], end=" ")
