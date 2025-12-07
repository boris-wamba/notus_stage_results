import numpy as np
import matplotlib.pyplot as plt

# download data
smg_2pi_32_data_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/smagorinsky/Re1600/delta=2pi_32/dissipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')
smg_dx_data_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/smagorinsky/Re1600/smg_les_tf15/diisipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')
mm_2pi_64_data_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/mixed_model/re1600/delta_2pi_64/sqrt2_nu_exact/les_Re1600_N256_cfl03_tf15.dat')
mm_dx_data_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/mixed_model/re1600/mm_tf15/dissipation_resolved_fields/Re1600_N256_cfl03_tf15.dat')

# to compute dns date with sqrt(2) in strain rate magnitude
dnsdata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/dns/re1600/schemas/o2_centered_o2_centered/filtered_dns_velocity/log.Re1600_N256_cfl03_tf15.dat')

# Physical parameter
Re = 1600.0
nu = 1.0 / Re

# data extraction
smg_2pi_32_time_256, smg_2pi_32_nu256, smg_2pi_32_pk256 = smg_2pi_32_data_256[:, 0], smg_2pi_32_data_256[:, 4], smg_2pi_32_data_256[:, 5]
smg_dx_time_256, smg_dx_nu256, smg_dx_pk256 = smg_dx_data_256[:, 0], smg_dx_data_256[:, 4], smg_dx_data_256[:, 5]
mm_2pi_64_time_256, mm_2pi_64_nu256, mm_2pi_64_pk256 = mm_2pi_64_data_256[:, 0], mm_2pi_64_data_256[:, 4], mm_2pi_64_data_256[:, 5]
mm_dx_time_256, mm_dx_nu256, mm_dx_pk256 = mm_dx_data_256[:, 0], mm_dx_data_256[:, 4], mm_dx_data_256[:, 5]

dnstime_256, dnsMeanKEDR_256, dnsfMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2], dnsdata_256[:, 4]

# compute S:S for dns filtered velocity
S_S_dns_filtered = dnsfMeanKEDR_256 / (2 * nu)
# Compute ε_sgs_exact
epsilon_sgs_exact = dnsMeanKEDR_256 - dnsfMeanKEDR_256
epsilon = 1e-12
S_S_safe = np.where(S_S_dns_filtered > epsilon, S_S_dns_filtered, epsilon)
nu_sgs_exact = epsilon_sgs_exact / (2 * S_S_safe)
nu_sgs_exact_clean = np.clip(nu_sgs_exact, -1, 10)  # Limit amazing boundary values
nu_sgs_exact_clean = np.nan_to_num(nu_sgs_exact_clean, nan=0.0, posinf=0.0, neginf=0.0)

plt.figure(1, figsize=(7, 7))
plt.title(r'LES production term $2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}$ vs $\epsilon_{exact} =\epsilon_{dns} - \bar{\epsilon}_{dns}$ $256^3$')
plt.plot(smg_2pi_32_time_256, smg_2pi_32_pk256, color='C4', label=r'SMG $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{32}$')
plt.plot(mm_2pi_64_time_256, mm_2pi_64_pk256, color='C5', label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$')
plt.plot(dnstime_256, epsilon_sgs_exact, color='C7', label=r'$\epsilon_{dns} - \bar{\epsilon}_{dns}$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$<2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}>$', fontsize=14)
plt.legend(fontsize= 10, frameon=True, borderpad=1, handletextpad=1,
           markerscale=2, edgecolor='black', framealpha=1)

plt.figure(2, figsize=(7, 7))
plt.title(r'LES production term $2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}$ vs $\epsilon_{exact} =\epsilon_{dns} - \bar{\epsilon}_{dns}$ $256^3$')
plt.plot(smg_dx_time_256, smg_dx_pk256, color='C6', label=r'SMG $\bar{\Delta}= \Delta x$')
plt.plot(mm_dx_time_256, mm_dx_pk256, color='C8', label=r'MM $\bar{\Delta}= \Delta x$')
plt.plot(dnstime_256, epsilon_sgs_exact, color='C7', label=r'$\epsilon_{dns} - \bar{\epsilon}_{dns}$')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$<2\nu_{sgs}\bar{S}_{ij}\bar{S}_{ij}>$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)

plt.figure(3, figsize=(7, 7))
plt.title(r'LES turbulent viscosity $\nu_{sgs}$ $256^3$')
plt.plot(smg_2pi_32_time_256, smg_2pi_32_nu256, color='C4', label=r'SMG $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{32}$')
plt.plot(mm_2pi_64_time_256, mm_2pi_64_nu256, color='C5', label=r'MM $\bar{\Delta}= \Delta x_0 = \frac{2\pi}{64}$')
plt.plot(dnstime_256, nu_sgs_exact_clean, color='C7', linewidth=2, label=r'$\nu_{sgs}^{exact}$ ($256^3$)')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$\nu_{sgs}$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)

plt.figure(4, figsize=(7, 7))
plt.title(r'LES turbulent viscosity $\nu_{sgs}$ $256^3$')
plt.plot(smg_dx_time_256, smg_dx_nu256, color='C6', label=r'SMG $\bar{\Delta}= \Delta x$')
plt.plot(mm_dx_time_256, mm_dx_nu256, color='C8', label=r'MM $\bar{\Delta}= \Delta x$')
#plt.plot(dnstime_256, nu_sgs_exact_clean, color='C7', linewidth=2, label=r'$\nu_{sgs}^{exact}$ ($256^3$)')
plt.xlabel('$time(s)$', fontsize=14)
plt.ylabel(r'$\nu_{sgs}$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5,
           markerscale=2, edgecolor='black', framealpha=1)

# storages figures
plt.figure(1)
plt.savefig('turbulence_production_2pi_tf15.png')

plt.figure(2)
plt.savefig('turbulence_production_dx_tf15.png')

plt.figure(3)
plt.savefig('turbulence_viscosity_2pi_tf15.png')

plt.figure(4)
plt.savefig('turbulence_viscosity_dx_tf15.png')

plt.show()
