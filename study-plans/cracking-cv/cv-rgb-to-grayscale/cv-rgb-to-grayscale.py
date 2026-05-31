def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using ITU-R BT.601 luma weights.

    Returns:
        2D list of shape (H, W) with luma values rounded to 4 decimals
    """
    H = len(image)
    W = len(image[0])
    out = [[0.0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            r, g, b = image[i][j]
            y = 0.299 * r + 0.587 * g + 0.114 * b
            out[i][j] = round(y, 4)
    return out
