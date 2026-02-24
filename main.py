import giovanni
import numpy as np
import mariagrazia
while True:

    # 1. QUI HO MESSO LA LISTA DEI FILE (Invece di caricarli subito in alto)
    #files = ["analisidigruppo.txt", "analisidigruppo2.txt","analisidigruppo3.txt"]
    #report_finale = ""

    # 2. QUI C'È IL CICLO CHE ANALIZZA UN FILE ALLA VOLTA
    '''for nome_file in files:
        try:
            # Carichiamo i dati solo quando serve dentro il ciclo
            #dati = np.loadtxt(nome_file)
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
    with open("risultati.txt", "r") as f:
        contenuto = f.read()
        print(contenuto)
    print("\nAnalisi conclusa. Controlla 'risultati_giovanni.txt'!")

if __name__ == "__main__":
    main()'''
    with open("risultati.txt","r") as file:
                contenuto = file.read()
                print(contenuto)
    scelta=input('vuoi continuare? ')
    if scelta=='no':
            break