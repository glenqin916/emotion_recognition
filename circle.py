def circle(row, col):
    p1 = (row + 3, col)
    p2 = (row + 3, col + 1)
    p3 = (row + 2, col + 2)
    p4 = (row + 1, col + 3)
    p5 = (row, col + 3)
    p6 = (row - 1, col + 3)
    p7 = (row - 2, col + 2)
    p8 = (row - 3, col + 1)
    p9 = (row - 3, col)
    p10 = (row - 3, col - 1)
    p11 = (row - 2, col - 2)
    p12 = (row - 1, col - 3)
    p13 = (row, col - 3)
    p14 = (row + 1, col - 3)
    p15 = (row + 2, col - 2)
    p16 = (row + 3, col)
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13,
            p14, p15, p16]
