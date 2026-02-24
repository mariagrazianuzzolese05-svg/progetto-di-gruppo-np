import numpy as np


nome_file = "analisidigruppo3.txt"

# 1. CREAZIONE DEL FILE (Solo se non esiste, per evitare l'errore)
# Creiamo una matrice finta per simulare dei dati di laboratorio
matrice2=np.random.rand(4,4)
#matrice2=np.random.rand(4,4)
np.savetxt(nome_file, matrice2) 
print(f"File '{nome_file}' creato con dati di prova!")

with open(nome_file, "r") as file:
    righe = file.readlines()
    print(f"Letto correttamente! Il file ha {len(righe)} righe.")