import random

N_PARTICLES = 20
DIMS        = 3
ITERS       = 100
W, C1, C2   = 0.5, 1.5, 1.5

def sphere(x): return sum(xi**2 for xi in x)

positions  = [[random.uniform(-5,5) for _ in range(DIMS)] for _ in range(N_PARTICLES)]
velocities = [[random.uniform(-1,1) for _ in range(DIMS)] for _ in range(N_PARTICLES)]
pbest      = [p[:] for p in positions]
gbest      = min(pbest, key=sphere)

for it in range(ITERS):
    for i in range(N_PARTICLES):
        for d in range(DIMS):
            r1, r2 = random.random(), random.random()
            velocities[i][d] = (W * velocities[i][d]
                              + C1*r1*(pbest[i][d] - positions[i][d])
                              + C2*r2*(gbest[d]   - positions[i][d]))
            positions[i][d] += velocities[i][d]
        if sphere(positions[i]) < sphere(pbest[i]):
            pbest[i] = positions[i][:]
    gbest = min(pbest, key=sphere)
    if it % 20 == 0:
        print(f'Iter {it:3d} | Best value: {sphere(gbest):.6f}')

print(f'Global best position: {[round(x,4) for x in gbest]}')
