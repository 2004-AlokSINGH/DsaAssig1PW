'''
Answer 1

class Solution(object):
    def Sumindex(self, nums,target):
        self.nums=nums
        self.target=target
        n=len(nums)
        for i in range(n-1):
            for j in range(n-1):
                if i==j:
                    continue
                elif nums[i]+nums[j]==target:
                    return i,j
                else:
                    continue

Answer 2                  

def remove_element(nums, val):
    k = 0  # Number of elements not equal to val
    
    # Iterate through the array with two pointers
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move the element to the front of the array
            k += 1  # Increment the count
    
    return k


Answer 3


def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
    
    return left


Answer4

def plusOne(digits):
    n = len(digits)
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, increment it by one and return the digits
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
    
    # If all digits are 9, we need to add an additional digit at the front
    return [1] + digits

    
Answer 5


def merge(nums1, m, nums2, n):
    i = m - 1  # Pointer for nums1
    j = n - 1  # Pointer for nums2
    k = m + n - 1  # Pointer for merged array
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # If there are remaining elements in nums2, copy them to the front of nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

        
Answer 6
def containsDuplicate(nums):
    num_set = set()  # Set to store unique elements
    
    for num in nums:
        if num in num_set:
            return True  # Found a duplicate
        num_set.add(num)  # Add the element to the set
    
    return False  # No duplicates found

    
Answer 7

def moveZeroes(nums):
    n = len(nums)
    zero_ptr = 0  # Pointer for zeros
    
    # Iterate through the array
    for i in range(n):
        if nums[i] != 0:
            # Swap non-zero element with the zero pointer
            nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
            zero_ptr += 1


Answer 8
def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = 0
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = 0
    
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)
        actual_sum += num
    
    missing = expected_sum - actual_sum
    
    return [duplicate, missing]

# Example usage
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)  # Output: [2, 3]

                    












'''



        