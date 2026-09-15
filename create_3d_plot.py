import rng_randu
import matplotlib.pyplot as plt
import numpy as np

randu = rng_randu.Randu()

randu.seed(1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.view_init(elev=24, azim=61)
ax.set_box_aspect((1, 1, 1)) 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

n = 1000000
p_num = n // 3
points = np.zeros((p_num, 3))

for i in range(p_num): 
    for j in range(3): 
        points[i][j] = randu.random()


kp = points.T 
ax.scatter(kp[0], kp[1], kp[2], s=1)
fig.savefig('plot.png', dpi=150)