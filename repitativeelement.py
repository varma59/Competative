def find_max_duplicate(arr):
    if not arr:
        return None 
    
    count = {}
    
    for char in arr:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    max_char = max(count, key=count.get)
    
    return max_char

arr1 = ["hi", "hi", "hi", "hi", "bye", "vlodf", "bye", "bye", "bye", "bye", "bye", "bye"]   
print(find_max_duplicate(arr1))  # Output: "bye"
