STATES  = ['S0','S1','S2','S3','GOAL','TRAP']
ACTIONS = ['left','right']
GAMMA   = 0.9
THETA   = 1e-6

T = {
  'S0':   {'left':[(.8,'S0',-1),(.2,'S1',-1)], 'right':[(.8,'S1',-1),(.2,'S0',-1)]},
  'S1':   {'left':[(.8,'S0',-1),(.2,'S2',-1)], 'right':[(.8,'S2',-1),(.2,'S1',-1)]},
  'S2':   {'left':[(.8,'S1',-1),(.2,'S3',-1)], 'right':[(.8,'S3',-1),(.2,'S2',-1)]},
  'S3':   {'left':[(.8,'S2',-1),(.2,'GOAL',-1)],'right':[(.8,'GOAL',+10),(.2,'TRAP',-10)]},
  'GOAL': {'left':[(1,'GOAL',0)], 'right':[(1,'GOAL',0)]},
  'TRAP': {'left':[(1,'TRAP',0)], 'right':[(1,'TRAP',0)]},
}

V = {s: 0 for s in STATES}

while True:
    delta = 0
    for s in STATES:
        if s in ('GOAL','TRAP'): continue
        q_vals = []
        for a in ACTIONS:
            q = sum(p*(r + GAMMA*V[s2]) for p,s2,r in T[s][a])
            q_vals.append(q)
        new_v = max(q_vals)
        delta = max(delta, abs(new_v - V[s]))
        V[s] = new_v
    if delta < THETA: break

policy = {}
for s in STATES:
    if s in ('GOAL','TRAP'): policy[s]='—'; continue
    policy[s] = max(ACTIONS, key=lambda a: sum(p*(r+GAMMA*V[s2]) for p,s2,r in T[s][a]))

print('Values :', {s:round(v,2) for s,v in V.items()})
print('Policy :', policy)
