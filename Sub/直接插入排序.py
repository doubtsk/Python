# Ö±½Ó²åÈëÅÅĞò
def InsertSort(list_):
    for i in range(1, len(list_)):
        j = i-1
        if list_[j] > list_[i]:
            temp = list_[i]
            list_[j+1] = list_[j]
            j -= 1
            while j >= 0 and list_[j] > temp:
                list_[j+1] = list_[j]
                j -= 1
                list_[j+1] = temp
    return list_
