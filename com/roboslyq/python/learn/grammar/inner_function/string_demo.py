from soupsieve.util import upper

str1 = "a,b,c"
str2 = "d,e,f"

"""
1、转大小写
"""
print(str1.upper())

# 第三方包的upper方法
print(upper(str1))

"""
2、合并拼接
"""
print(str1 + str2)

"""
3、删除空白
"""
str3 = "   a,b,c   "
print(str3.strip())

int1 = 23
# print(int1 + ",hello world") # 此语句报错，因为23可能是字符2和3，也可以是数字23
print(str(int1) + ",hello world")  # 此语句正确
