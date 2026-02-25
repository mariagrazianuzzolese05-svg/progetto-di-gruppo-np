import numpy as np
np.random.seed()


nome_file = "analisidigruppo2.txt"

# 1. CREAZIONE DEL FILE (Solo se non esiste, per evitare l'errore)
# Creiamo una matrice finta per simulare dei dati di laboratorio
arr=np.random.randint(1,10, size=5)
#matrice2=np.random.rand(4,4)
np.savetxt(nome_file, arr) 
print(f"File '{nome_file}' creato con dati di prova!")

with open(nome_file, "r") as file:
    righe = file.readlines()
    print(f"Letto correttamente! Il file ha {len(righe)} righe.")