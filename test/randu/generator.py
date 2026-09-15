import numpy as np


def randu(seed, n, multiplier, modulus):
    random_numbers = []

    for _ in range(n):
        seed = np.int32((multiplier * int(seed)) % modulus)
        random_numbers.append(seed)

    return random_numbers
