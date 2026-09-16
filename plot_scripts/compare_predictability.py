import pathlib
import secrets
import random

import matplotlib.pyplot as plt
import numpy as np

PLOTS = pathlib.Path(__file__).resolve().parent.parent / "plots"
N = 2000  # prediction attempts
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


def python_secrets(n, seed=1):
    return np.array([secrets.randbits(31) for _ in range(n)])


generators = [
    ('rng_randu (LCG)', randu),
    ('random (Mersenne Twister)', python_random),
    ('secrets (CSPRNG)', python_secrets),
]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Predicting the next number (top) and repeatability with the same seed (bottom)')

for column, (name, generate) in enumerate(generators):
    top, bottom = axes[0][column], axes[1][column]

    numbers = generate(N + 3)
    predicted = (6 * numbers[2:-1] - 9 * numbers[1:-2]) % M
    actual = numbers[3:]
    hits = np.mean(predicted == actual) * 100

    top.scatter(actual / M, predicted / M, s=2, alpha=0.4)
    top.plot([0, 1], [0, 1], color='tab:red', linewidth=0.8, linestyle='--')
    top.set_title(f'{name}\nrule is correct in {hits:.1f} % of cases')
    top.set_xlabel('actual number')
    top.set_ylabel('predicted number')

    difference = generate(200) - generate(200)
    identical = np.mean(difference == 0) * 100
    bottom.plot(difference / M, linewidth=0.8, color='tab:green')
    bottom.set_ylim(-1.05, 1.05)
    bottom.set_title(f'second run, same seed: {identical:.0f} % identical')
    bottom.set_xlabel('n')
    bottom.set_ylabel('difference run 1 - run 2')

fig.tight_layout()
fig.savefig(PLOTS / 'compare_predictability.png', dpi=150)
print('wrote plots/compare_predictability.png')
