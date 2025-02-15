student_age_list = [21,25,21,23,22,20]

student_age_list.append(31)
print(f"在尾部添加一个数字31：{student_age_list}\n")

new_list = [29,33,30]
student_age_list.extend(new_list)
print(f"在尾部添加一串数字(29,33,30)：{student_age_list}\n")

variable = student_age_list.pop(0)
print(f"取出第一个元素：{variable}")

count = len(student_age_list)
print(f"此数据列表有 {count} 个元素")

variable_1 = student_age_list.pop(count - 1)
print(f"取出末尾的元素是：{variable_1}")

print(student_age_list)
index = student_age_list.index(31)
print(f"数字31的下标是：{index}")