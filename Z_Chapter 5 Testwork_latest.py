import sys

#定义所需变量
balance =  int(5000000)
name_list_cardnum = [["屿的故事", "2424090125"], ["周洽铠", "2424090108"]] #名单列表
# card_num_list = ["2424090125", "2424090108"] #卡号列表 1：1对齐


#用户切换区域 卡号校验
card_num = input("您好欢迎使用存取款一体机，请输入卡号：")
limit_of_times = 5 #卡号输入限制次数
for i in range(5):
    count = 0 #验证卡号长度每次初始化为0
    for i in card_num:
        count += 1
    if count == 10:
        break
    else:
        limit_of_times -= 1
        if limit_of_times == 0:
            print("输入次数超过限制，程序已结束")
            sys.exit(0)
        card_num = input("卡号输入有误，请检查后在下方重新输入 (剩余次数 %d 次)\n" % limit_of_times)
        

#用户0
if card_num == name_list_cardnum[0][1]:
    name_0 = name_list_cardnum[0][0]
    print(f"Welcome  -用户 {name_0}\n")
    allow = 1  #验证用户合法性 打开主程序
#用户1
if card_num == name_list_cardnum[1][1]:
    name_1 = name_list_cardnum[1][0]
    print(f"Welcome  -用户 {name_1}\n")
    allow = 1

#以下为function区域 使用数字选择切换
def func_1():
    print("----------------查询余额----------------")
    print(f"卡号 {card_num} 您好，您的余额为：{balance}")

def func_2():
    print("----------------取款中----------------")
    withdrawal_money = int(input(f" {name_1}请输入取款金额：\n"))
    print(f"本次取款 {withdrawal_money}\n 您的余额剩余 {balance - withdrawal_money}")

def func_3():
    print("----------------存款中----------------")
    deposit_money = int(input("请将纸币放入机柜下方存钱口中，并输入存入金额：\n"))
    print(f"存入{deposit_money}元成功，您的余额为{balance + deposit_money}")

def func_4():
    print("     卡已弹出，请取卡")
    sys.exit(0)

#主程序----------------------------------------------------------------------------------
if allow == 1:
    print("----------------主菜单----------------")
    print("           查询余额  [数字1]")
    print("            取 款    [数字2]")
    print("            存 款    [数字3]")
    print("            退 出    [数字4]")

    select = int(input("请输入对应数字进行操作："))

    if select == 1:
        func_1()

    if select == 2:
        func_2()

    if select == 3:
        func_3()

    if select == 4:
        func_4()