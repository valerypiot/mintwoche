import pathlib
import secrets
import random

import matplotlib.pyplot as plt
import numpy as np

PLOTS = pathlib.Path(__file__).resolve().parent.parent / "plots"
N = 200000  # numbers per generator
M = 2**31


def randu(n, seed=1):
    """RANDU: x[n+1] = 65539 * x[n] mod 2^31."""
    out = np.empty(n, dtype=np.int64)
    for i in range(n):
        seed = (65539 * seed) % M
        out[i] = seed
    return out


def python_random(n, seed=1):
    random.seed(seed)
    return np.array([random.getrandbits(31) for _ in range(n)])


def python_secrets(n):
    return np.array([secrets.randbits(31) for _ in range(n)])


generators = [
    ('rng_randu (LCG)', randu(N)),
    ('random (Mersenne Twister)', python_random(N)),
    ('secrets (CSPRNG)', python_secrets(N)),
]

fig, axes = plt.subplots(2, 3, figsize=(15, 7))
fig.suptitle(f'{N} 31-bit numbers each: distribution of the values (top) and of the lowest bit (bottom)')

for column, (name, numbers) in enumerate(generators):
    top, bottom = axes[0][column], axes[1][column]

    top.hist(numbers / M, bins=50, range=(0, 1), color='tab:blue')
    top.axhline(N / 50, color='tab:red', linestyle='--', label='expected value')
    top.set_title(f'{name}\nmean {np.mean(numbers) / M:.4f} (expected 0.5)')
    top.set_xlabel('value')
    top.set_ylabel('count')
    top.legend(fontsize=8)

    share_of_ones = np.mean(numbers & 1)
    bottom.bar(['bit = 0', 'bit = 1'], [1 - share_of_ones, share_of_ones], color='tab:orange')
    bottom.axhline(0.5, color='tab:red', linestyle='--')
    bottom.set_ylim(0, 1)
    bottom.set_title(f'lowest bit: {share_of_ones * 100:.1f} % ones')
    bottom.set_ylabel('share')

fig.tight_layout()
fig.savefig(PLOTS / 'compare_histogram.png', dpi=150)
print('wrote plots/compare_histogram.png')
