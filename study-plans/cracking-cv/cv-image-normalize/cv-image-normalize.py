def normalize_image(image, mean, std):
    """
    Per-channel normalize a 3D image: (image[h][w][c] - mean[c]) / std[c].

    Returns:
        3D list of shape (H, W, C), each value rounded to 4 decimals
    """
    H = len(image)
    W = len(image[0])
    C = len(image[0][0])
    out = [[[0.0 for _ in range(C)] for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            for c in range(C):
                out[h][w][c] = round((image[h][w][c] - mean[c]) / std[c], 4)
    return out
