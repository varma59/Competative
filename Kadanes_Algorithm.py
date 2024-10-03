def largest_sum_contiguous_subarray(arr):
    # Edge case: empty array
    if len(arr) == 0:
        return 0  # or float('-inf') to indicate no sum is possible
    
    # Initialize variables
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Update max_ending_here to be the maximum of current element or the sum of current element and max_ending_here
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        
        # Update max_so_far if max_ending_here is greater
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example usage with edge cases
arrays = [
    [],                             # Empty array
    [-5, -3, -2, -7],               # All negative numbers
    [3],                            # Single element array
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] # Mixed array
]

for arr in arrays:
    print(f"Array: {arr}, Largest sum: {largest_sum_contiguous_subarray(arr)}")
