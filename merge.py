#!/usr/bin/env python3
def merge(list_left, list_right):
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1
        if index_right == len(list_right):
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            list_merged += list_right[index_right:]
            break
        
    return list_merged

def main():
    L1=[-98,-95,-89,-83,-82,-71,-69,-17,-3,4,5,7,13,21,26,64,69,73,82,98]
    L2=[-99,-84,-19,-2,2,17,35,42,57,65]
    L11=merge(L1,L2);

if __name__ == "__main__":
    main()
