
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift

# =============================================
# 1. Définition des deux filtres
# =============================================

def filtre_trapezes_2D(u):
    """  filtre (méthode des trapèzes) """
    u_filtre = np.zeros_like(u)
    nx, ny = u.shape
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u_filtre[i,j] = (
                u[i-1, j-1] + u[i+1, j-1] + u[i+1, j+1] + u[i-1, j+1]  # Diagonales (poids 1)
                + 2*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])     # Voisins directs (poids 2)
                + 4*u[i, j]                                             # Centre (poids 4)
            ) / 16
    return u_filtre

def filtre_notus_2D(u, coeff=4.0):
    """ filtre dans notus """
    u_filtre = np.zeros_like(u)
    nx, ny = u.shape
    coeff2 = coeff**2
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u_filtre[i,j] = -(
                u[i-1, j-1] + u[i+1, j-1] + u[i+1, j+1] + u[i-1, j+1]  # Diagonales
                + coeff*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1]) # Voisins directs
                + coeff2*u[i, j]                                        # Centre
            ) / (2 + coeff)**2 + u[i, j]                                # Normalisation + terme original
    return u_filtre

# =============================================
# 2. Génération d'un champ sinusoïdal 2D
# =============================================
nx, ny = 256, 256
x = np.linspace(0, 4*np.pi, nx)
y = np.linspace(0, 4*np.pi, ny)
X, Y = np.meshgrid(x, y)

# Fréquences spatiales (kx, ky)
kx, ky = 2, 3
u = np.sin(kx*X + ky*Y)  # Champ sinusoïdal

# Ajout d'un bruit haute fréquence pour tester le filtrage
noise = 0.1 * np.random.randn(nx, ny)
u_noisy = u   + noise

# =============================================
# 3. Application des filtres
# =============================================
u_filtre_trap = filtre_trapezes_2D(u_noisy)
u_filtre_notus = filtre_notus_2D(u_noisy)

# =============================================
# 4. Analyse spectrale (FFT)
# =============================================
def compute_spectrum(u):
    fft_u = fft2(u)
    return fftshift(np.abs(fft_u))

spectrum_original = compute_spectrum(u_noisy)
spectrum_trap = compute_spectrum(u_filtre_trap)
spectrum_notus_filtre = compute_spectrum(u_filtre_notus)

# =============================================
# 5. Visualisation
# =============================================
fig, axes = plt.subplots(3, 3, figsize=(15, 12))

# Champ original bruité
axes[0, 0].imshow(u_noisy, cmap='viridis')
axes[0, 0].set_title("Signal original bruité (espace réel)")
axes[1, 0].imshow(np.log(spectrum_original), cmap='hot')
axes[1, 0].set_title("Spectre filtré (original)   (log)")

# Filtre trapèzes
axes[0, 1].imshow(u_filtre_trap, cmap='viridis')
axes[0, 1].set_title("Filtre trapèzes (espace réel)")
axes[1, 1].imshow(np.log(spectrum_trap), cmap='hot')
axes[1, 1].set_title("Spectre filtré (trapèzes)")

# Filtre  dans notus 
axes[0, 2].imshow(u_filtre_notus, cmap='viridis')
axes[0, 2].set_title("Filtre dans notus  (espace réel)")
axes[1, 2].imshow(np.log(spectrum_notus_filtre), cmap='hot')
axes[1, 2].set_title("Spectre filtré (dans notus)")

# Coupes 1D pour comparer les filtres
axes[2, 0].plot(u_noisy[nx//2, :], label="Original bruité", alpha=0.7)
axes[2, 0].plot(u_filtre_trap[nx//2, :], label="Trapèzes")
axes[2, 0].plot(u_filtre_notus[nx//2, :], label="filtre dans notus")
axes[2, 0].legend()
axes[2, 0].set_title("Coupe 1D en x")

# Différence entre les deux filtres
axes[2, 1].plot(u_filtre_trap[nx//2, :] - u_filtre_notus[nx//2, :], 'r')
axes[2, 1].set_title("Différence (Trapèzes - Original)")

#plt.tight_layout()
#plt.show()
plt.savefig('filter.png')
