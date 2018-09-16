"""
https://www.youtube.com/watch?v=VNbkzsnllsU
"""

from collections import defaultdict

def find_largest_rectangle(histogram:list):
    largest = 0
    last_hight = 0
    current_largest_map = defaultdict(int)
    for bar_hight in histogram:
        for i in range(1, min(last_hight, bar_hight)+1):
            current_largest_map[i] += i
            if largest < current_largest_map[i]:
                largest = current_largest_map[i]
        print("->{} => {}".format(bar_hight, current_largest_map))

        if bar_hight > last_hight:
            for i in range(last_hight+1, bar_hight+1):
                current_largest_map[i] = i
                if largest < i:
                    largest = i
        
        print("->{} => {}".format(bar_hight, current_largest_map))
        last_hight = bar_hight
    
    return largest

if __name__ == "__main__":
    print(find_largest_rectangle([1,2,3,4,5])) #9
    print(find_largest_rectangle([1,2,3,4,5,0,10])) #10
    print(find_largest_rectangle([1,2,3,4,5,4,3,2,1])) #15
    print(find_largest_rectangle([1,2,3,4,5,4,3,2,1,2,3,4,5])) #15
