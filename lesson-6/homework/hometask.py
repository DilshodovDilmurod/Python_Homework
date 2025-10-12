# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
def STDIN(n):
    nums= []
    sonlar = list(range(n))
    for son in sonlar:
        nums.append(son**2)
    return nums
print(STDIN(5))

## Loop-Based Exercises
1: Print first 10 natural numbers using a while loop
nums =[]
n=1
while n<=10:
    nums.append(n)
    n+=1
print(nums)
2: Print the following pattern
def pattern(n):
    m = 1
    sonlar = []
    while m <= n:
        sonlar.append(m)
        for son in sonlar:
            print(son, end=' ')
        print()
        m += 1
print(pattern(5))

# 3: Calculate sum of all numbers from 1 to a given number
def summa(num):
    summ = 0
    n = 1
    while n<=num:
        summ +=n
        n+=1
    return summ
print(summa(10))

# 4: Print multiplication table of a given number
def jadval_for_number(num):
    for n in range(1, 11):
        print(num*n)
print(jadval_for_number(3))

# 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number> 50 and number <=150 and number % 5==0:
        print(number)

# 6: Count the total number of digits in a number
sonlar = '23344536'
num = len(str(sonlar))
print(num)

# 7: Print reverse number pattern
def re_pattern(n):
    sonlar = list(range(1, n+1))    
    while sonlar:
        sonlar.reverse()
        for son in sonlar:
            print(son , end=' ')
        print()
        sonlar.reverse()
        sonlar.pop()
print(re_pattern(5))

# 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list2=[]
while list1:
    num = list1.pop()
    list2.append(num)
print(list2)

# 9: Display numbers from -10 to -1 using a for loop
for n in range(-10, 0):
    print(n)

#10: Display message “Done” after successful loop execution
for n in range(-10, 0):
    print(n)
print('done!')

# 11: Print all prime numbers within a range
Prime numbers between 25 and 50:
def tub_son_top(a, b):
    sonlar =[]
    for son in range(a, b):
        tub = True
        if son >1 :
            for n in range(2, son):
                if son %n ==0:
                    tub = False
            if tub:
                sonlar.append(son)
    return(sonlar)
print(tub_son_top(25, 50)) 
            
# 12: Display Fibonacci series up to 10 terms
def fibonachi(n): 
    """Necha fobonachi kerak bolsa 0 boshlab 
    oshancha fibonachi ni topib beradi"""
    b=0
    a= 1
    sonlar=[]
    sonlar.append(b)
    sonlar.append(a)
    for m in range(n-2):
        x = a
        a = a+b
        b = x
        sonlar.append(a)
    return sonlar
print(fibonachi(10))

# 13: Find the factorial of a given number
def factorial(num):
    dublicate=1
    for son in range(1, num+1):
        dublicate *=son
    return dublicate
print(factorial(5))

# 14 Return Uncommon Elements of Lists
nums = []
# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for son1 in list1:
    if son1 not in list2:
        nums.append(son1)
for son2 in list2:
    if son2 not in list1:
        nums.append(son2)
print(nums)
