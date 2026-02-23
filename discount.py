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
