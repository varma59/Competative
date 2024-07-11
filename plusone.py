def plusOne(digits):
    # Convert the list of digits to an integer
    num = int(''.join(map(str, digits)))
    
    # Increment the integer by 1
    num += 1
    
    # Convert the incremented integer back to a list of digits
    return list(map(int, str(num)))

# Example usage:
print(plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plusOne([9]))  # Output: [1, 0]
