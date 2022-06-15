IstanbulTren=[]
AnkaraTren=[]
KonyaTren=[]
Yolcular=[]
print("Hoş Geldiniz\n")
while True:
    def YolcuEkle(sehir,gun,ay,kisisayisi):
        def YolcuBilgi(sehir,gun,ay,koltuk,sira):
            isim=input("Yolcu Adı Giriniz: ")
            soyisim=input("Yolcu Soyadı Giriniz: ")
            telefon=int(input("Yolcu Telefon Numarası Giriniz"))
            if(sehir==1):
                sehir="Istanbul"
            elif(sehir==2):
                sehir="Ankara"
            else:
                sehir="Konya"
            with open("21100011045.txt","a+",encoding="utf-8") as a:
                a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(isim,soyisim,telefon,sehir,koltuk,sira,gun,ay,))
        if(kisisayisi>0):
            if(sehir==1):
                print("Lütfen Koltuk Seçiniz: ")
                IstanbulTren=[]
                with open("IstanbulTreni.txt","r") as istanbul:
                    tren=istanbul.readlines()
                    print("A-B-C-D")
                    for i in tren:
                        vagon=[]
                        istanbultreni=i.split(" ")
                        istanbultreni.remove("\n")
                        vagon.append(istanbultreni[0])
                        vagon.append(istanbultreni[1])
                        vagon.append(istanbultreni[2])
                        vagon.append(istanbultreni[3])
                        IstanbulTren.append(vagon)
                    for i,e in enumerate(IstanbulTren):
                        print(*e,i+1,end="\n")
                koltuk=input("Koltuk Harfini Giriniz\n")
                sira=int(input("Sıra Numarasını Giriniz\n"))
                if(koltuk=="A"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[0]="*"
                if(koltuk=="B"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[1]="*"
                if(koltuk=="C"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[2]="*"
                if(koltuk=="D"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[3]="*"
                with open("IstanbulTreni.txt","w") as a:
                        for i,e in enumerate(IstanbulTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3]))
            if(sehir==2):
                print("Lütfen Koltuk Seçiniz: ")
                AnkaraTren=[]
                with open("AnkaraTreni.txt","r") as ankara:
                    tren=ankara.readlines()
                    print("A-B-C-D")
                    for i in tren:
                        vagon=[]
                        ankaratreni=i.split(" ")
                        ankaratreni.remove("\n")
                        vagon.append(i[0])
                        vagon.append(i[2])
                        vagon.append(i[4])
                        vagon.append(i[6])
                        AnkaraTren.append(vagon)
                    for i,e in enumerate(AnkaraTren):
                        print(*e,i+1,end="\n")
                koltuk=input("Koltuk Harfini Giriniz\n")
                sira=int(input("Sıra Numarasını Giriniz\n"))
                if(koltuk=="A"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[0]="*"
                if(koltuk=="B"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[1]="*"
                if(koltuk=="C"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[2]="*"
                if(koltuk=="D"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[3]="*"
                with open("AnkaraTreni.txt","w") as a:
                        for i,e in enumerate(AnkaraTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3]))
            if(sehir==3):
                print("Lütfen Koltuk Seçiniz: ")
                KonyaTren=[]
                with open("KonyaTreni.txt","r") as konya:
                    tren=konya.readlines()
                    print("A-B-C-D")
                    for i in tren:
                        vagon=[]
                        konyatreni=i.split(" ")
                        konyatreni.remove("\n")
                        vagon.append(i[0])
                        vagon.append(i[2])
                        vagon.append(i[4])
                        vagon.append(i[6])
                        KonyaTren.append(vagon)
                    for i,e in enumerate(KonyaTren):
                        print(*e,i+1,end="\n")
                koltuk=input("Koltuk Harfini Giriniz\n")
                sira=int(input("Sıra Numarasını Giriniz\n"))
                if(koltuk=="A"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[0]="*"
                if(koltuk=="B"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[1]="*"
                if(koltuk=="C"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[2]="*"
                if(koltuk=="D"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[3]="*"
                with open("KonyaTreni.txt","w") as a:
                        for i,e in enumerate(KonyaTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3]))
        YolcuBilgi(sehir,gun,ay,koltuk,sira)
        kisisayisi-=1
        if(kisisayisi>0):
            YolcuEkle()
    def YolcuLisele():
        global Yolcular
        Yolcular=[]
        with open("21100011045.txt","r",encoding="utf-8") as a:
            yolcu=a.readlines()
            for i in yolcu:
                kisi={}
                bilgi=i.split("-")
                bilgi.remove("\n")
                kisi["isim"]=bilgi[0]
                kisi["soyisim"]=bilgi[1]
                kisi["telefon"]=bilgi[2]
                kisi["sehir"]=bilgi[3]
                kisi["koltuk"]=bilgi[4]
                kisi["sira"]=bilgi[5]
                kisi["gun"]=bilgi[6]
                kisi["ay"]=bilgi[7]
                Yolcular.append(kisi)
        for i in Yolcular:
            print(i)
    def YolcuSil(numara):
        def Koltukiptal(sehir,koltuk,sira):
            if(sehir=="Istanbul"):
                global IstanbulTren
                IstanbulTren=[]
                with open("IstanbulTreni.txt","r") as a:
                    tren=a.readlines()
                    for i in tren:
                        vagon=[]
                        istanbultreni=i.split(" ")
                        istanbultreni.remove("\n")
                        vagon.append(istanbultreni[0])
                        vagon.append(istanbultreni[1])
                        vagon.append(istanbultreni[2])
                        vagon.append(istanbultreni[3])
                        IstanbulTren.append(vagon)
                if(koltuk=="A"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[0]="-"
                if(koltuk=="B"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[1]="-"
                if(koltuk=="C"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[2]="-"
                if(koltuk=="D"):
                    for i,e in enumerate(IstanbulTren):
                        if(i==sira-1):
                            e[3]="-"
                with open("IstanbulTreni.txt","w") as a:
                        for i,e in enumerate(IstanbulTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3]))
            if(sehir=="Ankara"):
                global AnkaraTren
                AnkaraTren=[]
                with open("AnkaraTreni.txt","r") as a:
                    tren=a.readlines()
                    for i in tren:
                        vagon=[]
                        istanbultreni=i.split(" ")
                        istanbultreni.remove("\n")
                        vagon.append(istanbultreni[0])
                        vagon.append(istanbultreni[1])
                        vagon.append(istanbultreni[2])
                        vagon.append(istanbultreni[3])
                        AnkaraTren.append(vagon)
                if(koltuk=="A"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[0]="-"
                if(koltuk=="B"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[1]="-"
                if(koltuk=="C"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[2]="-"
                if(koltuk=="D"):
                    for i,e in enumerate(AnkaraTren):
                        if(i==sira-1):
                            e[3]="-"
                with open("AnkaraTreni.txt","w") as a:
                        for i,e in enumerate(AnkaraTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3])) 
            if(sehir=="Konya"):
                global KonyaTren
                KonyaTren=[]
                with open("KonyaTreni.txt","r") as a:
                    tren=a.readlines()
                    for i in tren:
                        vagon=[]
                        istanbultreni=i.split(" ")
                        istanbultreni.remove("\n")
                        vagon.append(istanbultreni[0])
                        vagon.append(istanbultreni[1])
                        vagon.append(istanbultreni[2])
                        vagon.append(istanbultreni[3])
                        KonyaTren.append(vagon)
                if(koltuk=="A"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[0]="-"
                if(koltuk=="B"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[1]="-"
                if(koltuk=="C"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[2]="-"
                if(koltuk=="D"):
                    for i,e in enumerate(KonyaTren):
                        if(i==sira-1):
                            e[3]="-"
                with open("KonyaTreni.txt","w") as a:
                        for i,e in enumerate(KonyaTren):
                            a.write("{} {} {} {} \n".format(e[0],e[1],e[2],e[3]))        

        for i in Yolcular:
            if(i["telefon"]==numara):
                sehir=i["sehir"]
                koltuk=i["koltuk"]
                sira=i["sira"]
                Koltukiptal(sehir,koltuk,sira)
                Yolcular.remove(i)
                with open("21100011045.txt","w") as a:
                        for i,e in enumerate(Yolcular):
                            a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(e["isim"],e["soyisim"],e["telefon"],e["sehir"],e["koltuk"],e["sira"],e["gun"],e["ay"]))
        print("Başarıyla Yolcu Silindi\n")
    def YolcuGuncelle(numara):
        for i in Yolcular:
            if(i["telefon"]==numara):
                degisim=input("Yolcunun değiştirmek istediğiniz bilgisini giriniz: ")
                bilgi=input("Yolcunun yeni bilgisini giriniz: ")
                i[degisim]=bilgi
                print(i)
        with open("21100011045.txt","w",encoding="utf-8") as a:
            for i in Yolcular:
                a.write("{}-{}-{}-{}-{}-{}-{}-{}-\n".format(e["isim"],e["soyisim"],e["telefon"],e["sehir"],e["koltuk"],e["sira"],e["gun"],e["ay"]))
    def YolcuBul(numara):
        for i in Yolcular:
            if(i["telefon"]==numara):
                print(i)
    def VagonEkle(DosyaAdi):
        with open(DosyaAdi,"a+") as a:
            for i in range(0,10):
                a.write("- - - - \n")
    print("Yolcuları Eklemek İçin: 1\nYolcu Silmek İçin: 2\nYolcu Listelemek İçin: 3\nYolcu Güncellemek İçin: 4\nVagon Eklemek İçin 5:\nYolcu Bulmak İçin 6:\n")
    secim=int(input("Seçimizi Giriniz: "))
    if(secim==1):
        print("1: İstanbul\n2: Ankara\n3: Konya\n")
        sehir=int(input("Gitmek istediğiniz şehri seçiniz: "))
        if(sehir==1):
            Gun=int(input("Gitmek istediğiniz günü giriniz: "))
            Ay=int(input("Gitmek İstediğiniz ayı giriniz: "))
            kisi=int(input("Bilet almak isteyen kişi sayısını giriniz: "))
            YolcuEkle(sehir,Gun,Ay,kisi)
        elif(sehir==2):
            Gun=int(input("Gitmek istediğiniz günü giriniz: "))
            Ay=int(input("Gitmek İstediğiniz ayı giriniz: "))
            kisi=int(input("Bilet almak isteyen kişi sayısını giriniz: "))
            YolcuEkle(sehir,Gun,Ay,kisi)
        elif(sehir==3):
            Gun=int(input("Gitmek istediğiniz günü giriniz: "))
            Ay=int(input("Gitmek İstediğiniz ayı giriniz: "))
            kisi=int(input("Bilet almak isteyen kişi sayısını giriniz: "))
            YolcuEkle(sehir,Gun,Ay,kisi)
        else:
            print("Geçerli Seçim Girmediniz")
    elif(secim==2):
        YolcuLisele()
        numara=input("Bilet İptal Eden Yolcunun Telefonunu Giriniz")
        YolcuSil(numara)
    elif(secim==3):
        YolcuLisele()
    elif(secim==4):
        numara=input("Bilgisi Güncellenecek Yolcunun Telefonunu Giriniz")
        YolcuGuncelle(numara)
    elif(secim==5):
        dosya=input("Vagon Eklenicek Dosyanın Adı: ")
        VagonEkle(dosya)
    elif(secim==6):
        numara=input("Bulmak İstediğiniz Yolcunun Numarasını Giriniz: ")
        YolcuBul(numara)
    cikis=int(input("Çıkış yapmak isterseniz lütfen 1'i tuşlayınız, devam etmek için 0: "))
    if(cikis==1):
        break

print("Başarıyla Çıkış Yapıldı")
