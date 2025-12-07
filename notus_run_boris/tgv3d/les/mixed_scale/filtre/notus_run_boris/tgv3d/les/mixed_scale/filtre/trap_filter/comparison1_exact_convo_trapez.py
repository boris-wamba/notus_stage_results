import numpy as np
import matplotlib.pyplot as plt

def filter_delta_dx_trapz_2D(u):
    """  Filtre (méthode des trapèzes) avec conditions périodiques """
    u_filtre = np.zeros(u.shape)
    # u_filtre = -100.
    nx, ny = u.shape
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            u_filtre[i,j] = (
                    u[i-1, j-1] + u[i+1, j-1] + u[i+1, j+1] + u[i-1, j+1]  # Diagonales (poids 1)
                    + 2*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])     # Voisins directs (poids 2)
                    + 4*u[i, j]                                             # Centre (poids 4)
                    ) / 16

    # bas + coins
    print('bas')
    i=0
    im1=nx-1
    for j in range(ny):
        jp1 = j+1
        jm1 = j-1
        if j == 0: # gauche
            jm1=ny-1
        elif (j==ny-1): # droite
            jp1=0
        else: # autre
            jm1 = j-1
        u_filtre[i,j] = (
                    u[im1, jm1] + u[i+1, jm1] + u[i+1, jp1] + u[im1, jp1]  # Diagonales (poids 1)
                    + 2*(u[i+1, j] + u[im1, j] + u[i, jp1] + u[i, jm1])     # Voisins directs (poids 2)
                    + 4*u[i, j]                                             # Centre (poids 4)
                    ) / 16
    # haut + coins
    i=nx-1
    ip1=0
    print('haut')
    for j in range(ny):
        jp1 = j+1
        jm1 = j-1
        if j == 0: # gauche
            jm1=ny-1
        elif (j==ny-1): # droite
            jp1=0
        else: # autre
            jm1 = j-1
        u_filtre[i,j] = (
                    u[i-1, jm1] + u[ip1, jm1] + u[ip1, jp1] + u[i-1, jp1]  # Diagonales (poids 1)
                    + 2*(u[ip1, j] + u[i-1, j] + u[i, jp1] + u[i, jm1])     # Voisins directs (poids 2)
                    + 4*u[i, j]                                             # Centre (poids 4)
                    ) / 16
    # gauche ss coin
    j=0
    jm1=ny-1
    print('gauche')
    for i in range(1,nx-1):
            u_filtre[i,j] = (
                    u[i-1, jm1] + u[i+1, jm1] + u[i+1, j+1] + u[i-1, j+1]  # Diagonales (poids 1)
                    + 2*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, jm1])     # Voisins directs (poids 2)
                    + 4*u[i, j]                                             # Centre (poids 4)
                    ) / 16
    # droite ss coin
    j=nx-1
    jp1=0
    print('droite')
    for i in range(1,nx-1):
            u_filtre[i,j] = (
                    u[i-1, j-1] + u[i+1, j-1] + u[i+1, jp1] + u[i-1, jp1]  # Diagonales (poids 1)
                    + 2*(u[i+1, j] + u[i-1, j] + u[i, jp1] + u[i, j-1])     # Voisins directs (poids 2)
                    + 4*u[i, j]                                             # Centre (poids 4)
                    ) / 16
    return u_filtre

def compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y):
    argx = KXS * delta_x*0.5
    argy = KYS * delta_y*0.5
    fft_us = np.fft.fftshift(np.fft.fftn(signal))
    fft_filtre_s = np.sinc(argx/np.pi) * np.sinc(argy/np.pi)
    fft_convo_s = fft_filtre_s * fft_us
    # convolution exact
    u_filtered = np.fft.ifftn(np.fft.ifftshift(fft_convo_s)).real
    return u_filtered

L = 2*np.pi
N = 64
# N = 128
Nx, Ny = N, N
x = np.linspace(0, L, Nx)
y = np.linspace(0, L, Ny)
X, Y = np.meshgrid(x, y)
dx = x[1] - x[0]
dy = y[1] - y[0]
k_cutoff_x = 0.5*(2*np.pi)/dx
k_cutoff_y = 0.5*(2*np.pi)/dy
dk = (Nx*dx)**-1
# identic as using np.fft routines !
# kx = np.arange(0,k_cutoff_x+dk, dk)
# ky = np.arange(0,k_cutoff_y+dk, dk)
kxs = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Nx,dx))
kys = (2*np.pi)*np.fft.fftshift(np.fft.fftfreq(Ny,dy))
KXS, KYS = np.meshgrid(kxs, kxs)


# Fréquences spatiales (kx, ky)
kx, ky = 2, 3
# signal
# u = np.sin(kx*X) + np.sin(ky*Y)
signal = np.sin(kx*X + ky*Y)
# + noise
noise = 0.1 * np.random.randn(Nx, Ny)
signal = signal + noise

## numpy def : sin(k*Δ/2)/(k*Δ/2) = np.sinc((k*Δ/2)/π)
# Filter size
for i in range(1, 3):
    delta_x = i*dx
    delta_y = i*dy
    signal_filtered = compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y)
    signal_filtered_trapz = filter_delta_dx_trapz_2D(signal)
    # plt.figure()
    # plt.title("signal non filtré")
    # plt.imshow(u)
    # plt.colorbar()
    # # plt.show()

    # plt.figure()
    # plt.title("signal filtré (Apres FFT + IFFT) Delta = %s dx " % i)
    # plt.imshow(u_filtered)
    # plt.colorbar()

    # plt.figure()
    # plt.title("Error u_filtré - u")
    # plt.imshow(np.abs(u_filtered-u))
    # plt.colorbar()

    plt.figure()
    plt.title("Coupe 1D en x, Delta = %s dx " % i)
    plt.plot(signal[Nx//2, :], label="Original bruité")
    plt.plot(signal_filtered[Nx//2, :], label="Filtré exact")
    plt.plot(signal_filtered_trapz[Nx//2, :], label="Filtré trapz")
    plt.plot(signal_filtered[0, :], "-.", label="Filtré exact bord")
    plt.plot(signal_filtered_trapz[0, :], "-.", label="Filtré trapz bord")
    plt.legend()

plt.show()

