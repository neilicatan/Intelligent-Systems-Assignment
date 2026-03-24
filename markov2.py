import random

STATES  = ['S0','S1','S2','S3','GOAL','TRAP']
ACTIONS = ['left','right']

T = {
  'S0':   {'left':[(.8,'S0',-1),(.2,'S1',-1)], 'right':[(.8,'S1',-1),(.2,'S0',-1)]},
  'S1':   {'left':[(.8,'S0',-1),(.2,'S2',-1)], 'right':[(.8,'S2',-1),(.2,'S1',-1)]},
  'S2':   {'left':[(.8,'S1',-1),(.2,'S3',-1)], 'right':[(.8,'S3',-1),(.2,'S2',-1)]},
  'S3':   {'left':[(.8,'S2',-1),(.2,'GOAL',-1)],'right':[(.8,'GOAL',+10),(.2,'TRAP',-10)]},
  'GOAL': {'left':[(1,'GOAL',0)], 'right':[(1,'GOAL',0)]},
  'TRAP': {'left':[(1,'TRAP',0)], 'right':[(1,'TRAP',0)]},
}

ALPHA, GAMMA, EPISODES = 0.1, 0.9, 1000
EPSILON = 0.2

Q = {(s, a): 0.0 for s in STATES for a in ACTIONS}

def step(s, a):
    outcomes = T[s][a]
    probs = [o[0] for o in outcomes]
    idx = random.choices(range(len(outcomes)), weights=probs)[0]
    _, s2, r = outcomes[idx]
    return s2, r

for ep in range(EPISODES):
    s = random.choice(['S0','S1','S2','S3'])
    for _ in range(50):
        if s in ('GOAL','TRAP'): break
        a = (random.choice(ACTIONS) if random.random() < EPSILON
             else max(ACTIONS, key=lambda a: Q[(s,a)]))
        s2, r = step(s, a)
        Q[(s,a)] += ALPHA*(r + GAMMA*max(Q[(s2,b)] for b in ACTIONS) - Q[(s,a)])
        s = s2

policy = {s: max(ACTIONS, key=lambda a: Q[(s,a)])
          for s in STATES if s not in ('GOAL','TRAP')}
print('Q-values:', {k:round(v,2) for k,v in Q.items()})
print('Policy  :', policy)
