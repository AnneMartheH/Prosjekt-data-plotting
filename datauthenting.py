import pandas as pd

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