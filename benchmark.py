from timeit import time
from random import randrange




# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10700)]

mylist2 = mylist.copy()



# Algoritmo di ordinamento


def mymin(list):
    m_idx = 0
    m = list[0]
    for n_idx, n in enumerate(list):
        if n < m:
            m = n
            m_idx = n_idx
    return m, m_idx




start_time = time.time()
for idx in range(len(mylist)):
    # compute minimum and the index relative to the slice
    m, m_idx = mymin(mylist[idx::])
    # convert relative index into global index
    m_idx += idx
    swap = mylist[idx]
    mylist[idx] = m
    mylist[m_idx] = swap


stop_time = time.time()
print("selection_sort_time")
print(f"{(stop_time-start_time):.7f}")

#bubblesort

def bubble_sort (list):
    start_time = time.time()
    for index in range (len (list)):
        swapped = False
        for jdex in range (index, len (list)):
            if (list [index]> list [jdex]):
                list [index], list [jdex] = list [jdex], list [index]
                swapped = True
        if not swapped:
            break
    stop_time = time.time()
    print("bubble_sort_time")
    print(f"{(stop_time-start_time):.7f}")        
bubble_sort(mylist2)