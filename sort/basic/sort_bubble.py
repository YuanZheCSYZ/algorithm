def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for x in range(passnum):
            if alist[x] > alist[x+1]:
                alist[x], alist[x+1] = alist[x+1], alist[x]
