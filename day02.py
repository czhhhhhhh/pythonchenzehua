
#作业1
# a, b, c = map(float, input('请输入3个整数a,b,c, 用空格分隔：').split())  
# r1 = ((-b) + (b*b-4*a*c)**0.5)/(2*a)
# r2 = ((-b) - (b*b-4*a*c)**0.5)/(2*a)
# if b*b-4*a*c >0:
#     print('有两个根：r1=%f，r2=%f'%(r1,r2))
# elif b*b-4*a*c == 0:
#     print('有一个根:%f'%r1)
# elif b*b-4*a*c <0:
#     print('没有实根')


#2
# import numpy as np
# res = np.random.choice(101) 
# res1 =np.random.choice(101) 
# print(res)
# print(res1)
# ts = float(input('输入两个数字的和'))
# if ts == (res + res1):
#     print('答案正确')
# else:
#     print('答案错误')

#3
# jt  = int(input('今天星期几'))
# ts = int(input('几天后？'))
# wl  = jt  + ts 
# if wl  > 6:
#     print('未来是星期',wl % 7)
# else:
#     print('未来是星期',wl)


#4
# a, b, c = map(float, input('请输入3个整数a,b,c, 用空格分隔：').split())
# if a > b > c :
#     print(c ,b ,a)
# elif a >c >b:
#     print (b, c,a)
# elif b >a >c:
#     print(c,a,b)
# elif b >c >a:
#     print(a,c,b)
# elif c >a >b:
#     print(b,a,c)
# elif c >b >a:
#     print(a,b,c)


#5
# a, b = map(float, input('请输入第一种的质量和价格：').split())
# sum1 = b/a
# c, d = map(float, input('请输入第二种的质量和价格：').split())
# sum2 = d/c
# if sum1>sum2:
#     print('买第二种好')
# else:
#     print('买第一种好')




#6
# month,year = eval(input("Enter month an year (5,2004):"))
# leapyear =  year % 4
# if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8  or month == 10 or  month == 12:
#     month1 = 31
# elif month ==4 or  month == 6 or  month == 8  or  month ==9 or month ==11 :
#     month1 =30
# elif leapyear == 0 and   month == 2:
#     month1 = 29
# else:
#     month = 28
# print(year,"年",month,"月","有",month1,"天")









#7
# import numpy as np
# tishi = str(input('输入一个猜测值'))
# a = np.random.choice(['正面','反面',]) 
# print(a)
# if a == tishi:
#     print('猜测正确')
# else:
#     print('猜测错误')


#8
# import numpy as np
# user = int(input('请输入0（剪刀），1（石头）,2（布）,来进行游戏 '))
# com = np.random.choice(['石头','剪刀','布']) 
# print('系统是:%s'%com)
# if com == '石头' and user == 0 :
#     print('你输了')
# elif com == '石头' and user == 1 :
#     print('平局')
# elif com == '石头' and user == 2 :
#     print('你赢了')
# elif com == '剪刀' and user == 0 :
#     print('平局')
# elif com == '剪刀' and user == 1 :
#     print('你赢了')
# elif com == '剪刀' and user == 2 :
#     print('你输了')
# elif com == '布' and user == 0 :
#     print('你输了')
# elif com == '布' and user == 1 :
#     print('你赢了')
# elif com == '布' and user == 2 :
#     print('平局')





#9
# year = int(input('请输入年份：'))
# m = int(input('请输入月份：'))
# q = int(input('请输入天数：'))
# j = (year/100)//1
# k = year%100
# h = (q+((26*(m+1))/10)+k+(k/4)+(j/4)+5*j)%7
# print ('%d'%h)




#10
# import numpy as np
# res = np.random.choice(13) 
# res1 =np.random.choice(['梅花','红桃','方块','黑桃']) 
# print('你抽到的牌是%s%s'%(res1,res))


#11
# number = str(input('请输入一个数：'))
# number1 = (number [::-1])
# if number == number1:
#     print('是回文数')
# elif number != number1:
#     print('不是回文数')




#12
# a, b, c = map(float, input('请输入3个数a,b,c, 用空格分隔：').split())
# if a + b >c and a+c>b and b+c>a:
#     l = a+b+c
#     print('这个三角形的周长为%f'%l)
# else:
#     print('这个输入是非法的')




#13
# a = int(input('输入整数：'))
# for 


#14
# money = 10000
# i = 0
# while i < 14:
#     money = (money * 1.05)
#     i += 1
# print(money)








#16

# for i in range(100,1000):
#     if i % 5 ==  0 and i %6 ==0 :
#         print(i,end='\000')
    

#17






#18






#19







#20
# a = 0 
# for i in range(1,98,2):
#     a += i /(i+2)
# print(a)



#21
# a = 0
# for i in range(1,100000):
#     a += 4*((-1)**(i+1)/(2*i-1))
# print(a)




#22







#23
# a = 0
# for i in range(1,8,2):
#     for j in range(2,8):
#         if i !=j:
#             print(i,j)
#             a+=1
