import random, math

cities = [(0,0),(1,4),(3,2),(5,5),(7,1),(6,4),(2,6),(4,0)]

def dist(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])

def route_len(r): return sum(dist(cities[r[i]], cities[r[(i+1)%len(r)]]) for i in range(len(r)))

def ox_crossover(p1, p2):
    a, b = sorted(random.sample(range(len(p1)), 2))
    child = [None]*len(p1)
    child[a:b] = p1[a:b]
    fill = [g for g in p2 if g not in child]
    idx = 0
    for i in range(len(child)):
        if child[i] is None: child[i] = fill[idx]; idx += 1
    return child

def swap_mutate(r):
    if random.random() < 0.2:
        i, j = random.sample(range(len(r)), 2)
        r[i], r[j] = r[j], r[i]
    return r

n = len(cities)
pop = [random.sample(range(n), n) for _ in range(20)]

for gen in range(50):
    pop.sort(key=route_len)
    parents = pop[:10]
    offspring = [swap_mutate(ox_crossover(random.choice(parents),
                                          random.choice(parents))) for _ in range(10)]
    pop = parents + offspring

best = min(pop, key=route_len)
print(f'Best route: {best}')
print(f'Total distance: {route_len(best):.2f}')
