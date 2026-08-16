# https://www.youtube.com/watch?v=yubRKwixN-U

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    div = 1
    while x >= 10 * div: 
        div *= 10

    while x :
        left = x // div
        right = x % 10
        if left != right:
            return False
        x = (x % div) // 10
        div //= 100
    return True 

# 121 % 10 = 1 to get the last digit
# 121 / 100 = 1 to get the first digit
# 121 % 100 = 21 to remove the first digit
# 121 // 10 = 12 to remove the last digit