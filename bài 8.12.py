#-------------------------------------------------------#
# in ra màn hình số nguyên tố <1000                     #
# import math                                           #
# a = 0                                                 #
# b = 1000                                              #
# for i in range(a,b+1):                                #
#     if i >0:                                          #
#         for j in range(2,int(math.sqrt(i))+1):        #
#             if i%j == 0:                              #
#                 break                                 #
#         else:                                         #
#             print(i)                                  #
#-------------------------------------------------------#
n = int(input("nhập vào số n lớn hơn 1: "))
a = True
if n<2:
    a = False
elif n ==2:
    a = True
elif n%2 ==0:
    a = False
else:
    for i in range(3,n,2):
        if n%i==0:
            a = False
if a == True:
    print(n, " là số nguyên tố")
else:
    print(n," không phải là số nguyên tố")