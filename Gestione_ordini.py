
lista_ordini = []

#permette di creare gli ordini
def crea_ordine(warehouse):
    ordine = {}

    categoria = input("Inserire categoria articolo (Elettronica, Abbigliamento, Cibo)")
    if categoria not in warehouse:
        print("Categoria non trovata")
        return

    articolo = input(f"Scrivi nome articolo dalla categoria {categoria}:")
    if articolo not in warehouse[categoria]:
        print("articolo non trovato nella categoria")
        return

    quantità = int(input(f"Inserisci la quantità da ordinare{articolo}:"))
    if quantità > warehouse[categoria][articolo]:
        print("Quantità non disponibile")
        return
    
    warehouse[categoria][articolo] -= quantità

    ordine["categoria"] = categoria
    ordine["articolo"] = articolo
    ordine["quantità"] = quantità
    
#aggiunge un ordine alla lista
    lista_ordini.append(ordine)
    print(f"Ordine per {quantità} {articolo} aggiunto!")

#Visualizza gli ordini effettuati
def visualizza_ordini(warehouse):
    if not lista_ordini:
        print("Nessun ordine effettuato")
    else:
        print("Cronologia degli ordini:")
        for ordine in  lista_ordini:
             print(f"Categoria: {ordine['categoria']}, Articolo: {ordine['articolo']}, Quantità: {ordine['quantità']}")


def menu_ordini(warehouse):
    while True:  # Ciclo while
        # Menù delle scelte
        print("Scegli cosa fare:")
        print("1-Crea nuovo ordine")
        print("2-Cronologia ordini")
        print("3-Torna al menu principale")

        scelta = input("Inserire numero della scelta:")

        if scelta == '3':
            print("Torna al menu principale")
            break  # Esce dal ciclo while

        if scelta == "1":
            crea_ordine(warehouse)
            
        elif scelta == '2':
            visualizza_ordini(warehouse)





