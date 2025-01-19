class Cicek:
    def __init__(self,isim,renk,stok):
        self.isim=isim   
        self._renk=renk   
        self.stok=stok
    
    def stok_ekle(self, miktar):
        if miktar > 0:
            self.stok += miktar
            print(f"{miktar} adet stok eklendi. Güncel stok: {self.stok}")
        else:
            print("Geçersiz miktar!")

    def stok_azalt(self, miktar):
        if 0 < miktar <= self.stok:
            self.stok -= miktar
            print(f"{miktar} adet stok çikarildi. Güncel stok: {self.stok}")
        else:
            print("Yetersiz stok veya geçersiz miktar!")
    def bilgi_ver(self):
        print(f"Çiçek Adı: {self.isim}, Renk: {self._renk}, Stok: {self.stok}")
    
    
    def get_stock(self):
        return self.stok

    def set_stock(self, yeni_stok):
        if yeni_stok >= 0:
            self.stok = yeni_stok
        else:
            print("Stok miktarı negatif olamaz!")