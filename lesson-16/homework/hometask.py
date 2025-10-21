1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
import numpy as np 
my_list = [12.23, 13.32, 100, 36.32]
my_arr = np.array(my_list)
my_arr
2.  Create 3x3 Matrix (2?10)
arrr = np.arange(2, 11).reshape(3,3)
arrr
3. Null Vector (10) & Update Sixth
null_arr = np.zeros(10)
null_arr[5] = 11
null_arr
4  Array from 12 to 38
array_12_38 = np.arange(12, 38)
array_12_38
5. Convert Array to Float Type
int_array = [1,2,3,4]
float_array = np.array(int_array, dtype=np.float32)
float_array.dtype
6 Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.


cen1_arr = np.array([0, 12, 45.21, 34, 99.91])
fan2_arr = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])
fan1_arr = cen1_arr* 9/5 +32
fan1_arr.sort()
cen2_arr = (fan2_arr-32)* 5/9
rev_cen2 = np.sort(-cen2_arr)
print(fan1_arr)
print(rev_cen2)
7 Write a NumPy program to append values to the end of an array.
alter_arr = np.array([10, 20, 30])
new_arr = np.append(alter_arr, [40, 50, 60, 70, 80, 90])
new_arr
8 Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.


num_arr = np.random.randn(10)
print(f"mean:{np.mean(num_arr)}")
print(f"median: {np.median(num_arr)}")
print(f"std: {np.std(num_arr)}")
9. Create a 10x10 array with random values and find the minimum and maximum values.


min_max_arr = np.random.randn(10,10)
print(f"min:{np.min(min_max_arr)}")
print(f"max:{np.max(min_max_arr)}")
10 Create a 3x3x3 array with random values.


my_arr = np.random.randn(3,3,3)
my_arr
