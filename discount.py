def discount(prezzi, animale, numero):
    risultato = 0.0
    base_sconto = 0.0
    numero_animali = 0
    if len(set(animale)) == 2:
        index = 0
        for value in animale:
            if value:
                numero_animali = numero_animali + 1 
            else:
                base_sconto = base_sconto + prezzi[index]
            index = index + 1
        if (numero - numero_animali) >= 5:
            risultato = base_sconto * 0.2
    return risultato

def main():

    prices = []
    isPet = []
    sconto = 0.0
    with open ('lista_con_sconto.txt', 'r') as file:
        righe = file.readlines()
        for riga in righe:
            campi = riga.split()
            prices.append(float(campi[0]))
            if campi[1].upper() == 'Y':
                isPet.append(True)
            else:
                isPet.append(False)
        nItems = len(prices)
        if nItems == len(isPet):
            sconto = discount(prices, isPet, nItems)
    print(sconto)

if __name__ == "__main__":
    main()
