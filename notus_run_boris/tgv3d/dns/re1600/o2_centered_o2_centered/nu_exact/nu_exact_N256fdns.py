import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Load data
data_256 = np.loadtxt('log.Re1600_N256_cfl03_tf15.dat')
ndata_256 = np.loadtxt('/home/bkwamba/notus_run/tgv3d/les/mixed_model/re1600/delta_2pi_64/sqrt2_nu_exact/les_Re1600_N256_cfl03_tf15.dat')

time_256, MeanKEDR_256, fMeanKEDR_256 = data_256[:, 0], data_256[:, 2], data_256[:, 4]
ntime_256, nMeanKEDR_256, nu256, pk256, s256 = ndata_256[:, 0], ndata_256[:, 2], ndata_256[:, 4], ndata_256[:, 5], ndata_256[:, 6] 

# Physical parameter 
Re = 1600.0
nu = 1.0 / Re  #

# Calcul de ν_sgs_exact 

# ε_sgs_exact = ε_DNS - ε_res_DNS
# ν_sgs_exact = ε_sgs_exact / (2 * S:S)


# ε_res_DNS = 2 * nu * S(ū_DNS):S(ū_DNS)
# then  S(ū_DNS):S(ū_DNS) = ε_res_DNS / (2 * nu)

# compute  S:S for dns filtered velocity 

S_S_dns_filtered = fMeanKEDR_256 / (2 * nu)

# Compute  ε_sgs_exact

epsilon_sgs_exact = MeanKEDR_256 - fMeanKEDR_256

# Compute exact  ν_sgs_exact 
# avoid division by  zero

epsilon = 1e-12
S_S_safe = np.where(S_S_dns_filtered > epsilon, S_S_dns_filtered, epsilon)

nu_sgs_exact = epsilon_sgs_exact / (2 * S_S_safe)

# management of spurious values 
nu_sgs_exact_clean = np.clip(nu_sgs_exact, -1, 10)  # Limit amazing boundary values 
nu_sgs_exact_clean = np.nan_to_num(nu_sgs_exact_clean, nan=0.0, posinf=0.0, neginf=0.0)

# Figures
plt.figure(figsize=(7, 7))
plt.title(r'Exact SGS viscosity, $\nu_{sgs}^{exact} = \frac{\varepsilon_{DNS} - \varepsilon_{res,DNS}}{2\bar{S}_{ij}\bar{S}_{ij}}$')
plt.plot(time_256, nu_sgs_exact_clean, color='red', linewidth=2, label=r'$\nu_{sgs}^{exact}$ ($256^3$)') 
#plt.plot(ntime_256, nu256, color='C8', linewidth=2,  label=r'$\nu_{sgs}^{notus}$ ($256^3$)')
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel(r'$\nu_{sgs}^{exact}$', fontsize=14)
plt.legend(fontsize=12, frameon=True, borderpad=1.5, handletextpad=1.5, 
           markerscale=2, edgecolor='black', framealpha=1)
#plt.grid(True, alpha=0.3)

# numerical parameters 
#plt.text(0.02, 0.98, f'Re = {Re}, ν = {nu:.6f}', transform=plt.gca().transAxes, 
#         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('exact_nu_sgs_onN256_mesh.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistiques
print(f"Statistiques de ν_sgs_exact:")
print(f"Moyenne: {np.mean(nu_sgs_exact_clean):.6e}")
print(f"Écart-type: {np.std(nu_sgs_exact_clean):.6e}")
print(f"Minimum: {np.min(nu_sgs_exact_clean):.6e}")
print(f"Maximum: {np.max(nu_sgs_exact_clean):.6e}")
print(f"ν_moléculaire: {nu:.6e}")
print(f"Ratio ν_sgs/ν moyen: {np.mean(nu_sgs_exact_clean)/nu:.3f}")
