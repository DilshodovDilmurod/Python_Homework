### Exception Handling Exercises
1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
num1 = float(input('birinchi soni kiriting:'))
num2 = float(input('Ikkinchi sonni kiriting:'))
try :
    num1/num2
except ZeroDivisionError:
    print('0 ga bolish mumkin emas')
else: 
    print(num1/num2)
2 Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
yosh = input('Yoshingiz kiritng:')
try: 
    yosh = int(yosh)
except:
    print('Butun son kiritmadingiz!')
else:
    print(f"Siz {2025 - yosh} yilda tugilgansiz")
3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
data = 'data.txt'
try:
    with open(data) as f: 
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {data} fayl mavjud emas, bosh fayl tanlang")
4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    num1 = input('Birnchi sonni kiriting:')
    num2 = input('Ikkinchi sonni kiritng:')
    if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
        raise TypeError("Kiritilgan qiymatlar son emas!")
    num1 = float(num1)
    num2 = float(num2)

    print(f"Kiritilgan sonlar {num1} va {num2}")
except TypeError as e:
    print("xato:", e)
5 Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.


file_path = 'D:\learning\python homework\sariq_dev_file/new1.txt'
try:
    with open(file_path, 'w') as f: 
        new_content = 'hello world1'
        data = f.write(new_content)
        print('dastur ishladi')
except PermissionError:
    print('Siz kiritgan file yoli xato')

6 Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.


cars = ['malibu', 'cobalt', 'gentra', 'onix']
index = 2
try:
    print(cars[index])
except IndexError:
    print('Mavjud bolmagan indexni kiritdingiz!')
7 Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.


try:
    while True:
        num = float(input("istalgan son kiriting:"))
except KeyboardInterrupt:
    print('Dastur tugadi')
8 Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
num1 = 12 
num2 = 23
try:
    print(num1 /0)
except ArithmeticError:
    print('xatolik bor')
9 Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.


try:
    with open('new_content.txt', 'r') as f: 
        data = f.read()
except UnicodeDecodeError:
    print('bundagi malumotlar formati xato')
10 Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.


class Talaba:
    def __init__(self, ism):
        self.ism = ism

talaba1 = Talaba('DAnyor')

try:
    print(talaba1.yosh)
except AttributeError:
    print('Bunday malumotga ega emas')
### Python File Input Output: Exercises, Practice, Solution

1 Write a Python program to read an entire text file.


filename = 'ustozlar.txt'
with open(filename) as fayl: 
    data = fayl.read()
2 Write a Python program to read an entire text file.


filename = 'ustozlar.txt'
n = int(input('necha qator oqilsin'))
with open(filename) as fayl: 
    for num in range(n):
        line = fayl.readline()
        if not line:
            break
        print(line)
3 Write a Python program to append text to a file and display the text.


filename = 'nex_file.txt'
matn  = input('faylga yozish uchun matn kiriting:')

with open(filename, 'a') as fayl:
    fayl.write(matn + "\n")

with open(filename, 'r') as file: 
    print(file.read())
4 Write a Python program to read last n lines of a file.


filename = 'nex_file.txt'
n = int(input('Oxirgi necha qatorni olish kerak!'))
with open(filename, 'r') as fayl:
    satrlar = fayl.readlines()
    lastlines = satrlar[-n:]
for lastline in lastlines:
    print(lastline.rstrip())
5 Write a Python program to read a file line by line and store it into a list.


filename = 'nex_file.txt'
new_list = []
with open(filename, 'r') as fayl:
    satrlar = fayl.readlines()
    for satr in satrlar:
        new_list.append(satr.rstrip())
print(new_list)
6 Write a Python program to read a file line by line and store it into a variable.


filename = 'nex_file.txt'
with open(filename, 'r') as fayl:
    satr = fayl.readlines()
    matn = satr
print(matn)
7 Write a Python program to read a file line by line and store it into an array.


filename = 'nex_file.txt'
new_array =[]
with open(filename, 'r') as fayl:
    for line in fayl:
        new_array.append(line.rstrip())
print(new_array)
8 Write a Python program to find the longest words.


with open('nex_file.txt', 'r') as fayl:
    matn = fayl.read()
for belgi in[',', '.', '!', '?', ';', ':', ]:
    matn = matn.replace(belgi, '')
sozlar = matn.split()

uzun_soz = max(sozlar, key=len)
print(f'Eng uzun soz {uzun_soz}')
print(f'harflar soni {len(uzun_soz)}')
9 Write a Python program to count the number of lines in a text file.


filename = 'nex_file.txt'
with open(filename, 'r') as fayl:
    num = 1
    while fayl.readlines():
        num +=1
print(num)
10 Write a Python program to count the frequency of words in a file.


filename = 'nex_file.txt'
with open(filename, 'r') as fayl:
    text = fayl.read()
for belgi in [',', '.', '!', '?', ';', ':', ]:
    text = text.replace(belgi, '')
words = text.split()
result = {}
for word in words:
    if word in result:
        result[word] +=1
    else:
        result[word] = 1
for word, num in result.items():
    print(f'{word} soni {num}')
11 Write a Python program to get the file size of a plain file.


import os

filename = 'nex_file.txt'
hajm = os.path.getsize(filename)
print(f'{filename} ning hajmi {hajm} bayt')
12 Write a Python program to write a list to a file.



filename = 'nex_file.txt'
cars = ['malibu', 'kia k5', 'captiva', 'tahoe']
with open(filename, 'a') as f:
    for car in cars:
        f.write("%s\n" % car)
13 Write a Python program to copy the contents of a file to another file.


filename = 'nex_file.txt'
with open(filename) as f: 
    data = f.read()
    print(data)

with open ('copy_file.txt', 'w') as f: 
    f.write(data)

with open('copy_file.txt', 'r') as f:
    print(f.read())
