from uygulama.gul import Gul
from uygulama.lale import Lale
from uygulama.papatya import Papatya
from uygulama.anemon import Anemon
from uygulama.lotus import Lotus
from uygulama.akasya import Akasya
from uygulama.yeni_cicek import YeniCicek
from uygulama.orkide import Orkide


cicek_listesi=[]
def stok_ekleme():
    isim = input("\nStok eklemek istediğiniz çiçeğin adini girin: ")
    miktar = int(input("Eklenecek miktari girin: "))
    for cicek in cicek_listesi:
        if cicek.isim.lower() == isim.lower():
            cicek.stok_ekle(miktar)
            return
    else:
        print("Çiçek bulunamadı!")
def stok_azaltma():
    isim = input("\nStok azaltmak istediğiniz çiçeğin adını girin: ")
    miktar = int(input("Azaltılacak miktarı girin: "))

    for cicek in cicek_listesi:
        if cicek.isim.lower() == isim.lower():
            cicek.stok_azalt(miktar)
            return
    print("Çiçek bulunamadı!")
def fiyat_hesapla_hepsi():
    if not cicek_listesi:
        print("\nStokta hiç çiçek yok, fiyat hesaplanamaz!")
    else:
        print("\n çiçeklerinin fiyat hesaplamaları:")
        for cicek in cicek_listesi:
            if isinstance(cicek, Orkide):  
                if cicek.stok > 0: 
                    cicek.fiyat_hesapla(cicek.stok) 
                else:
                    print(f"{cicek.isim} çiçeği için stok yok!")
            

def cicek_ekle():
    print("\n1: Gül, 2: Lale, 3: Papatya, 4: Anemon, 5: Lotus, 6: Akasya, 7: Orkide, 8: Yeni Çiçek")
    try:
        durum = int(input("Hangi çiçeği eklemek istersiniz? (1-8): "))
    except ValueError:
        print("Geçersiz seçim! Lütfen bir sayı girin.")
        return
    renk = input("Rengi girin: ")

    try:
        stok = int(input("Stok miktarı girin: "))
    except ValueError:
        print("Geçersiz stok miktarı! Lütfen bir sayı girin.")
        return

    cicek = None
    if durum == 1:
        cicek = Gul(renk, stok)

    elif durum == 2:
        cicek = Lale(renk, stok)

    elif durum == 3:
        cicek = Papatya(renk, stok)

    elif durum == 4:
        cicek = Anemon(renk, stok)

    elif durum == 5:
        cicek = Lotus(renk, stok)

    elif durum == 6:
        cicek = Akasya(renk, stok)

    elif durum == 7:
        bolge = input("Orkide'nin yetiştiği bölgeyi girin: ")
        bakim_zorlugu = input("Bakım zorluğunu girin (Kolay/Orta/Zor): ")
        cicek = Orkide(renk, stok, bolge, bakim_zorlugu)
    

    elif durum == 8:
        yeni_tur = input("Yeni çiçek türü girin: ")
        cicek = YeniCicek.yeni_tur_ekle(yeni_tur, renk, stok)
    else:
        print("Geçersiz seçim! Lütfen 1 ile 8 arasında bir değer girin.")
        return
    
    if cicek:  
        cicek_listesi.append(cicek)
        print(f"{cicek.isim} eklendi")
    else:
        print("Çiçek eklenemedi. Lütfen tekrar deneyin.")
     
            
def cicek_sil():            
    isim=input("\nSilmek istediğiniz çiçeğin adını girin: ")

    for cicek in cicek_listesi:
        if cicek.isim.lower()==isim.lower():

            cicek_listesi.remove(cicek)
            print(f"{cicek.isim} stoktan çıkarıldı! ")
            return
    print("Çiçek bulunamadı!")

def stok_görüntüle():
    if not cicek_listesi:
        print("\nStokta hiç çiçek yok!")
    else:
        print("\nStok Durumu: ")
        for cicek in cicek_listesi:
            cicek.bilgi_ver()

def Ana_Menu():
    while True:
        print("\n=== Çiçekçi Otomasyon Sistemi ===")
        print("1: Çiçek Ekle")
        print("2: Çiçek Sil")
        print("3: Stok Görüntüle")
        print("4: Stok Ekle")
        print("5: Stok Azalt")
        print("6: fiyat hesapla")
        print("7: Çıkış")
        durum = int(input("Bir seçenek seçin (1-7): "))
        print("***********************************")

        if durum == 1:
            cicek_ekle()
        elif durum == 2:
            cicek_sil()
        elif durum == 3:
            stok_görüntüle()
        elif durum == 4:
            stok_ekleme()
        elif durum == 5:
            stok_azaltma()
        elif durum ==6:
            fiyat_hesapla_hepsi()

        elif durum == 7:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__=="__main__":
    Ana_Menu()



    
