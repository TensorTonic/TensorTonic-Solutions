import torch

def softmax_with_sinks(scores: torch.Tensor, sinks: torch.Tensor) -> torch.Tensor:
    scores = torch.as_tensor(scores, dtype=torch.float64)
    sinks = torch.as_tensor(sinks, dtype=torch.float64)

    # Broadcast sinks (H,) -> (H, 1, 1) -> (H, n_q, 1)
    sink_col = sinks[:, None, None] * torch.ones_like(scores[..., :1])

    # Concatenate sink onto the key axis: (H, n_q, n_k + 1)
    combined = torch.cat([scores, sink_col], dim=-1)

    # Stable softmax over the combined axis
    m = combined.max(dim=-1, keepdim=True).values
    e = torch.exp(combined - m)
    denom = e.sum(dim=-1, keepdim=True)

    # Drop the sink column from the output
    return e[..., :-1] / denom
