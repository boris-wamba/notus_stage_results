import sympy as sp

# 1) Définitions des symboles
x, dx = sp.symbols('x dx', positive=True)    
i = sp.symbols('i', integer=True)            
u = sp.Function('u')                         
U = sp.IndexedBase('u')                      

# 2) Expression continue du filtre top‑hat 1D
#    \bar u(x) = 1/(8*dx) * ∫_{x-4dx}^{x+4dx} u(s) ds
I_cont = 1/(8*dx) * sp.Integral(u(x), (x, x-4*dx, x+4*dx))
sp.pprint(I_cont, use_unicode=True)



# 3a) Définition des poids Simpson
W = { -4: 1, -3: 4, -2: 2, -1: 4, 0: 2, 1: 4, 2: 2, 3: 4, 4: 1 }



factor = sp.Rational(1, 24) 
expr_discrete =  sum(W[p] * U[i + p] for p in (-4, -3, -2, -1, 0, 1, 2, 3, 4))

# 4) Simplification et affichage
expr_simpl = sp.simplify(expr_discrete)
sp.pprint(factor*expr_simpl, use_unicode=True)


