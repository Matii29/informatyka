class laptop_ogolnie:
    def __init__(self, marka, cena):
        self.marka = marka
        self.cena = cena
        
    def wyswietl_info_ogln(self):
        print(f"""
        Laptop
        Marka: {self.marka}
        Cena: {self.cena}
        """)
        
class laptop_szczegolowo(laptop_ogolnie):
    def __init__(self, marka, cena, stan, model, rokprodukcja):
        super().__init__(marka, cena)
        self.model = model
        self.stan = stan
        self.rokprodukcja = rokprodukcja


    def wyswietl_info_szcz(self):
        print(f"""
        Laptop
        Marka: {self.marka}
        Model: {self.model}
        Cena: {self.cena}
        Stan: {self.stan} 
        Rok produkcji: {self.rokprodukcja}       
            """)
        
Lenovo = laptop_szczegolowo("Lenovo", 2000, "Uzywany", "Thinkpad", 2015 )
Lenovo.wyswietl_info_szcz()

        

