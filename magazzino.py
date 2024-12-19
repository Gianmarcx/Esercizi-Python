from Gestione_ordini import menu_ordini

warehouse = {
    "Elettronica": {"Laptop": 10, "Smartphone": 20},
    "Abbigliamento": {"Maglietta": 50, "Jeans": 30},
    "Cibo": {"Mela": 30, "Pane": 25},
}

# Visualizza tutti i prodotti
for categoria, articoli in warehouse.items():
    print(f"Categoria: {categoria}")
    for articolo, quantita in articoli.items():
        print(f" - {articolo}: {quantita}")

# Aggiunge un nuovo articolo con la rispettiva quantità nella categoria Elettronica
warehouse["Elettronica"]["Tablet"] = 15
print("Categoria: Elettronica")
for articolo, quantita in warehouse["Elettronica"].items():
    print(f" - {articolo}: {quantita}")

# Modifica il valore di un articolo già presente nella categoria
warehouse["Abbigliamento"]["Jeans"] = 50
print(warehouse)

# Rimuove la key con il valore da una categoria
del warehouse["Cibo"]["Pane"]
print("Categoria: Cibo")
for articolo, quantita in warehouse["Cibo"].items():
    print(f" - {articolo}: {quantita}")

# Funzione per il menu
def menu(warehouse):
    while True:
        # Menù delle scelte
        print("Scegli cosa fare:")
        print("1 - Visualizza tutti i prodotti")
        print("2 - Aggiungi nuovi prodotti")
        print("3 - Aggiorna quantità")
        print("4 - Rimuovi prodotti")
        print("5 - Apri gestione ordini")
        print("6 - Esci")

        scelta = input("Inserire numero della scelta: ")

        if scelta == '6':
            print("Esci")
            break

        elif scelta == "1":
            for categoria, articoli in warehouse.items():
                print(f"Categoria: {categoria}")
                for articolo, quantita in articoli.items():
                    print(f" - {articolo}: {quantita}")

        elif scelta == '2':
            categoria = input("Inserisci la categoria (Elettronica, Abbigliamento, Cibo): ")
            if categoria in warehouse:
                articolo = input("Scrivi nome articolo: ")
                quantita = int(input("Inserisci la quantità: "))
                warehouse[categoria][articolo] = quantita
                print(f"Articolo '{articolo}' aggiunto nella categoria '{categoria}' con quantità {quantita}.")
            else:
                print("Questa categoria non esiste!")

        elif scelta == '3':
            categoria = input("Quale categoria aggiorni? (Elettronica, Abbigliamento, Cibo): ")
            if categoria in warehouse:
                articolo = input("Scrivi nome articolo da aggiornare: ")
                if articolo in warehouse[categoria]:
                    quantita_aggiornata = int(input(f"Inserisci nuova quantità per '{articolo}': "))
                    warehouse[categoria][articolo] = quantita_aggiornata
                    print(f"Quantità di '{articolo}' aggiornata a {quantita_aggiornata}.")
                else:
                    print("Articolo non esistente")
            else:
                print("Categoria non esistente")

        elif scelta == '4':
            categoria = input("Quale categoria scegli? (Elettronica, Abbigliamento, Cibo): ")
            if categoria in warehouse:
                articolo = input("Scrivi articolo da rimuovere: ")
                if articolo in warehouse[categoria]:
                    del warehouse[categoria][articolo]
                    print(f"Articolo '{articolo}' rimosso dalla categoria '{categoria}'.")
                else:
                    print("Articolo non esistente")
            else:
                print("Categoria non esistente")

        elif scelta == '5':
            print("Ecco la gestione degli ordini")
            menu_ordini(warehouse)

menu(warehouse)
