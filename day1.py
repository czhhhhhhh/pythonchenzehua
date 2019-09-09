# email = '666@qq.com'
# for e in email:
#     o = ord(e)-10
#     print(chr(o),end='')







# year = int(input('请输入一个年份:'))
## if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
#     print ('%d 是闰年' %year)
# else:
#     print ('%d 不是闰年' %year) 






#作业1
# C = float(input('请输入一个摄氏温度：'))
# F = 1.8*C +32
# print('华氏温度：%f'%F) 
    




#2
# import math
# π = math.pi
# r = float(input('输入圆柱体的半径')) 
# h = float(input('输入圆柱体的高'))
# area = r * r * π
# volume= area * h
# print('the area is %.4f'%area)
# print('the volume is %.1f '%volume)



#3
# feet = float(input('输入一个英尺：'))
# meters=feet/0.305
# print('%.1f feet is %.4f meters'%(feet,meters))




#4
# kg = float(input('输入水的重量（kg）：'))
# IT = float(input('输入水的初始温度：'))
# FT = float(input('输入水的最终温度：'))
# Q = kg * (FT - IT)*4184
# print('能量为%.1f'%Q)




#5
# c=float(input('输入差额'))
# n=float(input('输入年利率'))
# l=c*(n/1200)
# print('输出利息为%.6f'%l)





#6
# v0=float(input('输入v0'))
# v1=float(input('输入v1'))
# t=float(input('输入时间t'))
# a=(v1-v0)/t
# print('输出平均加速度a%.4f'%a)






#7
# money = float(input('请输入每个月存款数'))
# a = money * ( 1 + 0.00417)
# b = ( a + money) * ( 1 + 0.00417)
# c = ( b + money) * ( 1 + 0.00417)
# d = ( c + money) * ( 1 + 0.00417)
# e = ( d + money) * ( 1 + 0.00417)
# f = ( e + money) * ( 1 + 0.00417)
# print('六个月后账户余额为',f)


# n=float(input('请输入每月存款数：'))
# m=1
# a=n*1.00417
# print(a)
# while m<=5:
#     a=(a+100)*1.00417
#     m+=1
# print('六个月后的账户总额：', a)



#8
# number = int (input('请输入0到1000的数字：'))
# bai = number//100
# shi = number//10%10
# ge = number%10
# sum_ = bai + shi + ge
# print('the sum of the digits is:%d'%sum_)


#9
# import math
# π = math.pi
# tan = math.tan
# sin = math.sin
# r = float(input('输入五边形定点到中心的距离：'))
# s = 2 * r *sin (π /5)
# area = 5 * s * s /(4*tan(π/5))
# print('五边形的面积：%.2f'%area)





#10
# import math
# π = math.pi
# tan = math.tan
# s = float(input('输入五角形的边'))
# area = 5 * s * s/(4 * tan(π/5))
# print('五角形的面积为：%f'%area) 





#11
# import math
# π = math.pi
# tan = math.tan
# s = float(input('输入边长：'))
# n = int(input('输入边数：'))
# area = n * s * s/(4 * tan(π/n))
# print('正多边形的面积为：%f'%area)


#12
# a = int(input('请输入一个数：'))
# b = chr(a)
# print ('输出的字符：%s'%b)




#13
# name = str(input('请输入姓名：'))
# hours = float(input('一周工作时间：'))
# pay = float (input('每小时报酬：'))
# tax = float (input('联邦预扣税率'))
# a_tax = (input('州预扣税率'))
# print ('雇员名字：%s'%name)
# print('工作小时：%f'%hours)
# print('每小时报酬：%f'%tax)



#14
# number = str(input('请输入一个数：'))
# print(number [::-1])




