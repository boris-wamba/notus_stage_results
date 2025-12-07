import sympy as sp
# simpson composite pour delta = 4dx en 2D 
# 1) Symboles
i, j     = sp.symbols('i j', integer=True)       # indices discrets
u        = sp.Function('u')                      # u(x,y) champ continu
U        = sp.IndexedBase('u')                   # U[i,j]   champ discret



# 2) poids de Simpson composite étendu à cinqs poids 
W = { -2: 1,  -1: 4,  0: 2,  1: 4,  2: 1 }

# 3) Facteur global : (dx/3)^2 / (4·dx)^2= 1/144

factor = sp.Rational(1, 144)
expr_discrete_2d = factor * sum(
    W[p] * W[q] * U[i + p, j + q]
    for p in (-2, -1, 0, 1, 2)
    for q in (-2, -1, 0, 1, 2)
)

# 4) Simplification et affichage
sp.pprint(expr_discrete_2d, use_unicode=True)

