import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données 
#data_32 = np.loadtxt('les_Re1600_N32_cfl03_tf15.dat')
data_64 = np.loadtxt('les_Re1600_N64_cfl03_tf15.dat')
data_128 = np.loadtxt('les_Re1600_N128_cfl03_tf15.dat')
#data_256 = np.loadtxt('les_Re1600_N256_cfl03_tf15.dat') 

dnsdata_64 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/Re1600_N64_cfl03_tf15.dat')
dnsdata_128 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/Re1600_N128_cfl03_tf15.dat')
dnsdata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/Re1600_N256_cfl03_tf15.dat')

data_vanr = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/vanrees_Fig3_N512_Re1600.dat', comments='#')


#Chargement des données  DNS 
#data_brachet = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/Brachet_Fig4_Re1600.dat')


 
#time_32, MeanKEDR_32 = data_32[:, 0], data_32[:, 2]
time_64  , MeanKEDR_64  , nu64 , pk64  , s64  = data_64[:, 0] , data_64[:, 2] , data_64[:, 4] , data_64[:, 5] , data_64[:, 6]
time_128 , MeanKEDR_128 , nu128, pk128 , s128 = data_128[:, 0], data_128[:, 2], data_128[:, 4] , data_128[:, 5]   , data_128[:, 6]
#time_256, MeanKEDR_256 = data_256[:, 0], data_256[:, 2]


dnstime_64, dnsMeanKEDR_64 = dnsdata_64[:, 0], dnsdata_64[:, 2]
dnstime_128, dnsMeanKEDR_128 = dnsdata_128[:, 0], dnsdata_128[:, 2]
dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]
time_vanr, MeanKEDR_vanr = data_vanr[:, 0], data_vanr[:, 2]
#time_brachet, MeanKEDR_brachet = data_brachet[:, 0], data_brachet[:, 1]

#masque pour tracer van rees jusqu' a 15s
mask = (time_vanr >= 0) & (time_vanr <= 15)
time_vanr=time_vanr[mask]
MeanKEDR_vanr = MeanKEDR_vanr[mask]



plt.figure(1, figsize=(7, 7))
plt.title(r'LES MM, $\overline{\Delta}_{0} = \frac{2\pi}{32}$, same value throughout all simulations')


#plt.plot(time_32, MeanKEDR_32,color='C3',  label=r'$\overline{\Delta}_{0} = \Delta x_0 = \frac{2\pi}{32}$,     $32^3$')
plt.plot(time_64, MeanKEDR_64,color='C0', label=r'$\Delta x_1= \frac{\Delta x_0}{2}$,     $64^3$')
plt.plot(time_128, MeanKEDR_128,color='C1', label=r'$\Delta x_2 = \frac{\Delta x_0}{4}$,     $128^3$')
#plt.plot(time_256, MeanKEDR_256,color='C2', label=r'$ \Delta x_3 = \frac{\Delta x_0}{8}$,    $256^3$')
plt.plot(dnstime_256, dnsMeanKEDR_256,'r-.', label='DNS $ 256^3 $')

plt.plot(time_64, pk64, color='C6', linestyle = '--' ,  label=r'pk, $64^3$')
plt.plot(time_128, pk128, color='C7',linestyle = '--',  label=r'pk, $128^3$')

#plt.plot(time_brachet, MeanKEDR_brachet, linestyle='--', color='purple', label=r'Brachet', lw=1.5, marker='s', markersize=4, markevery=5)
#plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5, marker='o',markersize=4, markevery=30)
plt.plot(time_vanr, MeanKEDR_vanr, 'k--', label=r'Van Rees', lw=1.5)

plt.xlabel('$time(s)$',fontsize=14)
plt.ylabel('$\\langle 2\\nu S_{ij}S_{ij} \\rangle$',fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)


plt.figure(2, figsize=(7, 7))
plt.title(r'turbulent viscosity $\nu_t$ ')
plt.plot(time_64, nu64, color='C6', label=r'$64^3$')
plt.plot(time_128, nu128, color='C7', label=r'$128^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$turbulent viscosity$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5, 
           markerscale=2, edgecolor='black', framealpha=1)


plt.figure(3, figsize=(7, 7))
plt.title(r'Production term  $\nu_t S_{ij}S_{ij}$')
plt.plot(time_64, pk64, color='C6', label=r'$64^3$')
plt.plot(time_128, pk128, color='C7', label=r'$128^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$\nu_{t}S_{ij}S_{ij}$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5, 
           markerscale=2, edgecolor='black', framealpha=1)


plt.figure(4, figsize=(7, 7))
plt.title(r'normalized turbulent viscosity $\frac{\nu_t}{\nu}$')
plt.plot(time_64, nu64 * 1600 , color='C6', label=r'$64^3$')
plt.plot(time_128, nu128 * 1600 , color='C7', label=r'$128^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$normalized viscosity$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)

s64_exact = (dnsMeanKEDR_64 * 800 / s64) - 1 
s128_exact = (dnsMeanKEDR_128 * 800 / s128) - 1

plt.figure(5, figsize=(7, 7))
plt.title(r'exact turbulent viscosity $\nu[\frac{S_{ij}}{\bar{S}_{ij}}]-1$')
plt.plot(time_64, s64_exact , color='C6', label=r'$64^3$')
plt.plot(time_128, s64_exact , color='C7', label=r'$128^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$normalized viscosity$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)



plt.figure(6, figsize=(7, 7))
plt.title(r'exact turbulent viscosity $[\frac{S_{ij}}{\bar{S}_{ij}}]-1$')
plt.plot(time_64, s64_exact  * 1600 , color='C6', label=r'$64^3$')
plt.plot(time_128, s64_exact * 1600 , color='C7', label=r'$128^3$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$normalized viscosity$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)



# Sauvegarde des figures
plt.figure(1)
plt.savefig('mean_kedr_les_mm_2pi_64.png')

plt.figure(2)
plt.savefig('turbulent_viscosity.png')

plt.figure(3)
plt.savefig('turbulence_production.png')

plt.figure(4)
plt.savefig('normalized_viscosity.png')

plt.figure(5)
plt.savefig('exact_nu_sgs.png')

plt.figure(6)
plt.savefig('exact_normalized_nu_sgs.png')


plt.show()
