## Function
#1. is_prime(n) funksiyasi
def is_prime(son):
    tub = True
    if son >1 :
       for n in range(2, son):
            if son %n ==0:
                tub = False
    return(tub)
print(is_prime(4))
print(is_prime(7))

#2 digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    num = k
    summa =0
    nums = [int(i) for i in str(num)]
    for num in nums:
        summa +=num
    return summa
print(digit_sum(234))

#3 Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def daraja(N):
    sonlar = []
    num = 1
    while 2**num< N:
        sonlar.append(2**num)
        num +=1
    return(sonlar)
print(daraja(129))
