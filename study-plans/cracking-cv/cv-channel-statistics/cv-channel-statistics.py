import numpy as np

def channel_statistics(batch):
    """
    Compute per-channel mean and per-channel population standard deviation
    across the (N, H, W) axes of a batch of images of shape (N, H, W, C).

    Returns:
        dict with keys "mean" and "std", each a list of length C,
        with every entry rounded to 4 decimals.
    """
    arr = np.asarray(batch, dtype=np.float64)
    mean = arr.mean(axis=(0, 1, 2))
    std = arr.std(axis=(0, 1, 2), ddof=0)
    return {
        "mean": [round(float(m), 4) for m in mean],
        "std": [round(float(s), 4) for s in std],
    }
