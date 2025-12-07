import sympy as sp

print(" champ de vitesse non normalisé \n Méthode des trapèzes composites pour delta = 8 dx" \n )  
# 1) Définitions des symboles
x, y, dx = sp.symbols('x y dx', positive=True)
i, j = sp.symbols('i j', integer=True)         
u = sp.Function('u')                            
U = sp.IndexedBase('u')                          

# 2) Expression continue du filtre Top‑Hat 2D
I_cont_2d = 1/(8*dx)**2 * sp.Integral(
    sp.Integral(u(x,y), (x, x-4*dx, x+4*dx)),
    (y, y-4*dx, y+4*dx)
)
sp.pprint(I_cont_2d, use_unicode=True)


# 3) Poids Simpson 1D
W = { -4: 1, -3: 2, -2: 2, -1: 2, 0: 2, 1: 2, 2: 2, 3: 2, 4: 1 }

# 4) Construction de l’approximation discrète par Simpson tensorisé
factor = sp.Rational(1,256)

expr_discrete_2d =  sum(
    W[p]*W[q] * U[i + p, j + q]
    for p in (-4, -3, -2, -1, 0, 1, 2, 3, 4) 
    for q in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
)

# 5) Simplification et affichage

expr_simpl_2d = sp.simplify(expr_discrete_2d)
#sp.pprint(expr_simpl_2d, use_unicode=True) 

sp.pprint(expr_simpl_2d, use_unicode=True)
