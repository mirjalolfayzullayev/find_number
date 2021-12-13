import random
def sontop_u(n=10):
    "Kompyuter son o'ylaydi, biz esa uni topamiz!"
    s = 0
    x = random.randint(1, n)
    print(f"1 dan {n} gacha son o'yladim topa olasizmi?")
    while True:
        s += 1
        y = int(input(">>"))
        if y < x:
            print("Kompyuter o'ylagan son {} dan katta, qaytadan urunib ko'ring!".format(y))
        elif y > x:
            print("Kompyuter o'ylagan son {} dan kichik, qaytadan urunib ko'ring!".format(y))
        else:
            break
    print("Kompyuter {} sonini o'ylagan edi. Tabriklaymiz siz {} urunishda topdingiz!".format(x, s))
    return s


def sontop_pc(n=10):
    "Biz son o'ylaymiz kompyuter esa uni topadi"
    input(f"1 dan {n} gacha bo'lgan son o'ylang va ixtiyoriy tugmani bosing\n>>")
    s = 0
    x1 = 1
    x2 = n
    while True:
        s += 1
        if x1 != x2:
            x = random.randint(x1,x2)
        else:
            break
        flag = input(f"Siz o'ylagan son {x}. To'g'i bo'lsa (t), siz o'ylagan sondan kichik bo'lsa (-),"
                     f"katta bo'lsa (+) ni kiriting\n>>").lower()
        # if x == x1:
        #     break
        if flag == "-" and x1 != x2:
            x2 = x-1
        elif flag == "+" and x1 != x2:
            x1 = x+1
        else:
            break
    print(f"Siz o'ylagan sonni {s} urunishda topdim!")   
    return s

def play():
    while True:
        print("Keling son topish o'yinini o'ynaymiz!")
        oraliq = int(input("Nechchigacha bo'lgan oraliqdagi sonlardan o'ynaymiz?\n>>"))
        urunish_u = sontop_u(oraliq)
        urunish_pc = sontop_pc(oraliq)
        if urunish_u < urunish_pc:
            print("Tabriklaymiz siz yutdingiz!")
        elif urunish_u > urunish_pc:
            print("Siz yutqazdingiz!")
        else:
            print("Durang")
        flag = input("Yana o'ynaymizmi(Yes/No):").lower()
        if flag == 'yes':
            continue
        else:
            break       
play()













