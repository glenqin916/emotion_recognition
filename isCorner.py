def isCorner(image, row, col, region, threshold, n_star):
    intensity = int(image[row][col])
    circle = []
    for point in region:
        if image[point[0]][point[1]] > intensity + threshold:
            circle.append(1)
        elif image[point[0]][point[1]] < intensity - threshold:
            circle.append(2)
        else:
            circle.append(0)

    i = 0
    point = circle[i]
    count = 1
    largest_count = count

    for i in range(1, len(circle)):
        if circle[i] == point and circle[i] != 0:
            count += 1
        else:
            if circle[i] == 0:
                point = 0
            if circle[i] != 0:
                if largest_count < count:
                    largest_count = count
                count = 1
                point = circle[i]

    return largest_count >= n_star
