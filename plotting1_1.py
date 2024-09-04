import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("denne koden kjører!")

data = pd.read_csv("../rrsalltest0.txt", index_col=False)
#print (data) #= printe data med matrise struktur
y1 = data[' max_cdom_conc'].values # .values converts the data into a NumPy data [ARRAY], this strips away the data frames row and colum labels, leaving just the data itself in an array 
y2 = data[' max_flag_c'].values
y3 = data[' max_diatom_c'].values

rrs = data.values[:, 0:-3] #henter verdiene i hele matrisen, uten å få med hederne og gjør det om til numPy. her også arbeider .vulue. Stripper dataen fra strukturen og lar kun et 2D array med tall stå igjenn
print(rrs)
#print(y1)
#print(y2)
#print(y3)

#y3 = data[' max_diatom_c'].values

print("\n linjen er kjørt")

# Definer bølgelengdene
wavelengths = np.arange(402.5, 697.6, 5)  # Lager en array med bølgelengder fra 402.5 nm til 607.5 nm
# sjekker at antall bølgelengder er riktig
#assert len(wavelengths) == 63, "Antallet bølgelengder stemmer ikke overens med forventet verdi på 63"

# Hent ut dataen fra data.values[:, 0:-3]
#rrs = data.values[:, 0:-3]  # Rrs verdier, hver rad representerer et spektrum

# Opprett plottet
plt.figure(figsize=(10, 6))

# Plott hver rad i rrs-arrayet som en separat linje
for i in range(rrs.shape[0]):
    plt.plot(wavelengths, rrs[i, :], color='blue', alpha=0.01)  # alpha=0.01 for å redusere intensiteten på hver linje

# Legg til akselabels og tittel
plt.xlabel('Wavelength (nm)')
plt.ylabel('Rrs (sr⁻¹)')
plt.title('Wavelength vs. Rrs')

# Viser plottet
plt.show()