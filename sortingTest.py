from buble import buble_sort
from quick_sort import quick_sort

n = int(input("Enter the number of array elements:"))
arr = []
for i in range(n):
  number = int(input("Enter the number:"))
  arr.append(number)
#print(f'your array is {arr}')
print("\n 1.Bubble \n 2.Quick")
algor = int(input("Choose algorithm: "))
ans = []
if (algor==1):
  ans = bubble_sort(arr)
elif (algor==2):
  ans = quick_sort(arr)
print(f'result {ans}')
