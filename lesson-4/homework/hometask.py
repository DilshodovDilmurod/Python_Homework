#1 Write a Python script to sort (ascending and descending) a dictionary by value.


#2 Write a Python script to add a key to a dictionary.
dic = {
    0:10, 1:20
}
dic[2] = 30
print(dic)

#3 Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#4 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
sonlar = {}
n = int(input('Son kiriting:'))
for num in range(1, n+1):
    num1 = num
    num2 = num**2
    sonlar[num1] = num2
print(sonlar)
#5 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
sonlar = {}
for num in range(1, 16):
    num1 = num
    num2 = num**2
    sonlar[num1] = num2
print(sonlar)

## Set Exercises
#1 Write a Python program to create a set.
my_sets = {'apple', 'banana', 'cherry'}
print(my_sets)

#2 Write a Python program to iterate over sets.
my_sets = {'apple', 'banana', 'cherry'}
for set in my_sets:
    print(set)

#3 Write a Python program to add member(s) to a set.
my_sets = {'apple', 'banana', 'cherry'}
my_sets.add('limon')
print(my_sets)
#4 Write a Python program to remove item(s) from a given set
my_sets = my_sets = {'apple', 'banana', 'cherry', 'limon'}
my_sets.remove('limon')
print(my_sets)

#5 Write a Python program to remove an item from a set if it is present in the set
my_sets = my_sets = {'apple', 'banana', 'cherry', 'limon'}
if 'limon' in my_sets:
    my_sets.remove('limon')
print(my_sets)
