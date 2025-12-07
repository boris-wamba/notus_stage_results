import numpy as np
import matplotlib.pyplot as plt

def filter_delta_dx_trapz_2D(u):
    """  Filtre (méthode des trapèzes) avec conditions périodiques """
    u_filtre = np.zeros(u.shape)
    # u_filtre = -100.
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
X, Y = np.meshgrid(x, y, indexing="ij")
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
KXS, KYS = np.meshgrid(kxs, kxs, indexing="ij")


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
#for i in range(1, 2):
#for i in range(1, 3):
for i in range(1, 5):
    delta_x = i*dx
    delta_y = i*dy
    signal_filtered = compute_exact_convolution_top_hat(signal, KXS, KYS, delta_x, delta_y)
    signal_filtered_trapz = filter_delta_dx_trapz_2D(signal)
    signal_filtered_trapz_2dx = filter_delta_2dx_trapz_2D(signal)
    signal_filtered_trapz_3dx = filter_delta_3dx_trapz_2D(signal)
    signal_filtered_trapz_4dx = filter_delta_4dx_trapz_2D(signal)


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
    plt.plot(signal_filtered_trapz[Nx//2, :], label="Filtré trapz (delta =  dx)" )
    plt.plot(signal_filtered_trapz_2dx[Nx//2, :], label="Filtré trapz (delta = 2 dx)" )
    plt.plot(signal_filtered_trapz_3dx[Nx//2, :], label="Filtré trapz (delta = 3 dx)" )
    plt.plot(signal_filtered_trapz_4dx[Nx//2, :], label="Filtré trapz (delta = 4 dx)" )
    #plt.plot(signal_filtered[0, :], "-.", label="Filtré exact bord")
    #plt.plot(signal_filtered_trapz[0, :], "-.", label="Filtré trapz (delta=  dx) bord" )
    plt.legend()

    #plt.figure()
    #plt.title("CLs , Delta = %s dx " % i)
    #plt.plot(signal_filtered_trapz[0, :], "-.", label="trapz gauche")
    #plt.plot(signal_filtered_trapz[Nx-1, :], "-.", label="trapz droite")
    #plt.plot(signal_filtered_trapz[:,0], "-.", label="trapz bas")
    #plt.plot(signal_filtered_trapz[:,Ny-1], "-.", label="trapz haut")
    #plt.legend()




plt.show()

