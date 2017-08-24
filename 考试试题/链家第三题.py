def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low
def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


with open('random.in', 'r') as fr:
    n = fr.readline()
    x = fr.readline()
num = [int(l) for l in x.split()]
num = list(set(num))
length = len(num)
y = file('random.out','w')
y.write(length+'\n')
quick_sort(num,0,len(num)-1)
for i in range(len(num)):
    f.write(num[i]+" ")
