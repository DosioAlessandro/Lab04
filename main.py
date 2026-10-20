import lingotto_fiere

def menu():
    print(f'\n--- MENU LINGOTTO FIERE ---')
    print("1. Modifica nome del centro fieristico")
    print("2. Carica dati da file")
    print("3. Assegna stand a espositore")
    print("4. Visualizza elenco espositori")
    print("5. Visualizza stand ordinati per prezzo")
    print("6. Esci")

    return input("Scegli un'opzione >> ").strip()

def main():
    lingotto = lingotto_fiere.LingottoFiere("Lingotto Fiere")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome del centro fieristico: ")
            lingotto.nome = nuovo_nome

        elif scelta == "2":
            file_path = input("Inserire il nome del file: ")
            try:
                lingotto.carica_file_dati(file_path)
                print("Dati caricati correttamente.")
            except FileNotFoundError:
                print("File non trovato.")

        elif scelta == "3":
            if len(lingotto_fiere.stand.lista_stand) == 0 or len(lingotto_fiere.espositori.lista_espositori) == 0:
                print("Inserire prima gli stand e gli espositori")
            else:
                codice_stand = input("Codice stand: ")
                codice_espositore = input("Codice espositore: ")
                try:
                    lingotto.assegna_stand_a_espositore(codice_stand, codice_espositore)
                    print("Stand assegnato con successo.")
                except Exception:
                    print("Non è stato possibile assegnare lo stand")

        elif scelta == "4":
            if len(lingotto_fiere.stand.lista_stand) == 0 or len(lingotto_fiere.espositori.lista_espositori) == 0:
                print("Inserire prima gli stand e gli espositori")
            else:
                print("\n--- Elenco espositori ---")
                lingotto.elenca_espositori()

        elif scelta == "5":
            if len(lingotto_fiere.stand.lista_stand) == 0 or len(lingotto_fiere.espositori.lista_espositori) == 0:
                print("Inserire prima gli stand e gli espositori")
            else:
                stand_ordinati = lingotto.stand_ordinati_per_prezzo()
                print("\n--- Stand ordinati per prezzo ---")
                for s in stand_ordinati:
                    print(s)

        elif scelta == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()