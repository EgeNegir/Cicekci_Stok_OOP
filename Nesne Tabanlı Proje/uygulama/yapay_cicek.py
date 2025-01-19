from uygulama.cicek import Cicek

class YapayCicek(Cicek):
    def __init__(self, isim, renk, stok, materyal):
        super().__init__(isim, renk, stok)
        self.materyal = materyal

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Malzeme: {self.materyal}")