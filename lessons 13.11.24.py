# import string
#
# print(string.hexdigits)
# print(string.octdigits)
# print(string.printable)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.whitespace)
# print(string.ascii_uppercase)


# myLst = list()
# print(type(myLst))

# myLst =[1,3,'Hello',True,10.5,500,'Hi']
# print(len(myLst))
# print(myLst[1])
# print(myLst[4:2:-1])
# print(myLst[::-1])
# print(myLst)
# print(myLst)
# # for i in range(10):
# #     print(i,end=" ")
#
# myLst = list()
# print(type(myLst))

# myLst =[1,3,'Hello',True,10.5,500,'Hi',500]
# myLst.append(100)
# print(myLst)
# myLst.insert(3,'World')
# print(myLst)
# myLst.remove(True)
# print(myLst)
# myLst.pop(3)
# print(myLst)
# a = myLst.count(500)
# print(a)
# ind = myLst.index("Hello")
# print(ind)
# print(myLst.reverse())
# print(myLst)
# myLst = [9,6,1,68,75,345]
# myLst.sort(reverse=False)
# print(myLst)
#
# myLst =[1,3,'Hello',True,10.5,500,'Hi',500]
#
# new_lst = myLst.copy()
# print(new_lst)
# myLst.remove("Hello")
# myLst.remove(True)
# print(new_lst)
# print(myLst)
# import copy
# mylst = [111,3,500,[10,20,30]]
# # new_lst = mylst.copy()
# # print(new_lst)
# # print(mylst)
#
# new = copy.deepcopy(mylst)
# print(new)
# mylst[3][0] = 500
# print(mylst)
# print(new)
#
# mylst.extend([100,100,100,100,100])
# print(mylst)
# # mylst.clear()
# # print(mylst)
# del mylst[3]
# print(mylst)

# s = "Hello World"
# new = s.split(" ")
# print(new)
# print(" ".join(new))
#
# text = "Hello World"
# new = text.split()
# words = []
# for i in range(2):
#     w = input("W")
#     words.append(w)
#     text = text.replace(w,w.upper())
# print(text)
# from random import randint
# mylst = []
# for i in range(11):
#     mylst.append(randint(1,20))
# suma = 0
# for i in range(len(mylst)):
#     suma += mylst[i]
# print(i)
# print(suma,suma / (i +1))


# from random import randint
# mylst = []
# suma , suma_1 ,suma_2 = 0,0,0
# for i in range(10):
#     mylst.append(randint(-20,20))
# for i in range(len(mylst)):
#     suma += mylst[i]
#     if mylst[i] < 0:
#         suma += mylst[i]
#     if mylst[i]%2==0:
#         suma_1+=mylst[i]
#     if mylst[i]%2==1:
#         suma_2+=mylst[i]
#
# print(suma,suma_1,suma_2)

