class Sklep:

    pieniadze = 0

    @classmethod
    def kupprodukt(cls, cena):
        cls.pieniadze += cena
    
    @classmethod
    def wyplata(cls, wartosc):
        cls.pieniadze -= wartosc