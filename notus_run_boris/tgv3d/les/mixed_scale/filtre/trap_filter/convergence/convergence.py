import numpy as np
import matplotlib.pyplot as plt

def filter_delta_dx_trapz_2D(u):
    """  Filtre (méthode des trapèzes) avec conditions périodiques """
    u_filtre = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # periodic j (axe y)
            if j == 0: # bas
                jm1 = ny - 1
                jp1 = j + 1
            elif j == ny - 1: # haut
                jm1 = j - 1
                jp1 = 0
            else:
                jm1 = j - 1
                jp1 = j + 1
            # periodic i (axe x)
            if i == 0: # gauche
                im1 = nx - 1
                ip1 = i + 1
            elif i == nx - 1: # droite
                im1 = i - 1
                ip1 = 0
            else:
                im1 = i - 1
                ip1 = i + 1
            u_filtre[i, j] = (
                u[im1, jm1] + u[ip1, jm1] + u[im1, jp1] + u[ip1, jp1] +  # coins
                2 * (u[im1, j] + u[ip1, j] + u[i, jm1] + u[i, jp1]) +  # bords
                4 * u[i, j]  # centre
            ) / 16.0
    return u_filtre


def filter_delta_2dx_trapz_2D(u): 
    """ Filtre (méthode des trapèzes ) avec conditions périodiques cas delta = 2dx """ 
    u_filtre_2dx = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # periodic j (axe y)
            if j == 0: # bas
                jm1 = ny - 1
                jp1 = j + 1
            elif j == ny - 1: # haut
                jm1 = j - 1
                jp1 = 0
            else:
                jm1 = j - 1
                jp1 = j + 1
            # periodic i (axe x)
            if i == 0: # gauche
                im1 = nx - 1
                ip1 = i + 1
            elif i == nx - 1: # droite
                im1 = i - 1
                ip1 = 0
            else:
                im1 = i - 1
                ip1 = i + 1
            u_filtre_2dx[i, j] = ( u[im1, jm1] + u[im1, jp1] + u[ip1, jm1] + u[ip1, jp1] ) / 4
    return u_filtre_2dx


def filter_delta_3dx_trapz_2D(u):
    """ Filtre (méthode des trapèzes ) avec conditions périodiques cas delta = 3dx """ 
    u_filtre_3dx = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # periodic j (axe y)
            if j == 0: # bas
                jm2 = ny - 2
                jm1 = ny - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == 1:
                jm2 = ny -1
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == ny - 1: # haut
                jm2 = j - 2
                jm1 = j - 1
                jp1 = 0
                jp2 = 1
            elif j == ny- 2:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 =  0
            else:
                jm1 = j - 1
                jm2 = j - 2
                jp1 = j + 1
                jp2 = j + 2
            # periodic i (axe x)
            if i == 0:  # gauche
                im2 = nx - 2
                im1 = nx - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == 1:
                im2 = nx - 1
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == nx - 2:  # droite
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = 0
            elif i == nx - 1:
                im2 = i - 2
                im1 = i - 1
                ip1 = 0
                ip2 = 1
            else:
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2

            u_filtre_3dx[i, j] = (
                u[im2, jm2] + u[im2, jm1] + u[im1, jm1] + u[im1, jm2] +
                u[im2, jp2] + u[im2, jp2] + u[im1, jp2] + u[im1, jp1] +
                u[ip1, jm2] + u[ip1, jm1] + u[ip2, jm1] + u[ip2, jm2] +
                u[ip1, jp1] + u[ip1, jp2] + u[ip2, jp2] + u[ip2, jp1]
            ) / 16
    return u_filtre_3dx

def filter_delta_4dx_trapz_2D(u):
    """ Filtre (méthode des trapèzes ) avec conditions périodiques cas delta = 4dx """ 
    u_filtre_4dx = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # periodic j (axe y)
            if j == 0: # bas
                jm2 = ny - 2
                jm1 = ny - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == 1:
                jm2 = ny -1
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == ny - 1: # haut
                jm2 = j - 2
                jm1 = j - 1
                jp1 = 0
                jp2 = 1
            elif j == ny- 2:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 =  0
            else:
                jm1 = j - 1
                jm2 = j - 2
                jp1 = j + 1
                jp2 = j + 2
            # periodic i (axe x)
            if i == 0:  # gauche
                im2 = nx - 2
                im1 = nx - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == 1:
                im2 = nx - 1
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == nx - 2:  # droite
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = 0
            elif i == nx - 1:
                im2 = i - 2
                im1 = i - 1
                ip1 = 0
                ip2 = 1
            else:
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2


            u_filtre_4dx[i, j] = (
                u[im2, jm2] + u[im2, jm2] + u[ip2, jm2] + u[ip2, jp2]
            ) / 4
    return u_filtre_4dx



def filter_delta_4dx_multipletrapz_2D(u):
    """ Filtre (méthode des trapèzes mutiples) avec conditions périodiques cas delta = 4dx """
    u_filtre_4dx_multi = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # periodic j (axe y)
            if j == 0: # bas
                jm2 = ny - 2
                jm1 = ny - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == 1:
                jm2 = ny -1
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == ny - 1: # haut
                jm2 = j - 2
                jm1 = j - 1
                jp1 = 0
                jp2 = 1
            elif j == ny- 2:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 =  0
            else:
                jm1 = j - 1
                jm2 = j - 2
                jp1 = j + 1
                jp2 = j + 2
            # periodic i (axe x)
            if i == 0:  # gauche
                im2 = nx - 2
                im1 = nx - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == 1:
                im2 = nx - 1
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == nx - 2:  # droite
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = 0
            elif i == nx - 1:
                im2 = i - 2
                im1 = i - 1
                ip1 = 0
                ip2 = 1
            else:
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2


            u_filtre_4dx_multi[i, j] = (
                u[im2, jm2] + u[im2, jp2] + u[ip2, jp2] + u[ip2, jm2] + 
                3*(u[im2, jm1] + u[im2, jp1] + u[ip2, jp1] + u[ip2, jm1]) +
                3*(u[im1, jm2] + u[im1, jp2] + u[ip1, jp2] + u[ip1, jm2]) +
                9*(u[im1, jm1] + u[im1, jp1] + u[ip1, jp1] + u[ip1, jm1]) 
            ) / 64
    return u_filtre_4dx_multi








def compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y):
    argx = KXS * delta_x*0.5
    argy = KYS * delta_y*0.5
    fft_us = np.fft.fftshift(np.fft.fftn(signal))
    fft_filtre_s = np.sinc(argx/np.pi) * np.sinc(argy/np.pi)
    fft_convo_s = fft_filtre_s * fft_us
    u_filtered = np.fft.ifftn(np.fft.ifftshift(fft_convo_s)).real
    return u_filtered

#N_list = [16, 32, 64, 128, 256]

#for N in N_list:
   # print(f"\nCalcul pour N={N}")
   # L = 2*np.pi
   # Nx, Ny = N, N
   # x = np.linspace(0, L, Nx)
   # y = np.linspace(0, L, Ny)
   # X, Y = np.meshgrid(x, y, indexing="ij")
   # dx = x[1] - x[0]
   # dy = y[1] - y[0]
   # kxs = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Nx, dx))
   # kys = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Ny, dy))
   # KXS, KYS = np.meshgrid(kxs, kys, indexing="ij")

    # Fréquences spatiales (kx, ky)
   # kx, ky = 2, 3
   # signal = np.sin(kx*X + ky*Y)
    #noise = 0.1 * np.random.randn(Nx, Ny)
    #signal = signal + noise

    # Filtrage =
    # for i in range(1, 2): 
        #delta_x = i * dx
        #delta_y = i * dy
        #signal_filtered = compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y)
        #signal_filtered_trapz = filter_delta_dx_trapz_2D(signal)



        # Erreur relative max (norme infinie  et euclidienne)
        #epsilon = np.linalg.norm(signal_filtered_trapz - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
        #epsilon2 = np.linalg.norm(signal_filtered_trapz - signal_filtered) / np.linalg.norm(signal_filtered)

        #print(f"  Erreur relative L^\\infty (trapz vs exact): {epsilon:.2e}")
        #print(f"  Erreur relative L^2 (trapz vs exact): {epsilon2:.2e}")

        #err_list.append(epsilon)
        #err_list2.append(epsilon2)
        # Visualisation pour chaque N
        #plt.figure()
        #plt.title(f"Coupe 1D en x, N={N}, Delta = {i} dx")
        #plt.plot(signal[Nx//2, :], label="Original bruité")
        #plt.plot(signal_filtered[Nx//2, :], label="Filtré exact")
        #plt.plot(signal_filtered_trapz[Nx//2, :], label="Filtré trapz (delta = dx)")
        #plt.legend()
        #plt.savefig(f"signal_coupe_1D_N{N}_dx{i}.png")


# Affichage convergence 
#plt.figure()
#plt.loglog(N_list, err_list2, "o-", label="Erreur relative quadratique  ($L^2$)")
#plt.loglog(N_list, err_list, "o-", label="Erreur relative max (L-inf)")
#plt.loglog(N_list, 1e3*1/np.asarray(N_list)**2, "-.", label="o2")
#plt.xlabel(r" $N$")
#plt.ylabel(r" $\epsilon_{max}(N)$ ")
#plt.title(r"Erreur  $L^\infty$" )
#plt.grid(True, which="both", ls=":")
#plt.legend()
#plt.savefig(f"erreur.png")
#plt.show()

N_list = [16, 32, 64, 128, 256,512]

# calcul des  erreurs  max et erreur L2
err_list_dx, err_list2_dx = [], []
err_list_2dx, err_list2_2dx = [], []
err_list_3dx, err_list2_3dx = [], []
err_list_4dx, err_list2_4dx = [], []

err_list_4dx_multi, err_list2_4dx_multi = [], []

for N in N_list:
    print(f"\nCalcul pour N={N}")
    L = 2*np.pi
    Nx, Ny = N, N
    x = np.linspace(0, L, Nx)
    y = np.linspace(0, L, Ny)
    X, Y = np.meshgrid(x, y, indexing="ij")
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    kxs = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Nx, dx))
    kys = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Ny, dy))
    KXS, KYS = np.meshgrid(kxs, kys, indexing="ij")

    kx, ky = 2, 3
    signal = np.sin(kx*X + ky*Y)

    # === Filtrage ===
    signal_filtered = compute_exact_convolution_top_hat(signal, KXS, KYS, dx, dy)
    signal_filtered_trapz     = filter_delta_dx_trapz_2D(signal)
    signal_filtered_trapz_2dx = filter_delta_2dx_trapz_2D(signal)
    signal_filtered_trapz_3dx = filter_delta_3dx_trapz_2D(signal)
    signal_filtered_trapz_4dx = filter_delta_4dx_trapz_2D(signal)
    signal_filtered_trapz_4dx_multi = filter_delta_4dx_multipletrapz_2D(signal)

    # Erreur relative max (Linf) et quadratique (L2) pour chaque cas
    # delta = dx
    epsilon_dx = np.linalg.norm(signal_filtered_trapz - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
    epsilon2_dx = np.linalg.norm(signal_filtered_trapz - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_dx.append(epsilon_dx)
    err_list2_dx.append(epsilon2_dx)

    # delta = 2dx
    epsilon_2dx = np.linalg.norm(signal_filtered_trapz_2dx - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
    epsilon2_2dx = np.linalg.norm(signal_filtered_trapz_2dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_2dx.append(epsilon_2dx)
    err_list2_2dx.append(epsilon2_2dx)

    # delta = 3dx
    epsilon_3dx = np.linalg.norm(signal_filtered_trapz_3dx - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
    epsilon2_3dx = np.linalg.norm(signal_filtered_trapz_3dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_3dx.append(epsilon_3dx)
    err_list2_3dx.append(epsilon2_3dx)

    # delta = 4dx
    epsilon_4dx = np.linalg.norm(signal_filtered_trapz_4dx - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
    epsilon2_4dx = np.linalg.norm(signal_filtered_trapz_4dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_4dx.append(epsilon_4dx)
    err_list2_4dx.append(epsilon2_4dx)


    # delta = 4dx multiple 
    epsilon_4dx_multi = np.linalg.norm(signal_filtered_trapz_4dx_multi - signal_filtered, ord=np.inf) / np.linalg.norm(signal_filtered, ord=np.inf)
    epsilon2_4dx_multi = np.linalg.norm(signal_filtered_trapz_4dx_multi - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_4dx_multi.append(epsilon_4dx_multi )
    err_list2_4dx_multi.append(epsilon2_4dx_multi)





#  AFFICHAGE 

ordre2 = 1 / np.asarray(N_list)**2

#fig, axs = plt.subplots(2, 2, figsize=(13, 10))
# Sous-figure Delta=dx
#ax = axs[0, 0]
#ax.loglog(N_list, err_list_dx, "o-", label=r"Trapz $\Delta=dx$ ($L^\infty$)")
#ax.loglog(N_list, err_list2_dx, "s--", label=r"Trapz $\Delta=dx$ ($L^2$)")
#coef2 = err_list_dx[0] / ordre2[0]
#ax.loglog(N_list, coef2 * ordre2, "-.", label="Ordre 2")
#ax.set_title(r"Erreur pour $\Delta=dx$")
#ax.set_xlabel("$N$")
#ax.set_ylabel(r"$\epsilon$")
#ax.legend()
#ax.grid(True, which="both", ls=":")

# Sous-figure Delta=2dx
#ax = axs[0, 1]
#ax.loglog(N_list, err_list_2dx, "o-", label=r"Trapz $\Delta=2dx$ ($L^\infty$)")
#ax.loglog(N_list, err_list2_2dx, "s--", label=r"Trapz $\Delta=2dx$ ($L^2$)")
#coef2_2dx = err_list_2dx[0] / ordre2[0]
#ax.loglog(N_list, coef2_2dx * ordre2, "-.", label="Ordre 2")
#ax.set_title(r"Erreur pour $\Delta=2dx$")
#ax.set_xlabel("$N$")
#ax.set_ylabel(r"$\epsilon$")
#ax.legend()
#ax.grid(True, which="both", ls=":")

# Sous-figure Delta=3dx
#ax = axs[1, 0]
#ax.loglog(N_list, err_list_3dx, "o-", label=r"Trapz $\Delta=3dx$ ($L^\infty$)")
#ax.loglog(N_list, err_list2_3dx, "s--", label=r"Trapz $\Delta=3dx$ ($L^2$)")
#coef2_3dx = err_list_3dx[0] / ordre2[0]
#ax.loglog(N_list, coef2_3dx * ordre2, "-.", label="Ordre 2")
#ax.set_title(r"Erreur pour $\Delta=3dx$")
#ax.set_xlabel("$N$")
#ax.set_ylabel(r"$\epsilon$")
#ax.legend()
#ax.grid(True, which="both", ls=":")

# Sous-figure Delta=4dx
#ax = axs[1, 1]
#ax.loglog(N_list, err_list_4dx, "o-", label=r"Trapz $\Delta=4dx$ ($L^\infty$)")
#ax.loglog(N_list, err_list2_4dx, "s--", label=r"Trapz $\Delta=4dx$ ($L^2$)")
#coef2_4dx = err_list_4dx[0] / ordre2[0]
#ax.loglog(N_list, coef2_4dx * ordre2, "-.", label="Ordre 2")
#ax.set_title(r"Erreur pour $\Delta=4dx$")
#ax.set_xlabel("$N$")
#ax.set_ylabel(r"$\epsilon$")
#ax.legend()
#ax.grid(True, which="both", ls=":")

#plt.tight_layout()
#plt.savefig("comparaison_ordres_filtrages.png")
#plt.show()
coef2 = err_list_dx[0] / ordre2[0]
coef2_2dx = err_list_2dx[0] / ordre2[0]
coef2_3dx = err_list_3dx[0] / ordre2[0]
coef2_4dx = err_list_4dx[0] / ordre2[0]
coef2_4dx_multi = err_list_4dx_multi[0] / ordre2[0]

plt.figure()
plt.loglog(N_list, err_list2_dx, "s--", label=r"Trapz $\Delta=dx$ ")
plt.loglog(N_list, err_list2_2dx, "s--", label=r"Trapz $\Delta=2dx$ ")
plt.loglog(N_list, err_list2_3dx, "s--", label=r"Trapz $\Delta=3dx$ ")
plt.loglog(N_list, err_list2_4dx, "s--", label=r"Trapz $\Delta=4dx$ ")
plt.loglog(N_list, err_list2_4dx_multi, "s--", label=r"multi_Trapz $\Delta=4dx$ ")

plt.loglog(N_list, coef2_4dx*ordre2,  "8-.", label="Ordre 2" )
plt.xlabel(r" $N$")
plt.ylabel(r" $\epsilon(N)$ ")
plt.title(r"Erreur  $L^2$" )
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.legend()
plt.show()
