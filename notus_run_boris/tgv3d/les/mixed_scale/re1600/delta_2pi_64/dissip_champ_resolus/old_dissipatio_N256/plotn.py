import numpy as np
import matplotlib.pyplot as plt

# Chargement du fichier (en ignorant la ligne de commentaire commençant par #)
data = np.loadtxt("les_Re1600_N256_cfl03_tf15.dat", comments="#")

# Extraction des colonnes
time = data[:, 0]
MeanKE = data[:, 1]
MeanKEDR = data[:, 2]
MeanP = data[:, 3]

# Figure 1 : MeanKE
plt.figure(figsize=(7,4))
plt.plot(time, MeanKE)
plt.xlabel("time")
plt.ylabel("MeanKE")
plt.grid(True)
plt.tight_layout()
plt.show()

# Figure 2 : MeanKEDR
plt.figure(figsize=(7,4))
plt.plot(time, MeanKEDR)
plt.xlabel("time")
plt.ylabel("MeanKEDR")
plt.grid(True)
plt.tight_layout()
plt.show()

# Figure 3 : MeanP
plt.figure(figsize=(7,4))
plt.plot(time, MeanP)
plt.xlabel("time")
plt.ylabel("MeanP")
plt.grid(True)
plt.tight_layout()
plt.show()

