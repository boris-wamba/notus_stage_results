import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données
data_32 = np.loadtxt('les_Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
#data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat')
data_512 = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/dnsRe1600_N512_cfl03_tf9.dat')
#data_brachet = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/Brachet_Fig4_Re1600.dat')
data_vanr = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/vanrees_Fig3_N512_Re1600.dat', comments='#')


# Extraction des colonnes
time_32, MeanKEDR_32 = data_32[:, 0], data_32[:,2]
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
#time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]
time_512, MeanKEDR_512 = data_512[:, 0], data_512[:, 2]
#time_brachet, MeanKEDR_brachet = data_brachet[:, 0], data_brachet[:, 1]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 2]

#masque pour tracer van rees jusqu' a 15s 
mask = (time_vanr >= 0) & (time_vanr <= 15)
time_vanr=time_vanr[mask]
MeanKEDR_vanr = MeanKEDR_vanr[mask]


# Créeation la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps
plt.plot(time_32, MeanKEDR_32, label='$32^3$')
plt.plot(time_64, MeanKEDR_64, label='$64^3$')
plt.plot(time_128, MeanKEDR_128, label='$128^3$')
#plt.plot(time_256, MeanKEDR_256, label='$256^3$')
plt.plot(time_512, MeanKEDR_512,'r-.', label='$512^3 $')
# Solution de Brachet en pointillés noirs
#plt.plot(time_brachet, MeanKEDR_brachet, 'k--', label='Brachet')
plt.plot(time_vanr, MeanKEDR_vanr, 'k', label='Van Rees')

# Ajout des titres et labels en mode mathématique
plt.xlabel('$time(s)$', fontsize=12)
plt.ylabel('$\\langle 2\\nu S_{ij}S_{ij} \\rangle$', fontsize=12)

# Ajout d'une légende
plt.legend()

# Sauvegarde de la figure
plt.savefig('mean_kedr_wale_2pi_32')

# Afficharge de la figure
plt.show()
