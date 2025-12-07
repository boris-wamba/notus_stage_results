import sympy as sp
# simpson composite pour delta = 4dx en 3D 
# 1) Symboles
i, j, k     = sp.symbols('i j k', integer=True)       # indices discrets
u        = sp.Function('u')                      # u(x,y,z) champ continu
U        = sp.IndexedBase('u')                   # U[i,j,k]   champ discret


# 2) Poids de  Simpson composite  étendu à cinq points
W = { -2: 1,  -1: 4,   0: 2,   1: 4,   2: 1 }

# 3) Facteur global : (dx/3)^3 / (4·dx)^3 = 1/1728
factor = sp.Rational(1, 1728)

# 4) Construction de l’expression discrète par Python‐sum
expr_discrete_3d = factor * sum(
    W[p] * W[q] * W[r] * U[i + p, j + q, k + r]
    for p in (-2, -1, 0, 1, 2)
    for q in (-2, -1, 0, 1, 2)
    for r in (-2, -1, 0, 1, 2)
)

# 5) Simplification et affichage

sp.pprint(expr_discrete_3d, use_unicode=True)

