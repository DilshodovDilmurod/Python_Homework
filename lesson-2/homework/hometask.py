#1 Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input('ismingizni kiriting:')
birth = int(input('Tugilgan yilingizni kiriting:'))
print(f'{name.title()} siz {2025 - birth} yoshdasiz')

#2 Extract car names from the following text:
txt = 'LMaasleitbtui'
var1 = txt[0::2]
var2 = txt[1::2]
print(f'Birinchi moshina {var1}, Ikkinchi moshina {var2}')

#3. Extract car names from the following text:
txt = 'MsaatmiazD'
car1 = txt[0::2]
car2 = txt[-1::-2]
print(f'Birinchi mashina {car1.title()} Ikkinchi mashina {car2}')

#4 Extract the residence area from the following text:
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print(area)

#5 Write a Python program that takes a user input string and prints it in reverse order.
txt = input('matn kirit:')
txt = txt[::-1]
print(txt)

#6 Write a Python program that counts the number of vowels in a given string.
txt = 'Hello World'
volves = ['e', 'u', 'i', 'o', 'a']
summ = sum(txt.lower().count(v) for v in volves)
print(summ) 

#7 Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = [34, 54, 65, 45, 13, 78, 43, 98]
num_max = numbers[0]
for num in numbers:
    if num > num_max:
        num_max = num
print(num_max)

#8 Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
txt = input('writing same text:')
txt1 = txt[::-1]
if txt == txt1:
    print(1)
else :
    print(0)

#9 Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
email = input('Writing email pochta:')
domain = email.split('@')[0]
print(domain)

#10 Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

password_lenth = int(input('Pasword uzunligini kiriting:'))
characters = string.ascii_letters+string.digits+string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_lenth))
print(password)
