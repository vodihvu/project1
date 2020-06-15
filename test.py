from sort import bubble_sort
from sort import selection_sort
import numpy as np
print('nhap n')
array=np.zeros(int(input()))
for j in range(np.size(array)):
    print('nhap a[',j,']=')
    array[j]=int(input())
print('bubble_sort : 1\nselection_sort: 2')
b = int(input())
if b==1 :
    print('bubble_sort')
    bubble_sort(array)
if b==2 :
    print('selection_sort')
    selection_sort(array)
if b!=1 and b!=2 :
    print('no sort')
print(array)

