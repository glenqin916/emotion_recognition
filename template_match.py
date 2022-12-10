import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import fftconvolve

from largest_index import largest_index
from patch_sum import patch_sum


def template_match(search, template):
    image_shape = search.shape

    image = np.array(search, dtype=np.float64, copy=False)
    pad_width = tuple((width, width) for width in template.shape)
    image = np.pad(image, pad_width=pad_width, mode='constant', constant_values=0)

    image_window_sum = patch_sum(image, template.shape)
    image_window_sum2 = patch_sum(image ** 2, template.shape)
    temp_mean = template.mean()
    temp_vol = np.prod(template.shape)
    temp_ssd = np.sum((template - temp_mean) ** 2)
    cross_corr = fftconvolve(image, template[::-1, ::-1, ::-1], mode="valid")[1:-1, 1:-1, 1:-1]
    numerator = cross_corr - image_window_sum * temp_mean
    denominator = image_window_sum2
    image_window_sum = np.multiply(image_window_sum, image_window_sum)
    image_window_sum = np.divide(image_window_sum, temp_vol)
    denominator -= image_window_sum
    denominator *= temp_ssd
    denominator = np.maximum(denominator, 0)  # sqrt of negative number not allowed
    denominator = np.sqrt(denominator)
    response = np.zeros_like(cross_corr, dtype=np.float64)
    mask = denominator > np.finfo(np.float64).eps
    response[mask] = numerator[mask] / denominator[mask]

    slices = []
    for i in range(template.ndim):
        d0 = template.shape[i] - 1
        d1 = d0 + image_shape[i] - template.shape[i] + 1
        slices.append(slice(d0, d1))
    result = response[tuple(slices)]

    ind_list = list(range(1, 500, 10))
    x_list = []
    y_list = []

    for t in ind_list:
        ind = largest_index(result, t)
        x_t, y_t = ind[1][-1], ind[0][-1]
        x_list.append(x_t)
        y_list.append(y_t)
    ij = np.unravel_index(np.argmax(result), result.shape)
    _, x, y = ij[::-1]

    # fig, ax = plt.subplots(len(ind_list), 2, figsize=(15, 20))
    #
    # for i in range(len(ind_list)):
    #     h_temp, w_temp, _ = template.shape
    #     ax[i, 0].imshow(search[y_list[i]: y_list[i] + h_temp, x_list[i]:x_list[i] + w_temp])
    #     ax[i, 0].set_axis_off()
    #     ax[i, 0].set_title(f'detected region, {ind_list[i]} closest')
    #
    #     ax[i, 1].imshow(search)
    #     ax[i, 1].set_axis_off()
    #     ax[i, 1].set_title(f'image: ({x_list[i]},{y_list[i]})')
    #
    #     rect = plt.Rectangle((x_list[i], y_list[i]), w_temp, h_temp, edgecolor='r', facecolor='none')
    #
    #     ax[i, 1].add_patch(rect)
    #
    # plt.show()

    return x_list, y_list
