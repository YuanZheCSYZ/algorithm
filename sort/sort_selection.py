def selectionSort(alist):
    for fillSlot in range(len(alist)-1, 1, -1):
        maxSlot = 0
        for x in range(1, fillSlot+1):
            if alist[maxSlot] < alist[x]:
                maxSlot = x

        alist[fillSlot], alist[maxSlot] = alist[maxSlot], alist[fillSlot]
