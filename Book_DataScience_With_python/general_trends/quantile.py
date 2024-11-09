def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]
