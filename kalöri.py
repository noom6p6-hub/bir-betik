from os import system#bu modül betiği yeniden başlatmak için kullanılır
def killprocess():
    while True:
        killprocess = input("betiği kapatmak için 'q' tuşuna basınız")#kullanıcıya betiği kapatmak için q tuşuna basması gerektiğini söyler
        if killprocess == "q":
            quit()#kullanıcı q tuşuna bastığında betiği kapatır 
        else:
            print("bu betik yapılırken henüz geçerli bir bilgi bulunmamıştır ve hatalar olabilir kapamak için q gir")#kullanıcıya betiğin henüz geçerli bir bilgiye sahip olmadığını ve hata olabileceğini söyler
            continue
def start():
    """betiği yeniden başlatır"""#betiği yeniden başlatır
    system("python3 $PWD/kalöri.py")#betiği yeniden başlatır
while True:
    i = input("günde kaç kalöri alıyorsun?")

    if not i.isdecimal() or i.startswith("-") or i.isspace():#kullanıcının girdiği değerin sayı olup olmadığını kontrol eder ve negatif sayı veya boşluk olup olmadığını kontrol eder
        print("lütfen sayı giriniz ve negatif sayı girmeyiniz,boşluk bırakmayınız")#kullanıcıya sayı girmesi gerektiğini ve negatif sayı girmemesi gerektiğini söyler aynı zamanda boşluk bırakmaması gerektiğini söyler
        continue
    else:
        break

i = int(i)

if i == 0:
    print("sen hiç kalöri almıyorsun şüphesiz aç kalırsın bu yüzdemn bu mümkün değil yeniden başla")#kalöri 0 olamayacğını söyler
    start()
elif i > 0 and i < 1000:
    print("bu kalöri çok az ")#kullanıcıya kalöri miktarının az olduğunu söyler
    start()
elif i >= 1300 and i <= 1600:
    print("bu kalöri senin için normal ")#kullanıcıya kalöri miktarının normal olduğunu söyler
    killprocess()
elif i > 3000:
    print("bu kalöri yetişkinler için çok yüksek ")#kullanıcıya kalöri miktarının yetişkinler için çok yüksek olduğunu söyler
    killprocess()