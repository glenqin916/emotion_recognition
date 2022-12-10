import matplotlib.pyplot as plt

from detect import detect


def int_point(img):
    c = detect(img, 10)
    fast_x = [x for x, y in c]
    fast_y = [y for x, y in c]
    plt.scatter(fast_x, fast_y, s=3, color='red')
    plt.title('FAST Feature Point Detection')
    plt.imshow(img, cmap='gray')
    plt.show()
