#1:
# def scores(a,b,c,d):
#    x = [a,b,c,d]
#    y = sorted(x)
#    z = y[3]
#    for i in range(len(x)):
#        if x[i] >= z - 10:
#            print('成绩为A')
#        elif x[i] >= z - 20:
#            print('成绩为B')
#        elif x[i] >= z - 30:
#            print('成绩为C')
#        elif x[i] >= z - 40:
#            print('成绩为D')
#        else:
#            print('成绩为F')
# scores(40,55,70,58)



#2：
# a = [1,2,3,4,0,9,8,7,9,4,2,7,3,16,7]
# b = a[::-1]
# print(b)






#3:
# def occurso(str1):
#     str3 = str1
#     str2 = []
#     for i in str1:
#         if i not in str2 :
#             str2.append(i)
#     for i in range(len(str2)):
#         num1 = 0
#         for j in range(len(str3)):
#             if str3[j] == str2[i]:
#                 num1 += 1
#             else:
#                 num1 = num1
#         print('str2[i]%d'%num1)
# occurso([1,2,3,4,5,4,3,5,3,2,4,2])




#4
# def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
# num1 = 0
# num2 = 0
# def fenshu(list_):
#    pinjun = average(list_)
#    for i in range(len(list_)):      
#        global num1
#        global num2
#        if list_[i] > pinjun: 
#            num1 += 1
#        elif list_[i] < pinjun:
#            num2 += 1
#        else:
#            pass
#    print(num1)
#    print(num2)
#    print(pinjun)
# fenshu([2,4,2,4,8])



#def indexOFSmallestElement(lst):
#    lst1 = lst
#    lst2 = sorted(lst)
#    zuixiao = lst2[0]
#
#    for i in range(len(lst1)):
#        if lst1[i] == zuixiao:
#            print('最小元素的下标再第几个呢，就是这里>>%d'%(i+1))
#            
#indexOFSmallestElement([3,4,2,7,5,4,1,4,3,4])