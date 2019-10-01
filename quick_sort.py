def QuickSort(li):
    if len(li) <= 1:
        return li
    pivot = li[len(li) // 2]
    lesser_li, equal_li, greater_li = [], [], []
    for value in li:
        if value < pivot:
            lesser_li.append(value)
            print("lesser_li :", lesser_li)
        elif value > pivot:
            greater_li.append(value)
            print("greater_li :", greater_li)
        else:
            equal_li.append(value)
            print("equal_li :", equal_li)

    print("-------------------------------")
    return QuickSort(lesser_li) + equal_li + QuickSort(greater_li)
    # (lesser_li, equal_li, greater_li)
    # 1. lesser_li [5,4,2,1] ---> pivot=2 / lesser_li [1] / equal_li [2] / greater_li [5,4]
    # 2. equal_li [7]                                                    ---> QuickSort(greater_li) ....
    # 3. greater_li [8]
    #
    # + equal_li + greater_li

if __name__ == "__main__":
    li = [5, 4, 8, 7, 2, 1]
    print(li)
    print(QuickSort(li))
    # https://www.daleseo.com/sort-quick/
    
