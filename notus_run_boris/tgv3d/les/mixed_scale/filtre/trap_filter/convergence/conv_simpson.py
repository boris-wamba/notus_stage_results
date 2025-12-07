import numpy as np
import matplotlib.pyplot as plt

def filter_delta_2dx_simpson_2D(u):
    """Filtre (Simpson simple 2D) avec conditions périodiques"""
    u_filtre_simp = np.zeros(u.shape)
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
        
            u_filtre_simp[i, j] = (
                u[im1, jm1] + u[ip1, jm1] + u[im1, jp1] + u[ip1, jp1] +  # coins
                4 * (u[im1, j] + u[ip1, j] + u[i, jm1] + u[i, jp1]) +    # bords
                16 * u[i, j]  # centre
            ) / 36.0
    return u_filtre_simp


def filter_delta_2dx_simp_composite_2D(u):
    """  Filtre (méthode des trapèzes) avec conditions périodiques """
    u_filtre_simp_composite = np.zeros(u.shape)
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
            u_filtre_simp_composite[i, j] = (
                u[im1, jm1] + u[ip1, jm1] + u[im1, jp1] + u[ip1, jp1] +  # coins
                2 * (u[im1, j] + u[ip1, j] + u[i, jm1] + u[i, jp1]) +  # bords
                4 * u[i, j]  # centre
            ) / 16.0
    return u_filtre_simp_composite




def compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y):
    argx = KXS * delta_x*0.5
    argy = KYS * delta_y*0.5
    fft_us = np.fft.fftshift(np.fft.fftn(signal))
    fft_filtre_s = np.sinc(argx/np.pi) * np.sinc(argy/np.pi)
    fft_convo_s = fft_filtre_s * fft_us
    u_filtered = np.fft.ifftn(np.fft.ifftshift(fft_convo_s)).real
    return u_filtered

N_list = [16, 32, 64, 128, 256, 512]
err_list_2dx    = []
err_list_composite_2dx = []

for N in N_list:
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

    delta_x = 2 * dx
    delta_y = 2 * dy

    signal_filtered_exact_2dx = compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y) 

    signal_filtered_simp_2dx = filter_delta_2dx_simpson_2D(signal)
    signal_filtered_simp_composite_2dx = filter_delta_2dx_simp_composite_2D(signal)

    epsilon_2dx = np.linalg.norm(signal_filtered_simp_2dx - signal_filtered_exact_2dx) / np.linalg.norm(signal_filtered_exact_2dx)
    epsilon_composite_2dx = np.linalg.norm(signal_filtered_simp_composite_2dx - signal_filtered_exact_2dx) / np.linalg.norm(signal_filtered_exact_2dx)

    err_list_2dx.append(epsilon_2dx)
    err_list_composite_2dx.append(epsilon_composite_2dx)



ordre2 = 1 / np.asarray(N_list)**2
ordre3 = 1 / np.asarray(N_list)**3

coef2_2dx = err_list_2dx[0] / ordre2[0]
coef3_2dx = err_list_2dx[0] / ordre3[0]

plt.figure()
plt.title(r"Erreur $L^2$ pour $\Delta=2dx$: Simpson simple")
plt.loglog(N_list, err_list_2dx, "s-.", label=r"Simpson simple  $\Delta=2dx$") 
plt.loglog(N_list, err_list_composite_2dx, "s-.", label=r"Simpson composite $\Delta=2dx$ ")
plt.loglog(N_list, coef2_2dx*ordre2, "8-.", label=r"Ordre 2")
plt.loglog(N_list, coef3_2dx*ordre3, "d-.", label=r"Ordre 3")
plt.xlabel(r" $N$")
plt.ylabel(r" $\epsilon(N)$ ")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.legend()
plt.show()

