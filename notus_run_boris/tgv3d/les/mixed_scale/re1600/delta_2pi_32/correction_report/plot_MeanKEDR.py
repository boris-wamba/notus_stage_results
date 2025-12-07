import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données 
data_32 = np.loadtxt('les_Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
dnsdata_512 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/Re1600_N512_cfl03_tf9.dat', comments= '#')
dnsdata_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/Re1600_N256_cfl03_tf15.dat')
data_vanr = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/mean_kedr_dns/van_rees.dat', comments='#')



# Extraction des colonnes 
time_32, MeanKEDR_32 = data_32[:, 0], data_32[:, 2]
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]
dnstime_512, dnsMeanKEDR_512 = dnsdata_512[:, 0], dnsdata_512[:, 1]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 1]



#Extraction des données dns 


# Créeation la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps

plt.plot(time_32, MeanKEDR_32,color='C3',  label=r'$\overline{\Delta}_{0} = \Delta x_0 = \frac{2\pi}{32}$,     $32^3$')
plt.plot(time_64, MeanKEDR_64,color='C0', label=r'$\Delta x_1= \frac{\Delta x_0}{2}$,     $64^3$')
plt.plot(time_128, MeanKEDR_128,color='C1', label=r'$\Delta x_2 = \frac{\Delta x_0}{4}$,     $128^3$')
plt.plot(dnstime_256, dnsMeanKEDR_256,'r-.', label='DNS $ 256^3 $')
#plt.plot(dnstime_512, dnsMeanKEDR_512, 'r:',label='DNS $ 512^3$')
plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5)

# Ajout des titres et labels en mode mathématique
plt.xlabel('$temps(s)$', fontsize=18)
plt.ylabel('$< 2\\nu S_{ij}S_{ij} > $', fontsize=18)

# Ajout d'une légende
plt.legend(loc='lower center', 
           bbox_to_anchor=(0.55, 0.02),  # (x, y) - 0.5 pour le centre horizontal, 0.02 pour le bas
           fontsize=9.0,
           borderpad=1.0, 
           handletextpad=1.5, 
           markerscale=2, 
           edgecolor='black', 
           framealpha=1)

# Sauvegarde de la figure
plt.savefig('mean_kedr_mm_2pi_over_32.png')

# Afficharge de  la figure
plt.show()
