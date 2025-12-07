import sympy as sp

# 1) Définitions des symboles 

i, j, k    = sp.symbols('i j k', integer=True)      
u          = sp.Function('u')                   
U          = sp.IndexedBase('u')                    

# 3) Poids Simpson 3D
W = { -1: 1,  0: 4,  1: 1 }
#factor = sp.Rational(1, 216)
expr_discrete_3d = factor *  sum(
    W[p]*W[q]*W[r] * U[i + p, j + q, k + r]
    for p in (-1,0,1)
    for q in (-1,0,1)
    for r in (-1,0,1)
)

sp.pprint(expr_discrete_3d, use_unicode=True)

