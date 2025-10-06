#1 Write a Python program to generate a random password containing letters, digits, and special characters.
mevalar= ['olma', 'uzum', 'anjir', 'anor', 'shaftoli']
print(mevalar[2])

#2 Create two lists of numbers and concatenate them into a single list.
list1 = [1, 4, 6, 7, 34, 65]
list2 = [76, 65, 56, 78]
list1.extend(list2)
print(list1)

#3 Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [23, 443, 345, 2345, 764, 787, 345,343]
new_list =[]
new_list.append(numbers.pop(0))
new_list.append(numbers.pop(-1))
new_list.append(numbers.pop(3))
print(new_list)

#4 Create a list of your five favorite movies and convert it into a tuple.
movies = ['Mexanik', 'Merlin', 'Polat', 'Qasoskorlar', 'Qutqaruvchilar']
movies = tuple(movies)
print(movies)
 
#5 Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['Dubai', 'Washington', 'Toshkent', 'Abu-Daby', 'Parij']
if 'Parij' in cities:
    print('Royxatda Parij bor')
else: 
    print('Royxatda Parij yoq')

#6 Create a list of numbers and duplicate it without using loops.
numbers = [12, 32, 43, 56, 34, 76, 67, 32, 43]
print(numbers)

#7 Given a list of numbers, swap the first and last elements.
numbers = [23, 43, 54, 342, 65, 2325, 65, 542, 7634]
print(numbers)
num = numbers[0]
numbers[0]= numbers[-1]
numbers[-1] = num
print(numbers)

#8 Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = list(range(11))
print(numbers[2:8])

#9 Create a list of colors and count how many times "blue" appears in the list.
colors = ['blue', 'white', 'green', 'blue', 'black']
cnt = colors.count('blue')
print(cnt)

#10 Given a tuple of animals, find the index of "lion".
animals = ['cat', 'dog', 'lion', 'elefant', 'mouse']
num = animals.index('lion')
print(num)

#11 Create two tuples of numbers and merge them into a single tuple.
nums1 = (12, 32, 43, 65, 67, 87, 56, 98)
nums2 = (43, 56, 45, 6, 76, 84)
n = nums1 + nums2
print(n)

#12 Given a list and a tuple, find and print their lengths.
lists = [22, 323, 43, 232, 54, 543, 3234]
tuples = (453, 43, 23, 54, 65, 23, 9)
len1 = len(lists)
len2 = len(tuples)
print(f'len of lists : {len1}, len of tuples: {len2}')

#13 Create a tuple of five numbers and convert it into a list.
nums = (12, 332, 43, 232, 234)
num_list = list(nums)
print(num_list)

# 14 Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (343, 647, 6573, 4367, 25567, 357, 36732, 786)
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num< min_num:
        min_num = num
print(f'Min numbers {min_num}, max numbers {max_num}')

# 15 Create a tuple of words and print it in reverse order.
matn = ('olma', 'anor', 'anjir','jiyda', 'limon', 'banan')
print(sorted(matn, reverse=True))
