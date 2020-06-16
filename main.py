from sort import bubble_sort
from sort import selection_sort
import numpy as np
print('Enter the array size n')
array=np.zeros(int(input()))
for j in range(np.size(array)):
    print('Enter a[',j,']=')
    array[j]=int(input())
print('array:',array)
print('which algorithm you want to use…\nbubble_sort : 1\nselection_sort: 2')
b = int(input())
if b==1 :
    print('Bubble_sort:')
    bubble_sort(array)
if b==2 :
    print('Selection_sort:')
    selection_sort(array)
if b!=1 and b!=2 :
    print('No sort')
print(array)

