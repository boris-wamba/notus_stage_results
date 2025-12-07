import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données
data_64 = np.loadtxt('Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('Re1600_N128_cfl03_tf15.dat')
data_256 = np.loadtxt('Re1600_N256_cfl03_tf15.dat')
data_512 = np.loadtxt('Re1600_N512_cfl03_tf9.dat', comments = '#') 

data_128_smg = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/smagorinsky/Re1600/delta_dx/les_Re1600_N128_cfl03_tf15.dat')
data_128_mm = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/mixed_scale/re1600/delta_dx/les_Re1600_N128_cfl03_tf15.dat')


data_vanr = np.loadtxt('van_rees.dat', comments='#')




# Extraction des colonnes
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]
time_512, MeanKEDR_512 = data_512[:, 0], data_512[:, 1]
time_vr, MeanKEDR_vr = data_vanr[:, 0], data_vanr[:, 1]

time_128_smg, MeanKEDR_128_smg = data_128_smg[:, 0], data_128_smg[:, 2]
time_128_mm, MeanKEDR_128_mm = data_128_mm[:, 0], data_128_mm[:, 2]


# Créeation la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps

plt.plot(time_64, MeanKEDR_64,label=r'DNS $64^3$')
plt.plot(time_128, MeanKEDR_128, label=r'DNS $128^3$')
plt.plot(time_256, MeanKEDR_256, label=r'DNS $256^3$')
plt.plot(time_512, MeanKEDR_512, linestyle='--', color='r', label=r'DNS $512^3$')

plt.plot(time_vr, MeanKEDR_vr, 'k--', label=r'Van Rees', lw=1.5)

plt.legend(loc='upper left', bbox_to_anchor=(0.02, 1.0),fontsize=14 ,borderpad=1.5, handletextpad=1.5, markerscale=2, edgecolor='black', framealpha=1)
# Ajout des titres et labels en mode mathématique
plt.xlabel('$temps(s)$',fontsize=18)
plt.ylabel('$ < 2\\nu S_{ij}S_{ij} > $',fontsize=18)

# Ajout d'une légende
#plt.legend()

# Ajout d'une grille

# Sauvegarde de la figure
plt.savefig('mean_kedr_dns.png')



plt.figure(figsize=(7, 7))
plt.plot(time_128, MeanKEDR_128, color= 'C1',  label=r'DNS $128^3$')
plt.plot(time_128_smg, MeanKEDR_128_smg, color = 'pink',  label=r'SMG $128^3$')
plt.plot(time_128_mm, MeanKEDR_128_mm,color = 'purple',  label=r'MM $128^3$')
plt.plot(time_vr, MeanKEDR_vr, 'k--', label=r'Van Rees', lw=1.5)
plt.xlabel('$temps(s)$',fontsize=18)
plt.ylabel('$ < 2\\nu S_{ij}S_{ij} > $',fontsize=18)
plt.legend(loc='upper left', bbox_to_anchor=(0.02, 1.0),fontsize=14 ,borderpad=1.5, handletextpad=1.5, markerscale=2, edgecolor='black', framealpha=1)
plt.savefig('comparison_LES_DNS_SMG_MM_on_mesh_N128.png')

# Afficharge de  la figure
plt.show()
