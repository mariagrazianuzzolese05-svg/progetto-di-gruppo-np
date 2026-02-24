import numpy as np
'''dati_caricati = np.loadtxt("analisidigruppo.txt")
print(dati_caricati)

dati_caricati2 = np.loadtxt("analisidigruppo2.txt")
print(dati_caricati2)'''


# --- COMPITO 1: Statistiche di base (Array 1D) ---
def analizza_statistiche_base(arr):
    valore_min = np.min(arr)
    valore_max = np.max(arr)
    media = np.mean(arr)
    deviazione = np.std(arr)
    
    return (f"--- RISULTATI 1D ---\n"
            f"Min: {valore_min}, Max: {valore_max}\n"
            f"Media: {media:.2f}, Deviazione: {deviazione:.2f}\n")

# --- COMPITO 3: Analisi per Assi (Array 2D) ---
def analizza_per_assi(matrix):
    somma_colonne = np.sum(matrix, axis=0)
    media_righe = np.mean(matrix, axis=1)
    
    return (f"--- RISULTATI 2D (ASSI) ---\n"
            f"Somma colonne (axis=0): {somma_colonne}\n"
            f"Media righe (axis=1): {media_righe}\n")

# --- LOGICA DI ESECUZIONE ---
def main():
    # 1. QUI HO MESSO LA LISTA DEI FILE (Invece di caricarli subito in alto)
    files = ["analisidigruppo.txt", "analisidigruppo2.txt"]
    report_finale = ""

    # 2. QUI C'È IL CICLO CHE ANALIZZA UN FILE ALLA VOLTA
    for nome_file in files:
        try:
            # Carichiamo i dati solo quando serve dentro il ciclo
            dati = np.loadtxt(nome_file)
            print(f"\nSto elaborando: {nome_file}...")

            # 3. QUI C'È IL CONTROLLO NDIM PER SCELTA ANALISI
            if dati.ndim == 1:
                risultato = analizza_statistiche_base(dati)
            else:
                risultato = analizza_per_assi(dati)
            
            print(risultato)
            # Aggiungiamo i risultati di questo file al report generale
            report_finale += f"FILE: {nome_file}\n{risultato}\n" + "="*20 + "\n"

        except FileNotFoundError:
            print(f"Errore: Il file {nome_file} non esiste!")
        except Exception as e:
            print(f"Errore generico con {nome_file}: {e}")

    # 4. QUI HO MESSO IL SALVATAGGIO FINALE (Scrive tutto in un colpo solo)
    with open("risultati_giovanni.txt", "w") as f:
        f.write(report_finale)
    print("\nAnalisi conclusa. Controlla 'risultati_giovanni.txt'!")

if __name__ == "__main__":
    main()