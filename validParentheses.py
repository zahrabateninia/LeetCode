# https://www.youtube.com/watch?v=WTzjTskDFMg
def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
#             if stack:
#                  top_element = stack.pop()
#             else:
#                  top_element = '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# For every character:

#     If it's an opening bracket:
#         Put it on the stack.

#     If it's a closing bracket:
#         Take the most recent opening bracket
#         off the stack.

#         If it doesn't match:
#             return False

# At the end:

#     If the stack is empty:
#         return True

#     Otherwise:
#         return False