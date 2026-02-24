import numpy as np
dati_caricati = np.loadtxt("analisidigruppo.txt")
print(dati_caricati)

dati_caricati3 = np.loadtxt("analisidigruppo3.txt")
print(dati_caricati3)
'''Analisi posizionale (ricerche, argmin, argmax, percentili)
Si possono analizzare le posizioni relative dei valori:
np.argmin(arr) → indice del valore minimo
np.argmax(arr) → indice del valore massimo
np.percentile(arr, 50) → mediana
np.searchsorted(arr, x) → trovare posizione ordinata di inserimento
'''

minimo=np.argmin(dati_caricati)
massimo=np.argmax(dati_caricati)
percentuale=np.percentile(dati_caricati,50)

dati_piatti = dati_caricati.flatten()
# Importante: searchsorted vuole dati ORDINATI
dati_ordinati = np.sort(dati_piatti)
ordina = np.searchsorted(dati_ordinati, 1)

'''Operazioni matriciali e algebriche (dot, transpose, norme)
Gli array multidimensionali permettono analisi strutturali complesse:
np.dot(A, B) → prodotto matriciale
np.transpose(A) → trasposizione
np.linalg.norm(A) → norma della matrice
np.cov(A.T) → matrice di covarianza'''

prd=np.dot(dati_caricati,dati_caricati3)
trs=np.transpose(dati_caricati)
norma=np.linalg.norm(dati_caricati)
co=np.cov(dati_caricati.T)

with open("risultati.txt","w") as f:
        
        f.write(f"{minimo}\n")
        f.write(f"{massimo}\n")
        f.write(f"{percentuale}\n")
        f.write(f"{ordina}\n")
        f.write(f"{prd}\n")
        f.write(f"{trs}\n")
        f.write(f"{norma}\n")
        f.write(f"{co}\n")

