import numpy as np
import matplotlib.pyplot as plt

# Chargement des données
data_32 = np.loadtxt('les_Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat')
dnsdata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/Re1600_N256_cfl03_tf15.dat') 
dnsdata_512 = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/dnsRe1600_N512_cfl03_tf9.dat')
#data_brachet = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/Brachet_Fig4_Re1600.dat')
data_vanr = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/vanrees_Fig3_N512_Re1600.dat', comments='#')

# Extraction des colonnes
time_32, MeanKEDR_32 = data_32[:, 0], data_32[:, 2]
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]
dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]
dnstime_512, dnsMeanKEDR_512 = dnsdata_512[:, 0], dnsdata_512[:, 2]
#time_brachet, MeanKEDR_brachet = data_brachet[:, 0], data_brachet[:, 1]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 2]

# Masque pour tracer van rees jusqu'à 15s 
mask = (time_vanr >= 0) & (time_vanr <= 15)
time_vanr = time_vanr[mask]
MeanKEDR_vanr = MeanKEDR_vanr[mask]

# Création de la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps 
plt.title(r'LES MM, $\overline{\Delta} = \Delta x$', fontsize=16)
plt.plot(time_32, MeanKEDR_32, color='C3', label=r'MM $32^3$')
plt.plot(time_64, MeanKEDR_64, color='C0', label=r'MM $64^3$')
plt.plot(time_128, MeanKEDR_128, color='C1', label=r'MM $128^3$')
plt.plot(time_256, MeanKEDR_256, color='C2', label=r'MM $256^3$')
plt.plot(dnstime_256, dnsMeanKEDR_256, 'r-.', label=r'DNS $256^3$') 
plt.plot(dnstime_512, dnsMeanKEDR_512, 'r:', label=r'DNS $512^3$')

# Solution de Brachet en pointillés noirs
#plt.plot(time_brachet, MeanKEDR_brachet, linestyle='--', color='purple', 
#         label=r'Brachet', lw=1.5, marker='s', markersize=4, markevery=5)
#plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5, 
#         marker='o', markersize=4, markevery=30)

plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5)
# Ajout des titres et labels en mode mathématique
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel(r'$\langle 2\nu S_{ij}S_{ij} \rangle$', fontsize=14)

# Configuration de l'échelle des axes et de la grille
#plt.grid(True, alpha=0.3)
#plt.xlim(0, 15)  # Ajuster selon vos données

# Ajout d'une légende (déplacé APRÈS les plots)
plt.legend(fontsize=12, loc='best')

# Ajustement des marges
plt.tight_layout()

# Sauvegarde de la figure
plt.savefig('les_mean_kedr_MM.png', dpi=300, bbox_inches='tight')

# Affichage de la figure
plt.show()
