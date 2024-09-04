import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Plotting1_2 kjører")

data = pd.read_csv("../rrsalltest0.txt", index_col=False)
#print (data) #= printe data med matrise struktur
y1 = data[' max_cdom_conc'].values # .values converts the data into a NumPy data [ARRAY], this strips away the data frames row and colum labels, leaving just the data itself in an array 
y2 = data[' max_flag_c'].values
y3 = data[' max_diatom_c'].values

rrs = data.values[:, 0:-3] #henter verdiene i hele matrisen, uten å få med hederne og gjør det om til numPy. her også arbeider .vulue. Stripper dataen fra strukturen og lar kun et 2D array med tall stå igjenn
#print(rrs)
#print(y1)
#print(y2)
#print(y3)

#y3 = data[' max_diatom_c'].values
print("\n linjen er kjørt")

# Definer bølgelengdene
wavelengths = np.arange(402.5, 697.6, 5)  # Lager en array med bølgelengder fra 402.5 nm til 607.5 nm

# Opprett plottet
plt.figure(figsize=(10, 6))

cmap = plt.get_cmap('rainbow')  # Du kan bytte ut 'viridis' med andre colormaps som 'plasma', 'inferno', 'rainbow', etc.
colors = cmap(np.linspace(0, 1, rrs.shape[0]))  # Genererer en farge for hver linje

# Plott hver rad i rrs-arrayet som en separat linje
for i in range(rrs.shape[0]):
    plt.plot(wavelengths, rrs[i, :], color=colors[i], alpha=0.7)  # alpha=0.01 for å redusere intensiteten på hver linje
plt.ylim(bottom=-0.0005) #justere grensen på y- aksen


# Legg til akselabels og tittel
plt.xlabel('Wavelength (nm)')
plt.ylabel('Rrs (sr⁻¹)')
plt.title('Wavelength vs. Rrs')

# Viser plottet
plt.show()