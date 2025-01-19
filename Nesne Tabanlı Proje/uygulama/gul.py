from uygulama.cicek import Cicek

class Gul(Cicek):
    gul_sayisi = 0
    def __init__(self, renk, stok):
        super().__init__("Gül",renk,stok)
        Gul.gul_sayisi += stok

    @staticmethod
    def gul_sayisi_getir(cls):
        return cls.gul_sayisi