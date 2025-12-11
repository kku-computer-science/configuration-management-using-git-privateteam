from bubble import bubble_sort
from quick_sort import quick_sort

n = int(input("Enter the number of array elements:"))
arr = []
for i in range(n):
  number = int(input("Enter a number:"))
  arr.append(number)
print("\n 1.Bubble_Sort \n 2.Quick_Sort")
algor = int(input("Choose algorithm: "))
chooseAlgor = ""
ans = []
if (algor==1):
  ans = bubble_sort(arr)
  chooseAlgor = "Bubble_Sort"
elif (algor==2):
  ans = quick_sort(arr)
  chooseAlgor = "Quick_Sort"
else:
  print("Invalid input")
print(f'Algorithm: {chooseAlgor}')
print(f'result {ans}')
