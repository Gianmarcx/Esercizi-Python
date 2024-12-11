lista = ['Muro', 'Palla', 'Calcio', 'Frutta']

#Crea un dizionario che mappa ogni parola della lista alla sua lunghezza
dizionario_lunghezza = {parola: len(parola) for parola in lista}

print(dizionario_lunghezza)
