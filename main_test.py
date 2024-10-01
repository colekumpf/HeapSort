from main import heapsort
from main import swap
from main import heapify
from main import build_max_heap


# #TEST NONE INPUT
print(heapsort(None) == None)

# # TEST EMPTY INPUT
print(heapsort([]) == [])

# # BASE TEST
print(heapsort([1,2,3]) == [1,2,3])

print(heapsort([3, 2, 1]) == [1,2,3])

print(heapsort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9])

# # TEST SWAP 
# x1 = 1
# x2 = 2
# print(f'PRE SWAP X1 = {x1} AND X2 ={x2}')
# x1, x2 = swap(x1, x2)
# print(f'AFTER SWAP X1 ={x1}, AND X2 = {x2}')
# short_list = [1,2]
# short_list[0], short_list[1] = swap(short_list[0], short_list[1])
# print(short_list)

# # TEST HEAPIFY
# simple_list = [1,2,3]
# heapify(simple_list,0)
# print(simple_list)

# TEST BUILD MAX HEAP
# complex_list = [1,2,3,4,5,6,7]
# build_max_heap(complex_list)
# print(complex_list)