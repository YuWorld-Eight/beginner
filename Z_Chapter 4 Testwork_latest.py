import random

#定义变量
salary = int(1000)
balance_of_funds = int(10000)

for i in range(1,21):
    member_GPA = random.randint(1,10)  #随机生成员工绩点
    if member_GPA >=5:
        balance_of_funds -= salary
        print("员工%d， 发放工资%d,账户余额还剩下%d" % (i, salary, balance_of_funds))
        if balance_of_funds == 0:
            break
    else:
        print(f"员工{i}，绩效分低于5，不发工资，下一位")
print("工资发完了，下个月再来吧！")