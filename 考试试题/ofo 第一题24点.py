#!/bin/python
import sys
import os
import math
PRECISION = 1E-6
NUMBER_TO_BE_CAL = 24
g_expression = ['', '', '', '']

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
#******************************开始写代码******************************
def solve(n):
    if (1 == n):
        if (math.fabs(NUMBER_TO_BE_CAL - g_number[0]) < PRECISION):
            return True
        else:
            return False
    else:
        for i in range(0, n):
            for j in range(i + 1, n):
                a = g_number[i]
                b = g_number[j]
                # **********************************
                #   将剩下的有效数字往前挪，
                #   由于两数计算结果保存在number[i]中，
                #   所以将数组末元素覆盖number[j]即可
                #   *******************************
                g_number[j] = g_number[n - 1]
                expa = g_expression[i]
                expb = g_expression[j]
                g_expression[j] = g_expression[n - 1]
                # 计算a+b
                g_expression[i] = '(' + expa + '+' + expb + ')'
                g_number[i] = a + b
                if (solve(n - 1)):
                    return True;

                # 计算a-b
                g_expression[i] = '(' + expa + '-' + expb + ')'
                g_number[i] = a - b
                if (solve(n - 1)):
                    return True

                # 计算b-a
                g_expression[i] = '(' + expb + '-' + expa + ')'
                g_number[i] = b - a
                if (solve(n - 1)):
                    return True

                # 计算(a*b)
                g_expression[i] = '(' + expa + '*' + expb + ')'
                g_number[i] = a * b
                if (solve(n - 1)):
                    return True;

                # 计算(a/b)
                if (b != 0):
                    g_expression[i] = '(' + expa + '/' + expb + ')'
                    g_number[i] = a / b
                    if (solve(n - 1)):
                        return True

                        # 计算(b/a)
                    if (a != 0):
                        g_expression[i] = '(' + expb + '/' + expa + ')'
                        g_number[i] = b / a
                        if (solve(n - 1)):
                            return True

                            # 恢复现场
                g_number[i] = a
                g_number[j] = b
                g_expression[i] = expa
                g_expression[j] = expb
        return False



#******************************结束写代码******************************


_data_rows = 0
_data_cols = 0
t = int(input())
n = int(input())

_data = []
for _data_i in range(t):
    _data_temp = list( map(float,input().strip().split(' ')) )
    _data.append(_data_temp)


for g_number in _data:

    if(solve(n)):
        print("true")
    else:
        print("false")


