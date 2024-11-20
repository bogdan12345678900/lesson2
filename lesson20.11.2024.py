# Д
#n = 10
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n- 1 or i == j or j == n-i-1 or i <j and i < n-1-j or i >j and i > n -1-j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# E
# n = 10
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n- 1 or i == j or j == n-i-1 or j <i and j < n -1-i or j > i and j>n-1-i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# дз
# text = "kjdfghd' djfgh eruigh , ruehgrgjdgh 23524687 903456 ,ikujtreiotj"
# temp = text.split(",")
# new = []
# for elem in temp:
#      new.append(elem.strip().capitalize().replace(".","!")+"!")
# print(new)
# res_text = "".join(new).rstrip()
# print(res_text)
# count = 0
# for i in res_text:
#     if i.isdigit():
#         count += 1
# count_s = 0
# symbol = ".,!?;:"
# for s in symbol:
#     if s in res_text:
#         count_s += res_text.count(s)
#
# print(count_s)
#
# s = "+"
# expression = "12+23"
# if s in expression:

# a = [1,2,3,4]
# b = [3,4,5,6]
# c = []
# for i in a:
#     if i not in b :
#         c.append(i)
# for i in b:
#     if i not in a :
#         c.append(i)
# print(c)

from random import randint
# lst =[[],[],[]]
# n,m = 3,4
# for i in range(n):
#     m = randint(5,10)
#     for j in range(m):
#         lst[i].append(randint(1,50))
# print(lst)
# for i in range(n):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end=" ")
#     print()


# gen_lst = [[randint(1,50)for i in range(m) ]for j in range(n)]
# print(gen_lst)
# x_max = []
# x_min = []
# for i in range(n):
#     temp = gen_lst[i][0]
#     for j in range(1,m):
#         if temp < gen_lst[i][j]:
#             temp = gen_lst[i][j]
#     x_max.append(temp)
# print(x_max)
# for i in range(n):
#     temp = gen_lst[0][i]
#     for j in range(1,m):
#         if temp > gen_lst[i][j]:
#             temp = gen_lst[i][j]
#     x_min.append(temp)
# print(x_min)

# myLst = [1,2,3,2,1]
# if myLst == myLst[::-1]:
#     print("ok")
# else:
#     print("No")
