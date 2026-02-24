import numpy as np
dati_caricati = np.loadtxt("analisidigruppo.txt")
print(dati_caricati)

'''Analisi posizionale (ricerche, argmin, argmax, percentili)
Si possono analizzare le posizioni relative dei valori:
np.argmin(arr) → indice del valore minimo
np.argmax(arr) → indice del valore massimo
np.percentile(arr, 50) → mediana
np.searchsorted(arr, x) → trovare posizione ordinata di inserimento
'''

minimo=np.argmin(dati_caricati)