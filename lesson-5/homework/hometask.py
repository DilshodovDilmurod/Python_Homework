#def is_leap(year): """ Determines whether a given year is a leap year.
def is_leap(year):
    leap_year = True
    if (year%4==0 and year % 100 !=0) or year%400==0:
        leap_year = True
    else: 
        leap_year = False
    return leap_year
print(is_leap(1604))

#Given an integer, n, perform the following conditional actions:
def juft_toq(n):
    result = ''
    if n % 2 ==1:
        result='weird'
    elif n%2==0 and n in range(2, 6):
        result = 'Not weird'
    elif n%2==0 and n in range(6, 21):
        result = 'weird'
    elif n %2 == 0 and n > 20:
        result = 'Not weird' 
    return result
print(juft_toq(4))
print(juft_toq(3))

#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#1-solution
def oraliq(a, b):
    if a % 2 !=0:
        a+=1
    return(list(range(a, b+1, 2)))
print(oraliq(3, 9))
#2-solution
a = 12
b = 24
nums =[]
sonlar = list(range(a, b+1))
for son in sonlar:
    if son%2==0:
        nums.append(son)
print(nums)
