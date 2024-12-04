# def old_num(a,b):
#     print(id(a),id(b))
#
#
#
#
# x = 1
# y = 2
# print(id(x),id(y))
# old_num(x,y)

# def count_num(a, b):
#     for i in range(a,b+1):
#         if i % 2:
#             print(i, end=" ")
#
#
# a = 1
# b = 50
# count_num(a,b)


# def lines(w,d,s):
#     for i in range(w):
#         if d == 1:
#             print(s,end="")
#         elif d == 2:
#             print(s)
#
#
# w = int(input("Довжина "))
# d = int(input("Напрямок 1,2 "))
# s = input("Символ ")
# lines(w,d,s)

# def maximum(a,b,c,d):
#     return max(a,b,c,d)
#
#
# a = 1
# b = 14



# c = 3
# d = 34
# max_num = maximum(a,b,c,d)
# print(max_num)

# def suma_num(a,b):
#     res = 0
#     for i in range(a,b+1):
#         res += i
#     return res
#
#
# a, b = 5,12
# suma = suma_num(a,b)
# print(suma)


# def easy_num(a):
#     if a <=2:
#         return True
#     for i in range(2,a):
#         if a % 2== 0:
#             return False
#         else:
#             return True
#
#
# a = 7
# easy_num(a)


def happy_num(a):
    a1 = sum(map(int,str(a)[0:3]))
    a2 = sum(map(int,str(a)[3:6]))
    if a1 == a2 :
        print("Heppy")
    else:
        print("not Happy")


a = 123420
happy_num(a)