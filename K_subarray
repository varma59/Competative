K-Subarrays

Queston : 
A k-subarray of an array is:

10

C

• a subarray (contiguous elements)

⚫ the sum of the elements is evenly divisible by

k (sum modulo k=0).

11

#

12

#

13

ALL

14 15

Given an array of integers, determine the

number of k-subarrays it contains.

16

#

17 18

Example

k=5

19 20

def

nums = [5, 10, 11, 9,5]

21 > if

2

The 10 k-subarrays are (5), (5, 10), (5, 10, 11,

9), (5, 10, 11, 9, 5), (10), (10, 11, 9), (10, 11, 9,

5), (11, 9), (11, 9, 5), (5).

3

Function Description

Complete the function kSub in the editor below. The function must return a long integer that represents the number of k- subarrays in the array.

kSub has the following parameter(s): int k: the divisor of a k-subarray

int nums[n]: an array of integers

Return

long int: the number of k-subarrays in





Program: 


def kSub(k, nums):
    # Write your code here
    rem = {0: 1}
    s = 0
    count = 0
    for num in nums:
        s = (s + num) % k
        if s in rem:
            count += rem[s]
        rem[s] = rem.get(s, 0) + 1
    return count 

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = kSub(k, nums)

    fptr.write(str(result) + '\n')

    fptr.close()
