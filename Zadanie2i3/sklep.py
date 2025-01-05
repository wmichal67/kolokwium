def dodaj_produkt(sprzedaz):
    """Dodaje nowy produkt do słownika sprzedaży."""
    nazwa = input("Podaj nazwę produktu: ")
    wyniki = input("Podaj wyniki sprzedaży z trzech tygodni, oddzielone spacją: ")
    wyniki = list(map(int, wyniki.split()))
    if len(wyniki) != 3:
        print("Musisz podać dokładnie trzy liczby.")
        return
    sprzedaz[nazwa] = wyniki
    print(f"Produkt {nazwa} został dodany.")

def wyswietl_sprzedaz(sprzedaz):
    """Wyświetla sumaryczną sprzedaż dla każdego produktu."""
    if not sprzedaz:
        print("Brak danych sprzedażowych.")
        return
    for produkt, wyniki in sprzedaz.items():
        suma = sum(wyniki)
        print(f"Produkt: {produkt}, Sumaryczna sprzedaż: {suma}")

def usun_produkt(sprzedaz):
    """Usuwa produkt ze słownika sprzedaży."""
    nazwa = input("Podaj nazwę produktu do usunięcia: ")
    if nazwa in sprzedaz:
        del sprzedaz[nazwa]
        print(f"Produkt {nazwa} został usunięty.")
    else:
        print(f"Produkt {nazwa} nie istnieje.")

def znajdz_najlepszy_produkt(sprzedaz):
    """Znajduje produkt o najwyższej sumarycznej sprzedaży."""
    if not sprzedaz:
        print("Brak danych sprzedażowych.")
        return
    max_suma = max(sum(wyniki) for wyniki in sprzedaz.values())
    najlepsze_produkty = [produkt for produkt, wyniki in sprzedaz.items() if sum(wyniki) == max_suma]
    print("Produkt(y) o najwyższej sumarycznej sprzedaży:")
    for produkt in najlepsze_produkty:
        print(f"- {produkt} z sumaryczną sprzedażą: {max_suma}")

def oblicz_srednia_sprzedaz(sprzedaz):
    """Oblicza i wyświetla średnią sprzedaż dla każdego produktu."""
    if not sprzedaz:
        print("Brak danych sprzedażowych.")
        return
    print("Średnia sprzedaż dla każdego produktu:")
    for produkt, wyniki in sprzedaz.items():
        srednia = sum(wyniki) / len(wyniki)
        print(f"Produkt: {produkt}, Średnia sprzedaż: {srednia:.2f}")

def produkty_ponizej_progu(sprzedaz):
    """Wyświetla produkty, których sumaryczna sprzedaż była poniżej podanego progu."""
    if not sprzedaz:
        print("Brak danych sprzedażowych.")
        return
    prog = int(input("Podaj próg sprzedaży: "))
    produkty_ponizej = [produkt for produkt, wyniki in sprzedaz.items() if sum(wyniki) < prog]
    if produkty_ponizej:
        print("Produkty o sprzedaży poniżej progu:")
        for produkt in produkty_ponizej:
            print(f"- {produkt}")
    else:
        print("Żaden produkt nie ma sprzedaży poniżej podanego progu.")

def menu():
    """Główna funkcja programu."""
    sprzedaz = {}
    while True:
        print("\nMenu:")
        print("1. Dodaj produkt")
        print("2. Wyświetl sumaryczną sprzedaż")
        print("3. Usuń produkt")
        print("4. Znajdź produkt o najwyższej sumarycznej sprzedaży")
        print("5. Oblicz średnią sprzedaż dla każdego produktu")
        print("6. Wyświetl produkty poniżej podanego progu sprzedaży")
        print("7. Zakończ program")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodaj_produkt(sprzedaz)
        elif wybor == "2":
            wyswietl_sprzedaz(sprzedaz)
        elif wybor == "3":
            usun_produkt(sprzedaz)
        elif wybor == "4":
            znajdz_najlepszy_produkt(sprzedaz)
        elif wybor == "5":
            oblicz_srednia_sprzedaz(sprzedaz)
        elif wybor == "6":
            produkty_ponizej_progu(sprzedaz)
        elif wybor == "7":
            print("Zakończenie programu.")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    menu()
