                                  GASOLINE95  29.16
                                  GASOLINE91  25.31
                                  GASOLHOL95  21.2
                                  GASOLHOL91  21.68
                                  GASOLHOLe20 21.2
                                  DIESL       21.1
print("input money/litre or litre/money")
    M = input()
    O = input("ต้องการเดิมนเำมันอะไร?  ")
    P = int(input("ต้องการเติมเท่าไหร่?  "))
    A = O.upper()
    D = 0
    if "money/litre" in M:  
        if "1" in A:
            D = D +(P/29.16)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "2" in A:
            D = D +(P/25.30)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "3" in A:
            D = D +(P/21.68)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "4" in A:
            D = D +(P/20.2)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "5" in A:
            D = D +(P/21.2)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "6" in A:
            D = D +(P/21.1)
            print("Oil",'%.2f' %D , "ลิตร")
        else:
            print("กรุณาเลือกจำนวนเงินใหม่")
    elif "litre/money" in M:
        if "1" in A:
            D = D +(P*29.16)
            print("price",P,"฿")
        elif "2" in A:
            D = D +(p*25.30)
            print("price",P,"฿")
        elif "3" in A:
            D = D +(p*21.68)
            print("price",P,"฿")
        elif "4" in A:
            D = D +(P*20.2)
            print("price",P,"฿")
        elif "5" in A:
            D = D +(P*21.2)
            print("price",P,"฿")
        elif "6" in A:
            D = D +(P*21.1)
            print("price",p,"฿")
        else :
             print("กรุณาเลือกน้ำมันชนิดใหม่")
    else :
        print("กรุณาเเจ้งพนักงาน")
    print("5 - exit,  0 - back the menu. ")
    f="5"
    s="0"
    e=input()
    while not(e in '50'):
            print("5 - exit,  0 - back the menu ")
            e = input()
    if(e !=s):
       break