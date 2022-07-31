def sort(array):

    for final in range(len(array), 0, -1):               
        for atual in range(0, final - 1):
            if array[atual] > array[atual + 1]:
                array[atual + 1], array[atual] = array[atual], array[atual + 1]
                

array = [13, 21, 3, 2, 7, 8, 14, 17, 9, 8]
sort(array)
print(array)