# Time Complexity:  O(log₃ n)
def powerOfThree(n):
    if n< 1: 
        return False
    while(n%3 == 0 ):
        n/=3
    return n == 1


def isPowerOfThreeRecursion(n):
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return isPowerOfThreeRecursion(n // 3)