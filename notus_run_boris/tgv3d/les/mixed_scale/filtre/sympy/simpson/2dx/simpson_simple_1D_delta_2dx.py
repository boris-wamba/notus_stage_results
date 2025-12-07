import sympy as sp

# 1) Définitions des symboles
x, dx = sp.symbols('x dx', positive=True)    # variable continue et moitié de largeur
i = sp.symbols('i', integer=True)            # indice discret
u = sp.Function('u')                         # u(x) : fonction continue
U = sp.IndexedBase('u')                      # u[i] : champ discret

W = { -1: 1,  0: 4,  1: 1 }

factor =sp.Rational(1, 6)  
expr_discrete = factor * sum(W[p] * U[i + p] for p in (-1, 0, 1))

sp.pprint(expr_discrete, use_unicode=True)

