import sympy as sp

# 1) Définitions des symboles

i, j, k    = sp.symbols('i j k', integer=True)
u          = sp.Function('u')
U          = sp.IndexedBase('u')


# 3) Poids Simpson 1D
W = { -4: 1, -3: 4, -2: 2, -1: 4, 0: 2, 1: 4, 2: 2, 3: 4, 4: 1 }

# 4) Construction de l'approximation discrète (tensorisation Simpson)
#    facteur = (dx/3)^3/(2dx)^3 = 1/13824
factor = sp.Rational(1, 13824)
expr_discrete_3d = factor * sum(
    W[p]*W[q]*W[r] * U[i + p, j + q, k + r]
    for p in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    for q in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    for r in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    )
 
sp.pprint(expr_discrete_3d, use_unicode=True)





