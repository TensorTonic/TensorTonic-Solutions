import torch
import math

def compute_yarn_rope_freqs(head_dim, base, initial_context_length, scaling_factor, ntk_alpha=1.0, ntk_beta=32.0):
    freq = base ** (torch.arange(0, head_dim, 2, dtype=torch.float64) / head_dim)
    if scaling_factor > 1.0:
        concentration = 0.1 * math.log(scaling_factor) + 1.0
        d_half = head_dim / 2
        low = d_half * math.log(initial_context_length / (ntk_beta * 2 * math.pi)) / math.log(base)
        high = d_half * math.log(initial_context_length / (ntk_alpha * 2 * math.pi)) / math.log(base)
        interpolation = 1.0 / (scaling_factor * freq)
        extrapolation = 1.0 / freq
        ramp = (torch.arange(int(d_half), dtype=torch.float64) - low) / (high - low)
        mask = 1.0 - torch.clamp(ramp, 0.0, 1.0)
        inv_freq = interpolation * (1.0 - mask) + extrapolation * mask
    else:
        concentration = 1.0
        inv_freq = 1.0 / freq
    return concentration, inv_freq
