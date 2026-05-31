def pad_and_center_crop(image, pad, crop_h, crop_w):
    """
    Zero-pad a 2D image and return its center crop, rounded to 4 decimals.
    """
    H = len(image)
    W = len(image[0]) if H > 0 else 0
    PH = H + 2 * pad
    PW = W + 2 * pad

    padded = [[0.0] * PW for _ in range(PH)]
    for i in range(H):
        for j in range(W):
            padded[i + pad][j + pad] = float(image[i][j])

    r_start = (PH - crop_h) // 2
    c_start = (PW - crop_w) // 2

    out = []
    for i in range(r_start, r_start + crop_h):
        row = []
        for j in range(c_start, c_start + crop_w):
            row.append(round(padded[i][j], 4))
        out.append(row)
    return out
