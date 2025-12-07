import numpy as np
import matplotlib.pyplot as plt

# Chargargement des données
#data_64 = np.loadtxt('Re400_N64_cfl03_tf15.dat')
#

o2o2data_256 = np.loadtxt('/home/bkwamba/Notus_run/TGV3D/DNS/Re1600/schemas/o2_centered_o2_centered/Re1600_N256_cfl03_tf15.dat')
o2o4data_256 = np.loadtxt('/home/bkwamba/Notus_run/TGV3D/DNS/Re1600/schemas/o2_centered_o4_centerd/Re1600_N256_cfl03_tf15.dat')
o4o2data_256 = np.loadtxt('/home/bkwamba/Notus_run/TGV3D/DNS/Re1600/schemas/o4_centered o2_centered/Re1600_N256_cfl03_tf15_o4_o2.dat')
o4o4data_256 = np.loadtxt('/home/bkwamba/Notus_run/TGV3D/DNS/Re1600/schemas/o4_centered o4_centered/Re1600_N256_cfl03_tf15_o4_o4.dat')

#Chargement des données  DNS 
#dnsdata_64 = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/dnsRe1600_N64_cfl03_tf9.dat')
#dnsdata_128 = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/dnsRe1600_N128_cfl03_tf9.dat')
#dnsdata_256 = np.loadtxt('/home/bkwamba/TGV3D_DNS_DATA/dnsRe1600_N256_cfl03_tf9.dat')




# Extraction des colonnes
#time_64, MeanKEDR_64 = data_64[:, 0], data_64[:, 2]
#time_128, MeanKEDR_128 = data_128[:, 0], data_128[:, 2]
o2o2time_256, o2o2MeanKEDR_256 = o2o2data_256[:, 0], o2o2data_256[:, 2]
o2o4time_256, o2o4MeanKEDR_256 = o2o4data_256[:, 0], o2o4data_256[:, 2]
o4o2time_256, o4o2MeanKEDR_256 = o4o2data_256[:, 0], o4o2data_256[:, 2]
o4o4time_256, o4o4MeanKEDR_256 = o4o4data_256[:, 0], o4o4data_256[:, 2]


#Extraction des données dns 
#dnstime_64, dnsMeanKEDR_64 = dnsdata_64[:, 0], dnsdata_64[:, 2]
#dnstime_128, dnsMeanKEDR_128 = dnsdata_128[:, 0], dnsdata_128[:, 2]
#dnstime_256, dnsMeanKEDR_256 = dnsdata_256[:, 0], dnsdata_256[:, 2]



# Créeation la figure
plt.figure(figsize=(7, 7))

# Tracer de MeanKEDR en fonction du temps
#plt.plot(time_64, MeanKEDR_64, label='DNS N=64')
#plt.plot(time_128, MeanKEDR_128, label='DNS N=128')
plt.plot(o2o2time_256, o2o2MeanKEDR_256, label='o2_cent o2_cent')
plt.plot(o2o4time_256, o2o4MeanKEDR_256, label='o2_cent o4_cent')
plt.plot(o4o2time_256, o4o2MeanKEDR_256, label='o4_cent o2_cent')
plt.plot(o4o4time_256, o4o4MeanKEDR_256, label='o4_cent o4_cent')



#plt.plot(dnstime_64, dnsMeanKEDR_64, label='dnsMeanKEDR (N=64)')
#plt.plot(dnstime_128, dnsMeanKEDR_128, label='dnsMeanKEDR (N=128)')
#plt.plot(dnstime_256, dnsMeanKEDR_256, label='dnsMeanKEDR (N=256)')




# Ajout des titres et labels
plt.title('MeanKEDR DNS')
plt.xlabel('Time')
plt.ylabel('MeanKEDR')

# Ajout d'une légende
plt.legend()

# Ajout d'une grille
plt.grid()

# Sauvegarde de la figure
plt.savefig('MEAN_KEDR_sheme_effet_on_DNS')

# Afficharge de  la figure
plt.show()
