# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))

# Input: a = "11", b = "1"
# Output: "100"

# When you have 1 + 1 + 1, the result is 1 with a carry of 1

# more pythonic:

# def addBinary(a: str, b: str) -> str:
#     return bin(int(a, 2) + int(b, 2))[2:]