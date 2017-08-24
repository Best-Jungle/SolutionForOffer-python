#寻找数组中重复出现的数
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        i = 0
        if(numbers is None):
            return
        while(i<len(numbers)-1):
            if(numbers[i] != i):
                if(numbers[i] == numbers[numbers[i]]):
                    duplication.append(numbers[i])
                    i += 1
                else:
                    k = numbers[i]
                    numbers[i], numbers[k] = numbers[k], numbers[i]
            else:
                i += 1
        print(duplication)
        return duplication

a = Solution()
b = [1,2,2,3,3,4,5]
# b[0] , b[b[0]] = b[b[0]], b[0]
# print(b)
c = []
a.duplicate(b,c)