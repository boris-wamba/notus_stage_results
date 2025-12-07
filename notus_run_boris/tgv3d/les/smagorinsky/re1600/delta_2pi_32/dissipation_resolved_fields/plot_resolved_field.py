import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données 
data_32 = np.loadtxt('Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('Re1600_N128_cfl03_tf15.dat')
data_256 = np.loadtxt('Re1600_N256_cfl03_tf15.dat') 


#to compute dns date with sqrt(2) in strain rate magnitude 
dnsdata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/filtered_dns_velocity/log.Re1600_N256_cfl03_tf15.dat') 
ndata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/mixed_model/re1600/delta_2pi_64/sqrt2_nu_exact/les_Re1600_N256_cfl03_tf15.dat')

data_vanr = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/vanrees_Fig3_N512_Re1600.dat', comments='#')

# Physical parameter
Re = 1600.0
nu = 1.0 / Re

#Chargement des données  DNS 



# Extraction des colonnes 
time_32, MeanKEDR_32 = data_32[:, 0], data_32[:, 2]
time_64 , MeanKEDR_64 , nu64 , pk64 = data_64[:, 0] , data_64[:, 2] , data_64[:, 4] , data_64[:, 5]
time_128, MeanKEDR_128, nu128, pk128 = data_128[:, 0], data_128[:, 2], data_128[:, 4] , data_128[:, 5]
time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]

dnstime_256, dnsMeanKEDR_256, dnsfMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2], dnsdata_256[:, 4]
ntime_256, nMeanKEDR_256, nu256, pk256, s256 = ndata_256[:, 0], ndata_256[:, 2], ndata_256[:, 4], ndata_256[:, 5], ndata_256[:, 6] 



# compute  S:S for dns filtered velocity 
S_S_dns_filtered = dnsfMeanKEDR_256 / (2 * nu) 
# Compute  ε_sgs_exact
epsilon_sgs_exact = dnsMeanKEDR_256 - dnsfMeanKEDR_256 



plt.figure(1, figsize=(7, 7))
plt.title(r'LES smg, $\overline{\Delta}_{0} = \frac{2\pi}{32}$, $2 \nu \bar{S}_{ij}\bar{S}_{ij}$ (LES)') 

plt.plot(time_32, MeanKEDR_32,color='C3',  label=r'$\overline{\Delta}_{0} = \Delta x_0 = \frac{2\pi}{32}$,     $32^3$')
plt.plot(time_64, MeanKEDR_64,color='C0', label=r'$\Delta x_1 = \frac{\Delta x_0}{2}$, $64^3$')
plt.plot(time_128, MeanKEDR_128,color='C1', label=r'$\Delta x_1 = \frac{\Delta x_0}{4}$, $128^3$')
plt.plot(time_256, MeanKEDR_256,color='C2', label=r'$ \Delta x_2 = \frac{\Delta x_0}{8}$, $256^3$')
plt.plot(dnstime_256, dnsfMeanKEDR_256,'r-.', label=r'$2\nu\bar{S}_{ij}\bar{S}_{ij}$(dns$256^3 $)')


plt.xlabel('$time(s)$',fontsize=14)
plt.ylabel(r'$< 2\nu\bar{S}_{ij}\bar{S}_{ij}>$',fontsize=14)
#plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
#           markerscale=2, edgecolor='black', framealpha=1)
plt.legend()



plt.figure(2, figsize=(7, 7))
plt.title(r'LES smg, $\overline{\Delta}_{0} = \frac{2\pi}{64}$,  $\epsilon_{exact}$ vs  $2\nu_t\bar{S}_{ij}\bar{S}_{ij}$')
plt.plot(ntime_256, pk256, color='C6', label=r'$2\nu_t\bar{S}_{ij}\bar{S}_{ij}(les)$')
plt.plot(dnstime_256, epsilon_sgs_exact, color='C7', label=r'$\epsilon_{dns} - \bar{\epsilon}_{dns}$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$<2\nu_t\bar{S}_{ij}\bar{S}_{ij}>$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5, 
           markerscale=2, edgecolor='black', framealpha=1)


plt.figure(3, figsize=(7, 7))
plt.title(r'LES smg, $\overline{\Delta}_{0} = \frac{2\pi}{64}$, $\nu_t$')
plt.plot(ntime_256, nu256, color='C6', label=r'$\nu_t$ $256^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$\nu_t$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5, 
           markerscale=2, edgecolor='black', framealpha=1)


# Sauvegarde des figures
plt.figure(1)
plt.savefig('mean_kedr_les_smg_revolved_fields_2pi_32.png')

plt.figure(2)
plt.savefig('turbulence_productio_smg_2pi_32.png')

plt.figure(3)
plt.savefig('turbulence_production_smg_2pi_32.png')
plt.show()
