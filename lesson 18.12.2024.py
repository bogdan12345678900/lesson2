# # test = lambda x:x*2
# # print(test(5))
# # print(test(10))
#
# my_lst = [1,2,54,5,8,0]
#
# new_lst = list(filter(lambda x: (x%2==0),my_lst))
# new_map = map(int,["1",'2'])
# print(new_lst)


# letter = 'q w e r t y'.split()
# print(letter)
# def fil_letter(letter):
#     v = ["a","e","y","o","u"]
#     for let in letter:
#         return True if let in v else False
#
#
# letter = 'q w e r t y'.split()
# print(fil_letter(letter))
#
# filt = list(filter(fil_letter,letter))
# print(filt)



#
# def fil_letter(letter):
#     v = ["a","e","y","o","u"]
#     for let in letter:
#         return True if let in v else False
#
#
# res = lambda letter: True if letter in v else False
#
# v = ["a", "e", "y", "o", "u"]
# letter = 'q w e r t y'.split()
# filt = list(filter(res,letter))
# print(fil_letter(letter))

# res  = any([1,3,4,2])
# print(res)
# res  = any([0,0,0,0,0])
# print(res)
# print(all([1,2,3,4]))
# print(all([1,2,3,4,0]))

# def func_recur(n):
#     if n <= 0 :
#         print("Stop")
#     else:
#         print(n)
#         func_recur(n-1)
#
#
# func_recur(10)


# def sum_num(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_num(n-1)
#
# print(sum_num(5))

# def factor(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n * factor(5)

# def step(a,n):
#     if n == 0:
#         return 1
#     else:
#         return n *step(a,n-1)
#
#
# print(step(2,5))


# def step(a,n):
#     if n == 0:
#         return 1
#     elif n <0:
#         return 1/step(a,-n)
#     else:
#         return n /step(a,n-1)

#
# def sum_num(a,b):
#     if a > b:
#         return 0
#     else:
#         return a + sum_num(a+1,b)
#
#
# print(sum_num(5,15))



# def num_12(n):
#     if n == 0:
#         return 1
#     else:
#         print("*",end="")
#         return num_12(n-1)
#
#
# num_12(5)

#
#
# from random import randint
#
#
# def draw_pole(lst):
#     num = 1
#     for i in range(3):
#         for j in range(3):
#             print(num,end=" ")
#             num +=1
#         print()
#
# def move_com():
#     com = "X"
#     while True:
#         p = randint(1,9)
#         if p in lst:
#             lst[p] = com
#             break
#
#
# def move_user():
#     user = "O"
#     while True:
#         us = int(input("1-9: "))
#         if us in lst:
#             lst[us] = user
#             break
#
#
# def game():
#     for _ in range(5):
#         move_com()
#         move_user()
#         if lst[1]==lst[2] and lst[1]==lst[3]:
#             print("win")
#             return
# if __name__ == "__main__":
#     lst =[0,1,2,3,4,5,6,7,8,9]
#     game()