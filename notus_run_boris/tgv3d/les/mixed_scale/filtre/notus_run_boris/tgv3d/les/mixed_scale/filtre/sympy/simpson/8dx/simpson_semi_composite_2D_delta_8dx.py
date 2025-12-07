import sympy as sp

# 1) Définitions des symboles
i, j = sp.symbols('i j', integer=True)         
u = sp.Function('u')                            
U = sp.IndexedBase('u')                          


# 3) Poids Simpson 2D
W = { -4: 1, -3: 4, -2: 2, -1: 4, 0: 2, 1: 4, 2: 2, 3: 4, 4: 1 }

# 4) Construction de l’approximation discrète par Simpson tensorisé
#    Factorisation : (dx/3)^2/(8dx)^2 = 1/576
factor = sp.Rational(1,576)
expr_discrete_2d = factor * sum(
    W[p]*W[q] * U[i + p, j + q]
    for p in (-4, -3, -2, -1, 0, 1, 2, 3, 4) 
    for q in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
)

# 5) Simplification et affichage
sp.pprint(expr_discrete_2d, use_unicode=True)
