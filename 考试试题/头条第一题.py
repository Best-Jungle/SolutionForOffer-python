#找最大点集合
def sort(array):#按 x 排序
    for i in range(len(array)):
        for j in range(i):
            if array[j][0] > array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def find(N):
    for i in range(len(N)):
        count = 0
        for j in range(i,len(N)):
            if (N[i][1]<N[j][1]):
                break
            else:
                count += 1
        if(count == len(N)-i):
            print(N[i])


import sys
if __name__ == "__main__":
    # # 读取第一行的n
    # N = []
    # n = int(sys.stdin.readline().strip())
    # for i in range(n):    # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     num = list(map(int, line.split()))
    #     N.append(num)
    N = [[1,2],[5,3],[4,6],[7,5],[9,0]]
    N = sort(N)
    m = find(N)






