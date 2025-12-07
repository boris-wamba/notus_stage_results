import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
data32_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/smagorinsky/re1600/delta_2pi_32/les_Re1600_N256_cfl03_tf15.dat')
data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat')

data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat')
dnsdata_512 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/Re1600_N512_cfl03_tf9.dat', comments= '#')
dnsdata_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/Re1600_N256_cfl03_tf15.dat')
data_vanr = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/van_rees.dat', comments='#')




# Extraction des colonnes
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
time32_256, MeanKEDR32_256 = data32_256[:, 0], data32_256[:, 2]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]
dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]
dnstime_512, dnsMeanKEDR_512 = dnsdata_512[:, 0], dnsdata_512[:, 1]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 1]


# Créeation la figure
plt.figure(figsize=(7, 7))


plt.plot(time_64, MeanKEDR_64,label=r'$\overline{\Delta}_{0} = \Delta x_0 = \frac{2\pi}{64}$,     $64^3$')
plt.plot(time_128, MeanKEDR_128, label=r'$\Delta x_1= \frac{\Delta x_0}{2}$,     $128^3$')
plt.plot(time_256, MeanKEDR_256, label=r'$\Delta x_2 = \frac{\Delta x_0}{4}$,     $256^3$')
plt.plot(time32_256, MeanKEDR32_256,linestyle='--', color='C2', label=r'$\overline{\Delta}_{0}=\frac{2\pi}{32}  , \Delta x= \frac{\overline{\Delta }_{0}}{8}  $, $256^3$')
plt.plot(dnstime_256, dnsMeanKEDR_256,'r-.', label='DNS $ 256^3 $')
#plt.plot(dnstime_512, dnsMeanKEDR_512, 'r:',label='DNS $ 512^3$')
plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5)

# Ajout des titres et labels en mode mathématique
plt.xlabel('$temps(s)$', fontsize=18)
plt.ylabel('$< 2\\nu S_{ij}S_{ij} > $', fontsize=18)

# Ajout d'une légende
plt.legend(loc='upper left', bbox_to_anchor=(0.02, 1.0),fontsize=11.0,borderpad=1.0, handletextpad=1.5, markerscale=2, edgecolor='black', framealpha=1)


# Ajout d'une légende
plt.legend()

# Ajout d'une grille

# Sauvegarde de la figure
plt.savefig('mean_kedr_smg_2pi_over_64.png')

# Afficharge de  la figure
plt.show()
