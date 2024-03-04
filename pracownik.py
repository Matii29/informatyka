class Menager:
    def __init__(self, _imie:str, _nazwisko:str, _stawka:int, _waluta:str) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.stawka = _stawka
        self.waluta = _waluta
        self.wyplataroczna = 0

    def zmien_wyplate(self, nowa_wyplata):
        self.stawka = nowa_wyplata
        self.wyplataroczna = self.oblicz_wypłate_roczna()

    def oblicz_wypłate_roczna(self):
        return 12 * self.stawka

    def info(self):
        print("---"*10)
        print(f"Imie i Nazwisko: {self.imie}{self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}{self.waluta}")
        print(f"Wypłataroczna: {self.wyplataroczna}{self.waluta}")
        print("---"*10)

menager1 = Menager("Olek", "Olkowaty", 5340, "PLN" )
menager1.wyplataroczna = menager1.oblicz_wypłate_roczna()
menager1.info()
menager1.zmien_wyplate(5500)
menager1.info()

class Kasjer:
    def __init__(self, _imie:str, _nazwisko:str, _stawka:int, _waluta:str) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.stawka = _stawka
        self.waluta = _waluta
        self.wyplataroczna = 0

    def zmien_wyplate(self, nowa_wyplata):
        self.stawka = nowa_wyplata
        self.wyplataroczna = self.oblicz_wypłate_roczna()

    def oblicz_wypłate_roczna(self):
        return 12 * self.stawka

    def info(self):
        print("---"*10)
        print(f"Imie: {self.imie}{self.nazwisko}")
        print(f"Wyplata miesieczna: {self.stawka}{self.waluta}")
        print(f"Wypłataroczna: {self.wyplataroczna}{self.waluta}")
        print("---"*10)

kasjer1 = Kasjer("Goleg", "Grubawy", 3430, "PLN")
kasjer1.wyplataroczna = kasjer1.oblicz_wypłate_roczna()
kasjer1.info()
kasjer1.zmien_wyplate(3500)
kasjer1.info()
