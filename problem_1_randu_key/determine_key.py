import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
import rng_randu

rand = rng_randu.Randu()

# hits start at 7 and then at 13: sn = 13 + 16(n - 1)

l = []
for i in range(1000):
    if i % 2 == 0:
        continue

    rand.seed(i)
    n = rand.random_hex()

    if n == "7":
        l.append(i)

print(l)

rand.seed(13)
a = ""
for i in range(16):
    a += rand.random_hex()

print(a)
