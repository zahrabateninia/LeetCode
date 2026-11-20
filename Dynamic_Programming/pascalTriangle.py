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

