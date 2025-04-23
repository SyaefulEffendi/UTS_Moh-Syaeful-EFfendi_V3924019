import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data_pasien.csv", sep=';')

total_pasien = len(data)
print(f"\nTotal pasien: {total_pasien}")

print("\nDistribusi data:")
tidak_menderita = len(data[data["Menderita_Penyakit"] == "Tidak"]) 
print(f"Pasien yang tidak menderita penyakit: {tidak_menderita} ({tidak_menderita/total_pasien:.3%})")

positif_dan_menderita = len(data[(data["Hasil_Tes"] == "Positif") & (data["Menderita_Penyakit"] == "Ya")])
print(f"Pasien dengan hasil tes positif dan menderita penyakit: {positif_dan_menderita} ({positif_dan_menderita/total_pasien:.3%})")

negatif_dan_menderita = len(data[(data["Hasil_Tes"] == "Negatif") & (data["Menderita_Penyakit"] == "Ya")])
print(f"Pasien dengan hasil tes negatif dan menderita penyakit: {negatif_dan_menderita} ({negatif_dan_menderita/total_pasien:.3%})")

tabel = pd.crosstab(data['Hasil_Tes'], data['Menderita_Penyakit'])
print("\nTabel kontingensi:")
print(tabel)

positif_total = len(data[data["Hasil_Tes"] == "Positif"])
penyakit_given_positif = len(data[(data["Hasil_Tes"] == "Positif") & (data["Menderita_Penyakit"] == "Ya")]) / positif_total
print(f"\na. P(Menderita Penyakit | Hasil Tes Positif) = {penyakit_given_positif:.4f} = {penyakit_given_positif:.2%}")

negatif_total = len(data[data["Hasil_Tes"] == "Negatif"])
tidak_penyakit_given_negatif = len(data[(data["Hasil_Tes"] == "Negatif") & (data["Menderita_Penyakit"] == "Tidak")]) / negatif_total
print(f"b. P(Tidak Menderita Penyakit | Hasil Tes Negatif) = {tidak_penyakit_given_negatif:.4f} = {tidak_penyakit_given_negatif:.2%}")

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Hasil_Tes", hue="Menderita_Penyakit")
plt.title("Distribusi Hasil Tes dan Status Penyakit")
plt.xlabel("Hasil Tes")
plt.ylabel("Jumlah Pasien")
plt.legend(title="Menderita Penyakit")
plt.tight_layout()
plt.savefig('distribusi_tes.png')
plt.show()

plt.figure(figsize=(8, 5))
prob_values = [penyakit_given_positif, tidak_penyakit_given_negatif]
prob_labels = ["P(Sakit|Positif)", "P(Tidak Sakit|Negatif)"]
plt.bar(prob_labels, prob_values)
plt.title("Probabilitas Kondisional")
plt.ylabel("Probabilitas")
plt.ylim(0, 1)
plt.savefig('probabilitas.png')
plt.show()