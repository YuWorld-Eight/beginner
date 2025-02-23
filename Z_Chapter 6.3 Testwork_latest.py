my_str = "万过薪月，员序程马黑来，nohtyP学"

#方法一：倒序字符串，然后取出
inverse_str = my_str[::-1][9:14]
# index = inverse_str.index("黑")
# print(index) 
print(inverse_str)


#方法二：split分割"，"  replace替换"来" 最后倒序
my_list = my_str.split("，")
# print(my_list)
my_str1 = my_list[1][0:6:][::-1]
# print(my_str1)
# inverse_str1 = my_str1[::-1]
inverse_str1 = my_str1.replace("来", "")

print(inverse_str1)

