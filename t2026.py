def calcola_tasse():
    reddito_input = input("Inserisci il tuo reddito stimato per l'anno 2026: €")
    try:
        reddito = float(reddito_input)
    except ValueError:
        print("Errore: Per favore inserisci un numero valido.")
        return

    tasse = 0.0

    if reddito <= 28000:
        # Primo scaglione: 23% su tutto
        tasse = reddito * 0.23
        
    elif reddito <= 50000:
        # Secondo scaglione: 23% sui primi 28.000 + 33% sull'eccedenza
        tasse_primo_scaglione = 28000 * 0.23
        tasse_secondo_scaglione = (reddito - 28000) * 0.33
        tasse = tasse_primo_scaglione + tasse_secondo_scaglione
        
    else:
        # Terzo scaglione: i primi due scaglioni sono pieni, 43% sull'eccedenza oltre i 50.000
        tasse_primo_scaglione = 28000 * 0.23               
        tasse_secondo_scaglione = (50000 - 28000) * 0.33   
        tasse_terzo_scaglione = (reddito - 50000) * 0.43
        tasse = tasse_primo_scaglione + tasse_secondo_scaglione + tasse_terzo_scaglione
      
    reddito_netto = reddito - tasse
    
    print(f"Reddito Lordo: € {reddito:,.2f}")
    print(f"Totale Tasse:  € {tasse:,.2f}")
    print(f"Reddito Netto: € {reddito_netto:,.2f}")

def main(): 

    
    calcola_tasse()

if __name__ == "__main__":
    main()
