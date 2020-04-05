"""""
toplam=0
for n in range(1,6):
    toplam=toplam+n #toplam+=n
    print(toplam)
"""""
"""""
toplam=0
n=1 toplam=1
n=2 toplam=3
n=3 toplam=6
n=4 toplam=10
n=5 toplam=15
"""
"""""
toplam=0
for x in range(1,21):
    if x%2==0:
        toplam=toplam+x
        print(x)
print("çift sayıların toplamı: ",toplam)

"""
"""
for a in range(1,51):
    if a%3==0 or a%4==0:
        print(a)
"""
"""
deger=int(input("değer giriniz: "))
for x in range(1,deger+1):
    print(" Sütun #",x,end=" ")
"""
"""
sayi=int(input("değer giriniz: "))
for satir in range(1,sayi+1):
    for sutun in range(1,sayi+1):
        deger=satir*sutun
        print(deger,end="      ")
    print()
"""
""""
kelime=input("kelime giriniz: ")
for harf in kelime:
 print(harf,end="  ")
"""


cumle=input("cümle giriniz: ")
sesliHarfSayisi=0
for x in cumle:
    if x=='A' or x=="a" or x=='e' or x=='E':
        sesliHarfSayisi+=1
print("Cümlede ",sesliHarfSayisi," tane A harfi var")
