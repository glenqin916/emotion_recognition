from isCorner import isCorner
from circle import circle


def detect(image, threshold=50):
    # Initialization
    corners = []
    rows, cols = image.shape
    startRow = 3
    endRow = rows - 3
    startCol = 3
    endCol = cols - 3
    n_star = 9

    # Begin searching through region of interest
    for row in range(startRow, endRow):
        for col in range(startCol, endCol):
            region = circle(row, col)
            if isCorner(image, row, col, region, threshold, n_star):
                corners.append((col, row))
    return corners
