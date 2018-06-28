# for i in range(1,101):
#     if i%2!=0:
#         print(i)



# str1 = '你好¥¥¥我正在学python@#@#现在需要&&&修改字符串'
# str2 = str1.replace('¥¥¥',' ').replace('@#@#',' ').replace('&&&',' ')
# print(str2)
#
# import re
# str1 = '你好¥¥¥我正在学python@#@#现在需要&&&修改字符串'
# str2 = re.sub('[¥@#&]+', ' ', str1)
# print(str2)



# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d * %d = %d\t' % (j, i, i*j), end='')
#         # j 控制每次从1 开始循环，i 运行完一次会加1
#     print()



# def calcute_pro(I):
#     if I <= 10:
#         a = I * 0.1
#         return a
#     elif I <=20 and I > 10:
#         b = 0.25 + I * 0.075
#         return b
#
# I = int(input('输入净利润：'))
# profit = calcute_pro(I)
# print('利润为%d万元时, 发奖金%d万元' % (I, profit))

# def calcute_profit(I):
#     arr = [10, 60, 40, 20, 10,0]
#     rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
#
#     r = 0
#     for idx in range(0, 6): #有6个分界值，循环6次
#         if I > arr[idx]:
#             r = r + (I - arr[idx]) * rat[idx]
#             I = arr[idx]
#     return r
#
# I = int(input('输入净利润（万元）：'))
# profit = calcute_profit(I)
# print('利润为%d万元时, 发奖金%d万元' % (I, profit))


# import operator
# numdict = {1:2, 3:4, 4:3, 2:1, 0:0}
# sorted_numdict = sorted(numdict.items(), key=operator.itemgetter(1))
# print(sorted_numdict)

