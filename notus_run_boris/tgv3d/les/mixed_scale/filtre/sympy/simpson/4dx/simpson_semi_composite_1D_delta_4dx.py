import sympy as sp

# 1) Symboles
x, dx = sp.symbols('x dx', positive=True)  # variable continue et pas
i      = sp.symbols('i', integer=True)     # indice discret
u      = sp.Function('u')                  # u(x) champ continu
U      = sp.IndexedBase('u')               # U[i]   champ discret

# 2) Intégrale continue (non évaluée)
I_cont = 1/(4*dx) * sp.Integral(u(x), (x, x-2*dx, x+2*dx))
sp.pprint(I_cont, use_unicode=True)

# 3) Poids de Simpson composite sur [-2dx, +2dx]
#    points p=-2,-1,0,1,2
W = { -2: 1,  -1: 4,  0: 2,  1: 4,  2: 1 }

# 4) Approximation Simpson composite :
#    ∫_{x-2dx}^{x+2dx} u(s) ds ≈ (dx/3) * Σ_{p=-2..2} W[p]·u(x + p·dx)
expr_discrete = (1/(4*dx)) * (dx/3) * sum(
    W[p] * U[i + p] for p in (-2, -1, 0, 1, 2)
)

# 5) Simplification et affichage
expr_simpl = sp.simplify(expr_discrete)
sp.pprint(expr_simpl, use_unicode=True)

