
class Dosya():

    def __init__(self):

        with open("metin.txt","r", encoding="utf-8") as file:

            dosya_icerik = file.read()
            self.sade_kelimeler = list()
            kelimeler = dosya_icerik.split()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
    
    def tum_kelimeler(self):

        kelimeler_kumesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)

        for i in kelimeler_kumesi:
            print(i)
            print("************************************")

    def kelime_frekans(self):

        kelime_sozluk = dict()

        for i in self.sade_kelimeler:
            
            if(i in kelime_sozluk):
                kelime_sozluk[i] += 1
            else:
                kelime_sozluk[i] = 1
        
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor.".format(kelime,sayi))

            print("--------------------------------------")

dosya = Dosya()
dosya.kelime_frekans()
                
                

