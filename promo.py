# promo.py

def main(): 
    prezzi = []
    animali = []
    riga = input("Inserisci il prezzo del prodotto: ")
    while riga != "-1":
        dati = riga.split(" ")
        prezzi.append(float(dati[0]))
        animali.append(dati[1] == "Y")
        riga = input("Inserisci il prezzo del prodotto: ")
    sconto = discount(prezzi, animali, len(prezzi))
    print("Sconto totale: ", sconto)

def discount(prices, isPet, nItems):
    numPet = 0
    numNonPet = 0
    total = 0
    
    # totalizza e conta gli animali e articoli
    for i in range(nItems):
        total += prices[i]
        if isPet[i] == True: 
            numPet += 1
        else:
            numNonPet += 1
            
    # calcolo dello sconto
    if numPet >= 1 and numNonPet > 5:
        return total * 0.2
    
    return 0
    
    
        
main()