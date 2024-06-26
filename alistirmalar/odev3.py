#Problem 1
#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

toplam = 0
i=1
sayi= int(input("Sayı giriniz: "))

while(i<sayi):
    if(sayi % i ==0):
        toplam+=i
    i+=1
if(toplam==sayi):
    print("mükemmel sayi")
else:
    print("Mükemmel sayı değildir.")


#Problem 2
#Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

#Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) 
#o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

#Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

sayi = input("Sayı giriniz ")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak= 0
toplam = 0


gecici_sayi = sayi

while(gecici_sayi>0):
    basamak = gecici_sayi % 10
    toplam +=basamak**basamak_sayisi
    gecici_sayi //= 10

if (toplam == sayi):
    print(sayi,"bir armstrong sayısıdır.")
else:
    print(sayi,"bir armstrong sayısı değildir.")



#Problem 3
#1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

#*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*
    

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {} ".format(i,j,i*j))

#Problem 4
#Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
#Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

#*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*

toplam=0 
while(True):
    sayi= input("Sayı giriniz: ")
    if (sayi =="q"):
        print("Programdan çıkılıyor..")
        print("Girdiğiniz sayıların toplamı : ",toplam)
        break
    else:
        sayi = int(sayi)
        toplam+=sayi

#Problem 5
#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi *continue* ile yapmaya çalışın.

for i in range(1,101):
    if(i % 3 != 0):
        continue
    print(i)


#Problem 6
#Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve 
#list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
    
#liste = [i for i in range(1,101) if(i % 2 ==0)]

#print(liste)