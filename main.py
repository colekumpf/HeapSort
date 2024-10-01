# subroutines if any, go here
def input_checker(hlist):
    if hlist is None:
        return None
    if len(hlist) == 0:
        return []
    if not isinstance(hlist, list):
        return False
    return True


def left_child_index(index):
    return index * 2 + 1


def right_child_index(index):
    return index * 2 + 2


def swap(element1, element2):
    temp = element1
    element1 = element2
    element2 = temp
    return element1, element2


def build_max_heap(hlist):
    first_non_leaf = (len(hlist) // 2) - 1
    for i in range(first_non_leaf, -1, -1):
        heapify(hlist, i)
    return hlist


def heapify(max_heap, index):
    left = left_child_index(index)
    right = right_child_index(index)
    largest = index
    if (left < len(max_heap)) and (max_heap[left] > max_heap[index]):
        largest = left
    if (right < len(max_heap)) and (max_heap[right] > max_heap[largest]):
        largest = right
    if largest != index:
        max_heap[index], max_heap[largest] = swap(max_heap[index], max_heap[largest])
        heapify(max_heap, largest)
    return 


# fill in heapsort
def heapsort(hlist):
    if input_checker(hlist) is not True:
        return input_checker(hlist)
    max_heap = build_max_heap(hlist[:])
    final_list = len(max_heap) * [0]
    for i in range(len(max_heap), 0, -1):
        max_heap[0], max_heap[-1] = swap(max_heap[0], max_heap[-1])
        final_list[i - 1] = max_heap.pop()
        heapify(max_heap, 0)
    return final_list
