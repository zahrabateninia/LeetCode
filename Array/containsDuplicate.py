# 217. Contains Duplicate

def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()  # O(nlogn)

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False

# space complexity: O(n)

# More efficient solution: Using a set:
def containsDuplicateSet(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

