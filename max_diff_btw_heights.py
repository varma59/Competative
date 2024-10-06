def profit(arr, k):
    # If there is only one element, no height difference
    if len(arr) == 1:
        return 0

    # Calculate the midpoint of the smallest and largest values
    n = (min(arr) + max(arr)) // 2
    new = []

    # If the current difference is smaller than k, return the difference
    if max(arr) - min(arr) < k:
        return max(arr) - min(arr)
    
    for i in arr:
        if i >= n:
            new.append(i - k)
        else:
            new.append(i + k)
    
    return max(new) - min(new)

# Test cases with edge cases
test_cases = [
    ([2], 5),                     # Single element
    ([5, 5, 5], 3),               # All elements are the same
    ([10, 20], 8),                # Two elements only
    ([1, 2, 3], 10),              # Difference smaller than k
    ([100, 200, 300], 150),       # k larger than the difference
]

for i, (array, k) in enumerate(test_cases):
    print(f"Test Case {i+1}: Array = {array}, k = {k}")
    print("Maximum difference is:", profit(array, k))
    print('-' * 40)
