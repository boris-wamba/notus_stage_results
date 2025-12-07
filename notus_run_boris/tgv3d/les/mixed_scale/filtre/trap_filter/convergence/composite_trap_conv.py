import numpy as np
import matplotlib.pyplot as plt

def filter_delta_dx_trapz_2D(u):
    """  Filtre (méthode des trapèzes composites) avec conditions périodiques """
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
    """  Filtre (méthode des trapèzes composites ) avec conditions périodiques cas delta = 2dx """
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
                u[im2, jm2] + u[im2, jp2] + u[ip2, jp2] + u[ip2, jm2]        +
                3 * (u[im2, jm1] + u[im2, jp1] + u[ip2, jp1] + u[ip2, jm1])  +
                3 * (u[im1, jm2] + u[im1, jp2] + u[ip1, jp2] + u[ip1, jm2])  +
                4 * (u[im2, j] + u[i, jp2] + u[ip2, j] + u[i, jm2])          + 
                12* (u[im1, j] + u[i, jp1] + u[ip1, j] + u[i, jm1])          +
                9 * (u[im1, jm1] + u[im1, jp1] + u[ip1, jp1] + u[ip1, jm1])  +

                16 *u[i, j]
            ) / 144
    return u_filtre_3dx

def filter_delta_4dx_trapz_2D(u):
    """ Filtre (méthode des trapèzes composite ) avec conditions périodiques cas delta = 4dx """
    u_filtre_4dx = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # indices périodiques en y
            if j == 0:
                jm2 = ny - 2
                jm1 = ny - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == 1:
                jm2 = ny - 1
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
            elif j == ny - 1:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = 0
                jp2 = 1
            elif j == ny - 2:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = 0
            else:
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
            # indices périodiques en x
            if i == 0:
                im2 = nx - 2
                im1 = nx - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == 1:
                im2 = nx - 1
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
            elif i == nx - 1:
                im2 = i - 2
                im1 = i - 1
                ip1 = 0
                ip2 = 1
            elif i == nx - 2:
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = 0
            else:
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2

            u_filtre_4dx[i, j] = (
               u[im2, jm2] + u[im2, jp2] + u[ip2, jm2] + u[ip2, jp2]         +         # Coins extrêmes 
               2 * (u[im2, jm1] + u[im2, jp1] + u[ip2, jp1] + u[ip2, jm1])   + 
               2 * (u[im1, jm2] + u[im1, jp2] + u[ip1, jp2] + u[ip1, jm2])   +         # carré i-2  i+2  j-2   j+2
               2 * (u[im2, j] + u[i, jp2] + u[ip2, j] + u[i, jm2])           + 

               4 * (u[im1, jm1] + u[im1, jp1] + u[ip1, jp1] + u[ip1, jm1])   +         # carré  i-1  i+1  j-1   j+1
               4 * (u[im1, j] + u[i, jp1] + u[ip1, j] + u[i, jm1])           + 

               4 * u[i, j]                                                            # centre                                                        
            ) / 64.0
    return u_filtre_4dx


def filter_delta_6dx_trapz_2D(u):
    """Filtre (méthode des trapèzes composites) Δ=6dx, conditions périodiques, écriture compacte et structurée."""
    u_filtre_6dx = np.zeros(u.shape)
    nx, ny = u.shape
    for i in range(nx):
        for j in range(ny):
            # indices périodiques en y
            if j == 0:
                jm3 = ny - 3
                jm2 = ny - 2
                jm1 = ny - 1
                jp1 = j + 1
                jp2 = j + 2
                jp3 = j + 3
            elif j == 1:
                jm3 = ny - 2
                jm2 = ny - 1
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
                jp3 = j + 3
            elif j == 2:
                jm3 = ny - 1
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
                jp3 = j + 3
            elif j == ny - 3:
                jm3 = j - 3
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
                jp3 = 0
            elif j == ny - 2:
                jm3 = j - 3
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = 0
                jp3 = 1
            elif j == ny - 1:
                jm3 = j - 3
                jm2 = j - 2
                jm1 = j - 1
                jp1 = 0
                jp2 = 1
                jp3 = 2
            else:
                jm3 = j - 3
                jm2 = j - 2
                jm1 = j - 1
                jp1 = j + 1
                jp2 = j + 2
                jp3 = j + 3
            # indices périodiques en x
            if i == 0:
                im3 = nx - 3
                im2 = nx - 2
                im1 = nx - 1
                ip1 = i + 1
                ip2 = i + 2
                ip3 = i + 3
            elif i == 1:
                im3 = nx - 2
                im2 = nx - 1
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
                ip3 = i + 3
            elif i == 2:
                im3 = nx - 1
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
                ip3 = i + 3
            elif i == nx - 3:
                im3 = i - 3
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
                ip3 = 0
            elif i == nx - 2:
                im3 = i - 3
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = 0
                ip3 = 1
            elif i == nx - 1:
                im3 = i - 3
                im2 = i - 2
                im1 = i - 1
                ip1 = 0
                ip2 = 1
                ip3 = 2
            else:
                im3 = i - 3
                im2 = i - 2
                im1 = i - 1
                ip1 = i + 1
                ip2 = i + 2
                ip3 = i + 3

            u_filtre_6dx[i, j] = (
                u[im3, jm3] + u[im3, jp3] + u[ip3, jm3] + u[ip3, jp3] +             # Coins extrêmes 
                2 * (u[im2, jm3] + u[im2, jp3] + u[ip2, jp3] + u[ip2, jm3] )   +
                2 * (u[im1, jm3] + u[im1, jp3] + u[ip1, jp3] + u[im1, jm3] )   +
                2 * (u[im3, jm2] + u[im3, jp2] + u[ip3, jp2] + u[ip3, jm2] )   +
                2 * (u[im3, jm1] + u[im3, jp1] + u[ip3, jp1] + u[ip3, jm1] )   +    # carré i-3  i+3  j-3 j+p  
                2 * (u[im3, j] + u[i, jp3] + u[ip3, j] + u[i, jm3] )           +

               
                4 * (u[im2, jm2] + u[im2, jp2] + u[ip2, jp2] + u[ip2, jm2] )   +
                4 * (u[im2, jm1] + u[im2, jp1] + u[ip2, jp1] + u[ip2, jm1] )   +
                4 * (u[im1, jm2] + u[im1, jp2] + u[ip1, jp2] + u[ip1, jm2] )   +   # carré  i-2  i+2    j-2    j+2  
                4 * (u[im2, j] + u[i, jp2] + u[ip2, j] + u[i, jm2] )           + 

                4 * (u[im1, jm1] + u[im1, jp1] + u[ip1, jp1] + u[ip1, jm1] )   +   # carré i-1   i+1    j-1    j+1          
                4 * (u[im1, j] + u[i, jp1] + u[ip1, j] + u[i, jm1] )           +

                4 * u[i, j]                                                       #    centre 
            ) / 144.0  
    return u_filtre_6dx



def compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y):
    argx = KXS * delta_x*0.5
    argy = KYS * delta_y*0.5
    fft_us = np.fft.fftshift(np.fft.fftn(signal))
    fft_filtre_s = np.sinc(argx/np.pi) * np.sinc(argy/np.pi)
    fft_convo_s = fft_filtre_s * fft_us
    u_filtered = np.fft.ifftn(np.fft.ifftshift(fft_convo_s)).real
    return u_filtered

N_list = [16, 32, 64, 128, 256,512]

# calcul des  erreurs  max et erreur L2

err_list_dx  =  []
err_list_2dx =  []
err_list_3dx =  []
err_list_4dx =  []
err_list_6dx =  []


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
    signal_filtered_trapz_6dx = filter_delta_6dx_trapz_2D(signal)


    # Erreur relative  quadratique (L2) pour chaque cas

    # delta = dx
    epsilon_dx = np.linalg.norm(signal_filtered_trapz - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_dx.append(epsilon_dx)

    # delta = 2dx
    epsilon_2dx = np.linalg.norm(signal_filtered_trapz_2dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_2dx.append(epsilon_2dx)

    # delta = 3dx
    epsilon_3dx = np.linalg.norm(signal_filtered_trapz_3dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_3dx.append(epsilon_3dx)

    # delta = 4dx
    epsilon_4dx = np.linalg.norm(signal_filtered_trapz_4dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_4dx.append(epsilon_4dx)


    # delta = 6dx
    epsilon_6dx = np.linalg.norm(signal_filtered_trapz_6dx - signal_filtered) / np.linalg.norm(signal_filtered)
    err_list_6dx.append(epsilon_6dx)

ordre2 = 1 / np.asarray(N_list)**2

coef2 = err_list_dx[0] / ordre2[0]
coef2_2dx = err_list_2dx[0] / ordre2[0]
coef2_3dx = err_list_3dx[0] / ordre2[0]
coef2_4dx = err_list_4dx[0] / ordre2[0]
coef2_6dx = err_list_6dx[0] / ordre2[0]

plt.figure()
plt.title(r"Erreur $L^2$ avec méthode des trapèzes composites" ) 
plt.loglog(N_list, err_list_dx, "s--", label=r"Trapz $\Delta=dx$ ")
plt.loglog(N_list, err_list_2dx, "s--", label=r"Trapz $\Delta=2dx$ ")
plt.loglog(N_list, err_list_3dx, "s--", label=r"Trapz $\Delta=3dx$ ")
plt.loglog(N_list, err_list_4dx, "s--", label=r"Trapz $\Delta=4dx$ ")
plt.loglog(N_list, err_list_6dx, "s--", label=r"Trapz $\Delta=6dx$ ")

plt.loglog(N_list, coef2_6dx*ordre2,  "8-.", label="Ordre 2" )
plt.xlabel(r" $N$")
plt.ylabel(r" $\epsilon(N)$ ")
#plt.title(r"Erreur  $L^2$" )
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.legend()
plt.show()

