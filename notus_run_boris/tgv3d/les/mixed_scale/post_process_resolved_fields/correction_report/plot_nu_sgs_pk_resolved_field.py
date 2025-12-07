import numpy as np
import matplotlib.pyplot as plt

# chargement  des données
smg_2pi_32_data_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/smagorinsky/re1600/delta_2pi_32/dissipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')
smg_dx_data_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/smagorinsky/re1600/delta_dx/dissipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')
mm_2pi_64_data_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/mixed_scale/re1600/delta_2pi_64/dissip_champ_resolus/les_Re1600_N256_cfl03_tf3.dat')
mm_dx_data_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/les/mixed_scale/re1600/delta_dx/dissipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')

# données pour calculer la viscosité et le terme de production pour delta = 2pi/64  MM 
datanu = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/data_resolved_fieds_2pi_64/nu.dat')
datapk = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/data_resolved_fieds_2pi_64/pk.dat')



# données dns
dnsdata_256 = np.loadtxt('/home/pove/Téléchargements/notus_run_boris/tgv3d/dns/re1600/o2_centered_o2_centered/nu_exact/log.Re1600_N256_cfl03_tf15.dat')


Re = 1600.0
nu = 1.0 / Re

# extraction des données
smg_2pi_32_time_256, smg_2pi_32_nu256, smg_2pi_32_pk256 = smg_2pi_32_data_256[:, 0], smg_2pi_32_data_256[:, 4], smg_2pi_32_data_256[:, 5]
smg_dx_time_256, smg_dx_nu256, smg_dx_pk256 = smg_dx_data_256[:, 0], smg_dx_data_256[:, 4], smg_dx_data_256[:, 5]
mm_2pi_64_time_256, mm_2pi_64_nu256, mm_2pi_64_pk256 = mm_2pi_64_data_256[:, 0], mm_2pi_64_data_256[:, 4], mm_2pi_64_data_256[:, 5]
mm_dx_time_256, mm_dx_nu256, mm_dx_pk256 = mm_dx_data_256[:, 0], mm_dx_data_256[:, 4], mm_dx_data_256[:, 5]

dnstime_256, dnsMeanKEDR_256, dnsfMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2], dnsdata_256[:, 4]

# extraction des données pour calculer la viscosité et le terme de production pour delta = 2pi/64  MM 
nutime , nu64 = datanu[:, 0], datanu[:, 1]
pktime , pk = datapk[:, 0], datapk[:, 1]



# calcul sw S:S Champ DNS 
S_S_dns_filtered = dnsfMeanKEDR_256 / (2 * nu)
# Calcul de ε_sgs_exact
epsilon_sgs_exact = dnsMeanKEDR_256 - dnsfMeanKEDR_256
epsilon = 1e-12
S_S_safe = np.where(S_S_dns_filtered > epsilon, S_S_dns_filtered, epsilon)
nu_sgs_exact = epsilon_sgs_exact / (2 * S_S_safe)
nu_sgs_exact_clean = np.clip(nu_sgs_exact, -1, 10)  # valeurs extremes
nu_sgs_exact_clean = np.nan_to_num(nu_sgs_exact_clean, nan=0.0, posinf=0.0, neginf=0.0)


#plot
# terme de production filtre constant
plt.figure(1, figsize=(7, 7))
plt.plot(smg_2pi_32_time_256, smg_2pi_32_pk256,
         color='C4', marker='o', markersize=10,  markevery=0.1,
         label=r'SMG $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{32}$')
#plt.plot(nutime, nu64,
#         color='C5', marker='s', markersize=10,markevery=0.1,
#         label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$')
plt.plot(pktime, pk,
         color='C5', marker='s', markersize=10,markevery=0.1,
         label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$')

plt.plot(dnstime_256, epsilon_sgs_exact,
         color='C7', marker='^', markersize=10,markevery=0.1,
         label=r'$\epsilon_{dns} - \bar{\epsilon}_{dns}$')
# Mettre l'axe des y en échelle logarithmique
plt.yscale('log')
plt.xlabel('$temps(s)$', fontsize=20)
plt.ylabel(r' Log $<2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}>$', fontsize=18)
plt.legend(fontsize=20, frameon=True, borderpad=1, handletextpad=1,
           markerscale=2, edgecolor='black', framealpha=1)
plt.savefig('turbulence_production_2pi_tf15.png')


#terme de production filtre variable 
plt.figure(2, figsize=(7, 7))
plt.plot(smg_dx_time_256, smg_dx_pk256,
         color='C6', marker='o', markersize=12, markevery=0.1,
         label=r'SMG $\bar{\Delta}= \Delta x$')
plt.plot(mm_dx_time_256, mm_dx_pk256,
         color='C8', marker='s', markersize=12, markevery=0.1,
         label=r'MM $\bar{\Delta}= \Delta x$')
plt.plot(dnstime_256, epsilon_sgs_exact,
         color='C7', marker='^', markersize=12,markevery=0.1,
         label=r'$\epsilon_{dns} - \bar{\epsilon}_{dns}$')
# Axe Y en échelle logarithmique
plt.yscale('log')
plt.xlabel('$temps(s)$', fontsize=22)
plt.ylabel(r'Log $<2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}>$', fontsize=22)
plt.legend(fontsize=20, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)
plt.savefig('turbulence_production_dx_tf15.png')



#viscosité turbulente filtre constant
plt.figure(3, figsize=(7, 7))
plt.plot(smg_2pi_32_time_256, smg_2pi_32_nu256,
         color='C4', marker='o', markersize=10, markevery=0.1,
         label=r'SMG $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{32}$')
#plt.plot(pktime, pk,
#         color='C5', marker='s', markersize=10,markevery=0.1,
#         label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$') 
plt.plot(nutime, nu64,
         color='C5', marker='s', markersize=10,markevery=0.1,
         label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$')

plt.plot(dnstime_256, nu_sgs_exact_clean,
         color='C7', linewidth=1, marker='^', markersize=10, markevery=0.1,
         label=r'$<\nu_{sgs}^{idéal}>$ ($256^3$)')
# Échelle log en y
plt.yscale('log')
plt.xlabel('$temps(s)$', fontsize=22)
plt.ylabel(r'Log $<\nu_{sgs}>$', fontsize=22)
plt.legend(fontsize=17, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)
plt.savefig('turbulence_viscosity_2pi_tf15.png')







plt.figure(4, figsize=(7, 7))
# Courbe SMG avec marqueurs espacés automatiquement (10 marqueurs répartis)
plt.plot(smg_dx_time_256, smg_dx_nu256,
         color='C6', marker='o', markersize=12, markevery=0.1,
         label=r'SMG $\bar{\Delta}= \Delta x$')
# Courbe MM avec marqueurs espacés automatiquement
plt.plot(mm_dx_time_256, mm_dx_nu256,
         color='C8', marker='s', markersize=12, markevery=0.1,
         label=r'MM $\bar{\Delta}= \Delta x$')

plt.plot(dnstime_256, nu_sgs_exact_clean,
         color='C7', linewidth=1, marker='^', markersize=10, markevery=0.1,
         label=r'$<\nu_{sgs}^{idéal}>$ ($256^3$)')

# Axe Y en échelle log
plt.yscale('log')
plt.xlabel('$temps(s)$', fontsize=22)
plt.ylabel(r'Log $<\nu_{sgs}>$', fontsize=22)
plt.legend(loc = 'lower right', fontsize=17, frameon=True, borderpad=1.0, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)
plt.savefig('turbulence_viscosity_dx_tf15.png')
            
plt.show()






