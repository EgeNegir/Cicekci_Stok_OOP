from uygulama.cicek import Cicek
from uygulama.egzotik_bitki import EgzotikBitki

class Orkide(Cicek, EgzotikBitki):
    def __init__(self, renk, stok, bolge, bakim_zorlugu):
        Cicek.__init__(self, "Orkide", renk, stok)
        EgzotikBitki.__init__(self, bolge, bakim_zorlugu)

    def bilgi_ver(self):
        Cicek.bilgi_ver(self)
        print(f"Bölge: {self.bolge}, Bakım Zorluğu: {self.bakim_zorlugu}")

    def fiyat_hesapla(self, *args):
        if len(args) == 1:
            # Sadece stok ile hesapla
            fiyat = args[0] * 19
            print(f"Orkide'nin fiyatı (stokla): {fiyat} TL")
        elif len(args) == 2:
            # Stok ve fiyat ile hesapla
            fiyat = args[0] * args[1]
            print(f"Orkide'nin fiyatı (stok ve fiyatla): {fiyat} TL")
        else:
            print("Geçersiz parametre sayısı! Lütfen 1 veya 2 parametre girin.")
        return fiyat