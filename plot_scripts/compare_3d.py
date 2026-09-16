import pathlib
import secrets
import random

import matplotlib.pyplot as plt
import numpy as np

PLOTS = pathlib.Path(__file__).resolve().parent.parent / "plots"
N = 30000  # points per generator
M = 2**31


def randu(n, seed=1):
    """RANDU: x[n+1] = 65539 * x[n] mod 2^31."""
    out = np.empty(n, dtype=np.int64)
    for i in range(n):
        seed = (65539 * seed) % M
        out[i] = seed
    return out / M


def python_random(n, seed=1):
    random.seed(seed)
    return np.array([random.getrandbits(31) for _ in range(n)]) / M


def python_secrets(n):
    return np.array([secrets.randbits(31) for _ in range(n)]) / M


fig = plt.figure(figsize=(16, 5.5))
fig.subplots_adjust(left=0.04, right=0.98, wspace=0.12)
fig.suptitle(f'{N} points (x[n], x[n+1], x[n+2]) each - viewing angle elev=24, azim=61')

for i, (name, values) in enumerate([
    ('rng_randu (LCG)', randu(3 * N)),
    ('random (Mersenne Twister)', python_random(3 * N)),
    ('secrets (CSPRNG)', python_secrets(3 * N)),
]):
    points = values.reshape(N, 3).T
    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.view_init(elev=24, azim=61)
    ax.set_box_aspect((1, 1, 1))
    ax.set_title(name)
    ax.set_xlabel('x[n]')
    ax.set_ylabel('x[n+1]')
    ax.set_zlabel('x[n+2]')
    ax.scatter(points[0], points[1], points[2], s=0.5, alpha=0.3)

fig.savefig(PLOTS / 'compare_3d.png', dpi=150)
print('wrote plots/compare_3d.png')
