def generate(numRows: int) -> list[list[int]]:
    """
    Generate Pascal's Triangle up to the specified number of rows.

    :param numRows: The number of rows to generate in Pascal's Triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    res = [[1]]

    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    
    return res

# Explanation:
# The function `generate` creates Pascal's Triangle up to the specified number of rows.
# It initializes the result list with the first row of Pascal's Triangle, which is [1].
# For each subsequent row, it constructs a temporary list `temp` that has 0s padded on both ends of the last row of the triangle. 
# This allows for easy calculation of the new row by summing adjacent elements from the previous row.
# The new row is then appended to the result list, 
# and the process continues until the desired number of rows is generated. Finally, the function returns the complete list representing Pascal's Triangle.