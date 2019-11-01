"""
定义普通的列表，通过小括号，与shell脚本类型，但是是通过逗号分割
"""
# 只读列表（元组）：（）
# 读写列表: []
# kye value:{}
list1 = ("v1", "v2", "v3", "v4", "v5")
list2 = ["v1", "v2", "v3", "v4", "v5"]
# 遍列方式1
for i in list1:
    print(i)

# 遍列方式2
for i in range(len(list1)):
    print(list1[i])

# 修改元素

list2[1] = "hello"
print(list2)

# 添加元素
list2.append("v9")  # 末尾添加
print(list2)
list2.insert(1, "v10")  # 指定位置添加(所有元素位置后移)
print(list2)

# 删除元素
list2.pop()  # 末尾删除，可以当作栈使用
list2.pop(1)  # 根据索引位置删除
list2.remove("v4")  # 根据值删除
del list2[1]  # 根据索引位置删除
print(list2)
del list2[1]
print(list2)
