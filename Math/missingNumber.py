# 268. Missing Number

# sum formula

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expectedSum = (n * (n+1)) // 2
    actualSum = sum(nums)

    return expectedSum - actualSum

#  XOR
def missingNumberXOR(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num

    return result

# a ^ a = 0
# a ^ 0 = a
# a ^ b ^ a = b