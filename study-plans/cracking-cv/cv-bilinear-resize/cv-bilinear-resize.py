import math

def bilinear_resize(image, new_h, new_w):
    """
    Corner-aligned bilinear resize. Equivalent to
    F.interpolate(..., mode='bilinear', align_corners=True).
    """
    H = len(image)
    W = len(image[0])

    sy = 0.0 if new_h == 1 else (H - 1) / (new_h - 1)
    sx = 0.0 if new_w == 1 else (W - 1) / (new_w - 1)

    out = [[0.0] * new_w for _ in range(new_h)]
    for i in range(new_h):
        y_src = 0.0 if new_h == 1 else i * sy
        y0 = int(math.floor(y_src))
        y1 = min(y0 + 1, H - 1)
        wy = y_src - y0
        for j in range(new_w):
            x_src = 0.0 if new_w == 1 else j * sx
            x0 = int(math.floor(x_src))
            x1 = min(x0 + 1, W - 1)
            wx = x_src - x0

            v = ((1.0 - wy) * (1.0 - wx) * float(image[y0][x0]) +
                 (1.0 - wy) * wx         * float(image[y0][x1]) +
                 wy         * (1.0 - wx) * float(image[y1][x0]) +
                 wy         * wx         * float(image[y1][x1]))
            out[i][j] = round(v, 4)
    return out
