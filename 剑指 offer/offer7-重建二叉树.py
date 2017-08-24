class Tree():
    def __init__(self,item,left,right):
        self.data = item
        self.left = left
        self.right = right

def Construct_tree1(pre_oder,mid_oder):
    if(len(pre_oder) == 0):
        return
    item = pre_oder[0]
    for i in range(len(pre_oder)):
        if (pre_oder[0] == mid_oder[i]):
            break
    left = Construct_tree(pre_oder[1:i+1],mid_oder[:i])
    right = Construct_tree(pre_oder[1+i:],mid_oder[1+i:])
    return Tree(item,left,right)

def Construct_tree2(mid_order,back_order):
    if(len(mid_order) == 0):
        return
    else:
        item = back_order[-1]
        for i in range(len(mid_order)):
            if(item == mid_order[i]):
                break
        left = Construct_tree2(mid_order[:i],back_order[:i])
        right = Construct_tree2(mid_order[i+1:],back_order[i:-1])
        return Tree(item,left,right)


pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
back_order = [7,4,2,5,8,6,3,1]
root = Construct_tree2(mid_order,back_order)
print(root.left.data)
# a = []
# if (len(a) != 0):
#     print(a[-1])



# class Node:
#   def __init__(self, data, left, right):
#     self.data = data
#     self.left = left
#     self.right = right
# def construct_tree(pre_order, mid_order):
#   # 忽略参数合法性判断
#   if len(pre_order) == 0 :
#     return None
#   # 前序遍历的第一个结点一定是根结点
#   root_data = pre_order[0]
#   for i in range(0, len(mid_order)):
#     if mid_order[i] == root_data:
#       break
#   # 递归构造左子树和右子树
#   left = construct_tree(pre_order[1 : 1 + i], mid_order[:i])
#   right = construct_tree(pre_order[1 + i:], mid_order[i+1:])
#   return Node(root_data, left, right)
# if __name__ == '__main__':
#   pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
#   mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
#   root = construct_tree(pre_order, mid_order)
#   print (root.data)

