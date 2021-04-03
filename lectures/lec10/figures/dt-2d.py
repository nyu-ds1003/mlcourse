import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x1 = np.random.uniform(0, 10, 100)
x2 = np.random.uniform(0, 10, 100)

blue_pts = []
red_pts = []

for _x1, _x2 in zip(x1, x2):
    pt = (_x1, _x2)
    if _x2 < 3:
        if _x1 < 8:
            blue_pts.append(pt)
        else:
            red_pts.append(pt)
    else:
        if _x1 < 3:
            red_pts.append(pt)
        else:
            blue_pts.append(pt)

plt.xlabel('x1')
plt.ylabel('x2')
plt.scatter([p[0] for p in blue_pts], [p[1] for p in blue_pts])
plt.scatter([p[0] for p in red_pts], [p[1] for p in red_pts])
#plt.savefig('dt-2d.pdf')
plt.axvline(x=3, color='black', linestyle='--', ymin=0.3)
plt.axhline(y=3, color='black', linestyle='--')
plt.axvline(x=8, color='black', linestyle='--', ymax=0.3)
plt.text(4, 1, '$R_{11}$', fontsize=16, bbox=dict(facecolor='white', alpha=0.5))
plt.text(4, 1, 'R1', fontsize=16, bbox=dict(facecolor='white', alpha=0.5))
plt.savefig('dt-2d-regions.pdf')
