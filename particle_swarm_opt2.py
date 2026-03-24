import random

def mock_accuracy(lr, n_est):
    peak_lr, peak_n = 0.05, 150
    return 1 - 0.5*((lr - peak_lr)**2 / 0.01 + (n_est - peak_n)**2 / 10000)

N, ITERS = 15, 80
W, C1, C2 = 0.4, 1.8, 1.8

pos = [[random.uniform(0.001, 0.5), random.uniform(10, 300)] for _ in range(N)]
vel = [[random.uniform(-0.01, 0.01), random.uniform(-5, 5)] for _ in range(N)]
pbest = [p[:] for p in pos]
gbest = max(pbest, key=lambda p: mock_accuracy(*p))

for it in range(ITERS):
    for i in range(N):
        for d in range(2):
            r1, r2 = random.random(), random.random()
            vel[i][d] = (W*vel[i][d]
                       + C1*r1*(pbest[i][d]-pos[i][d])
                       + C2*r2*(gbest[d]-pos[i][d]))
            pos[i][d] += vel[i][d]
        pos[i][0] = max(0.0001, min(0.5, pos[i][0]))
        pos[i][1] = max(10, min(300, pos[i][1]))
        if mock_accuracy(*pos[i]) > mock_accuracy(*pbest[i]):
            pbest[i] = pos[i][:]
    gbest = max(pbest, key=lambda p: mock_accuracy(*p))

lr, n = gbest
print(f'Best lr={lr:.4f}, n_estimators={int(n)}, acc={mock_accuracy(lr,n):.4f}')
