def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi =="toplama":
        print(f1(2,3))
    elif islem_adi =="çıkarma":
        print(f2(5,3))
    elif islem_adi =="çarpma":
        print(f3(3,4))
    elif islem_adi =="bölme":
        print(f4(10,2))
    else:
        print("Geçersiz işlem...")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "çıkarma")
islem(toplama, cikarma, carpma, bolme, "çarpma")
islem(toplama, cikarma, carpma, bolme, "bölme")
islem(toplama, cikarma, carpma, bolme, "a")