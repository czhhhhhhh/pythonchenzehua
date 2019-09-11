# 作业1

# x = 1
# def getPentagonalNumber(n):
#    j = n * (3 * n - 1) / 2
#    return j
# M = getPentagonalNumber(x)
# print('显示前100个五角树:>>')
# count = 0
# for i in range(100):
#    j = getPentagonalNumber(x)
#    x += 1
#    i += 1
#    print(j,end='   ')
#    count += 1
#    if(count%10==0):
#        print(end='\n')



# 2
# def sumDigits(n):
#     ge = n % 10
#     a = 0
#     for i in range (n) :
#         bai = n // (10 * (10 **i))%10
#         a += bai
#     sum = a + ge
#     print('这个整数和为：%f'%sum)  
# sumDigits(1234)


#3
# def displaySortedNumbers(num1,num2,num3):
#     i = 0
#     while i<4:
#         if num1 > num2:
#             x = num2
#             num2 = num1 
#             num1 = x
#         elif num2 > num3:
#             x = num3
#             num3 = num2
#             num2 = x
#         i += 1
#     print(num1,num2,num3)
# displaySortedNumbers(7,5,6)



#5
# def printchars():
#     for i in range(73,91):
#         print(chr(i),end=' ')
#         if i % 10 == 0:
#             print('\n')
# printchars()



#7
# def numberOfDaysInAYear(year):
#     for count in range(year,year+11):
#         if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
#             print("%d年有366天"%count)
#         else:
#             print("%d年有365天"%count)
# numberOfDaysInAYear(2010)



#8
# def distance(x1,x2,y1,y2):
#     dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     print("这两个点的距离是：%f"%dis)
# distance(1,3,3,2)






#10
# import random
# def shaizi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# shaizi()
