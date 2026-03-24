import random

POP_SIZE = 10
GENES    = 8
GENS     = 20
MUT_RATE = 0.1

def fitness(chrom): return sum(chrom)

def crossover(p1, p2):
    pt = random.randint(1, GENES - 1)
    return p1[:pt] + p2[pt:]

def mutate(chrom):
    return [1 - g if random.random() < MUT_RATE else g for g in chrom]

pop = [[random.randint(0,1) for _ in range(GENES)] for _ in range(POP_SIZE)]

for gen in range(GENS):
    pop.sort(key=fitness, reverse=True)
    parents = pop[:POP_SIZE//2]
    children = []
    for i in range(0, len(parents)-1, 2):
        child = crossover(parents[i], parents[i+1])
        children.append(mutate(child))
    pop = parents + children
    best = max(pop, key=fitness)
    print(f'Gen {gen+1:2d} | Best: {best} | Fitness: {fitness(best)}')
