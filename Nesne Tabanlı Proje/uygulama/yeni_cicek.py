from uygulama.cicek import Cicek

class YeniCicek(Cicek):
    @staticmethod
    def yeni_tur_ekle(isim, renk, stok):
        return YeniCicek(isim, renk, stok)