dizionario = {'Vincenzo': 3339765551, 'Paolo': 3568434452, 'Laura': 3518883564}
print(dizionario)

#cerca una key e un valore nel dizionario
key_cercata = 'Laura'
for key, value in dizionario.items():
    if key == key_cercata: 
        print(key + "-"+ str(value)) #stampa la chiave cercata e il suo valore

#aggiunge una key al dizionario
dizionario['Ciro'] = 375991446
print(dizionario)

#stampa le key del dizionario ordinate in ordine alfabetico di nome 
for key in sorted(dizionario.keys()):
    print(key + "-"+ str(dizionario[key]))


