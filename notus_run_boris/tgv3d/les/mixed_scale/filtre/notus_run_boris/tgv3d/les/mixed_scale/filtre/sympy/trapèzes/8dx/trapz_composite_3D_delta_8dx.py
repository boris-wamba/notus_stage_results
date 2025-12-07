import sympy as sp 
print(" champ de vitesse non normalisé \n Méthode des trapèzes composites pour delta = 8 dx \n" )


# 1) Définitions des symboles
x, y, z, dx, dy, dz = sp.symbols('x y z dx dy dz', positive=True)

i, j, k    = sp.symbols('i j k', integer=True)
u          = sp.Function('u')
U          = sp.IndexedBase('u')

# 2) Intégrale à évaluer en 3D
print("Intégrale à évaluer en 3D" ) 
xi, eta, zeta = sp.symbols('xi eta zeta')

I_cont_3d = 1/(8*dx)**3 * sp.Integral(
    u(xi, eta, zeta),
    (xi, x-4*dx, x+4*dx),
    (eta, y-4*dy, y+4*dy),
    (zeta, z-4*dz, z+4*dz)
)
sp.pprint(I_cont_3d, use_unicode=True)
# 3) Poids Simpson 1D
W = { -4: 1, -3: 2, -2: 2, -1: 2, 0: 2, 1: 2, 2: 2, 3: 2, 4: 1 }

# 4) Construction du champ discret  méthode de trepèzes.

factor = sp.Rational(1,4096)  

expr_discrete_3d =  sum(
    W[p]*W[q]*W[r] * U[i + p, j + q, k + r]
    for p in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    for q in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    for r in (-4, -3, -2, -1, 0, 1, 2, 3, 4)
    )

# 5) Simplification et affichage
#expr_simpl_3d = sp.simplify(expr_discrete_3d) 
#sp.pprint(expr_simpl_3d, use_unicode=True)
sp.pprint(expr_discrete_3d, use_unicode=True)


