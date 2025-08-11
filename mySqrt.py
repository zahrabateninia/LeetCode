
# def mySqrt(x):
#     if x < 2:
#         return x
#     i = 2
#     while i * i <= x: 
#         i += 1
#     return i - 1

# Use binary search: time complexity O(log x)
def mySqrt(x):
    if x < 2:
        return x
    left, right = 1, x//2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1 
        else:
            right = mid - 1
    return right