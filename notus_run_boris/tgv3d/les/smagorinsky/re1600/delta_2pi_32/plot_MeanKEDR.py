import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données
data_32 = np.loadtxt('les_Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat')
#Chargement des données  DNS 
data_brachet = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/Brachet_Fig4_Re1600.dat')
dnsdata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/Re1600_N256_cfl03_tf15.dat')
data_vanr = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/vanrees_Fig3_N512_Re1600.dat', comments='#')



# Extraction des colonnes
time_32, MeanKEDR_32 = data_32[:, 0], data_32[:, 2]
time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]

dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 2]
time_brachet, MeanKEDR_brachet = data_brachet[:, 0], data_brachet[:, 1]
#masque pour tracer van rees jusqu' a 15s
mask = (time_vanr >= 0) & (time_vanr <= 15)
time_vanr=time_vanr[mask]
MeanKEDR_vanr = MeanKEDR_vanr[mask]


# Créeation la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps 
#plt.legend(fontsize=22)
#plt.tile('$\overline{\Delta}_{0}=\frac{2\pi}{32}$')
plt.title(r'LES SMG, $\overline{\Delta}_{0} = \frac{2\pi}{32}$, same value throughout all simulations ')

plt.plot(time_32, MeanKEDR_32,color='C3',   label=r'$\overline{\Delta}_{0} = \Delta x_0 = \frac{2\pi}{32}$,    $32^3$')
plt.plot(time_64, MeanKEDR_64, color='C0',label=r'$ \Delta x_1= \frac{\Delta x_0}{2}$,    $64^3$')
plt.plot(time_128, MeanKEDR_128,color='C1', label=r'$ \Delta x_2= \frac{\Delta x_0}{4}$,    $128^3$')
plt.plot(time_256, MeanKEDR_256,color='C2', label=r'$ \Delta x_3 = \frac{\Delta x_0}{8}$,    $256^3$')



plt.plot(dnstime_256, dnsMeanKEDR_256,'r-.', label='DNS $ 256^3 $')
#plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5, marker='o',markersize=4, markevery=30)
#plt.plot(time_brachet, MeanKEDR_brachet, linestyle='--', color='purple', label=r'Brachet', lw=1.5, marker='s', markersize=4, markevery=5)

plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5)
#plt.plot(time_brachet, MeanKEDR_brachet, linestyle='--', color='purple', label=r'Brachet')


plt.legend(
    fontsize=26,
    frameon=True,
    borderpad=1.5,       # + d'espace dans le cadre
    handletextpad=1.5,   # + d'espace entre ligne et texte
    markerscale=2,       # Symboles 2x plus gros
    edgecolor='black',
    framealpha=1
)

# Ajout des titres et labels en mode mathématique

plt.ylabel('$\\langle 2\\nu S_{ij}S_{ij} \\rangle$', fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=16)
# Ajout d'une légende
plt.legend()

# Ajout d'une grille

# Sauvegarde de la figure
plt.savefig('mean_kedr_smg_2pi_over_32.png')

# Afficharge de  la figure
plt.show()
