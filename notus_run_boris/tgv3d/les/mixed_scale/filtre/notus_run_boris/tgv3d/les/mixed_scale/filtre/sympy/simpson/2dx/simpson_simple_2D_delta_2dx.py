import sympy as sp

# 1) Définitions des symboles
i, j = sp.symbols('i j', integer=True)            # indices discrets
u = sp.Function('u')                              # u(x,y) : champ continu
U = sp.IndexedBase('u')                           # U[i,j] : champ discret


# 3) Poids Simpson 2D
W = { -1: 1,  0: 4,  1: 1 }

factor = sp.Rational(1,36)
expr_discrete_2d = factor * sum(
    W[p]*W[q] * U[i + p, j + q]
    for p in (-1,0,1) for q in (-1,0,1)
)


sp.pprint(expr_discrete_2d, use_unicode=True)

