import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lamda = 8 # rata-rata kedatangan
jamKerja = 12
hari = 30
totalJamKerja = jamKerja * hari

data = poisson.rvs(lamda, size=totalJamKerja)

unique, counts = np.unique(data, return_counts = True)
freq = dict(zip(unique, counts))

plt.bar(unique, counts, color='blue')
plt.title('Distribusi Poisson : Jumlah Kedatangan Pelanggan selama 30 Hari')
plt.xlabel('Jumlah Kedatangan Pelanggan')
plt.ylabel('Frekuensi')
plt.show()

tidakAdaKedatangan = poisson.pmf(0, lamda)
LebihDari10 = 1 - poisson.cdf(10, lamda)

theoriticalDistribusi = [poisson.pmf(k, lamda) * totalJamKerja for k in range(max(unique)+1)]
simulated_counts = np.bincount(data)

plt.figure(figsize=(12, 6))
plt.bar(range(len(simulated_counts)), simulated_counts, alpha=0.5, label='Simulasi', color='red')
plt.bar(range(len(theoriticalDistribusi)), theoriticalDistribusi, alpha=0.5, label='Teoritis', color='blue')

plt.title('Perbandingan Distribusi Simulasi dan Teoritis')
plt.xlabel('Jumlah Pelanggan')
plt.ylabel('Frekuensi')
plt.legend()
plt.grid(axis='y')
plt.show()