# size = 10
# coice_user = input("a b c")
# if coice_user == "a":
#      for i in range(size):
#          for j in range(size):
#              if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i ==j or i < j :
#                  print("*", end="")
#              else:
#                  print(" ", end="")
#          print()
# elif coice_user == "b":
#      for i in range(size):
#          for j in range(size):
#              if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i ==j or j < i :
#                  print("*", end="")
#              else:
#                  print(" ", end="")
#          print()
#
# size = 3
# for k in range(size):
#     for i in range(9):
#         if i % 2 == 0:
#             for j in range(size):
#                 print('*', end='')
#         elif i % 2 == 1:
#             for j in range(size):
#                 print('_', end='')
#     print()
#     for i in range(9):
#             if i % 2 == 0:
#                 for j in range(size):
#                     print('_', end='')
#             elif i % 2 == 1:
#                 for j in range(size):
#                     print('*', end='')
#     print()


# size = 3
# for k in range(size):
#     for i in range(size * 2):
#         if i % 2 == 0:
#             for j in range(size):
#                 print('*', end='')
#         elif i % 2 == 1:
#             for j in range(size):
#                 print('_', end='')
#     print()
#     for i in range(size * 2):
#             if i % 2 == 0:
#                 for j in range(size):
#                     print('_', end='')
#             elif i % 2 == 1:
#                 for j in range(size):
#                     print('*', end='')
#     print()

# from random import randint
# level = input("level ")
#
# if level == "1":
#     temp = 0
#     for i in range(5):
#         a = randint(1,10)
#         b = randint(1,10)
#         print(f"{a} {b}")
#         res = int(input('Result '))
#         if a * b == res:
#            print("yes")
#            temp += 1
#         else:
#             print("no")
#     print(f"grade{round(12*temp/5 ,0)}")
# elif level == "2":
#     temp = 0
#     for i in range(10):
#         a = randint(1,10)
#         b = randint(1,10)
#         print(f"{a} {b}")
#         res = int(input('Result '))
#         if a * b == res:
#            print("ok")
#            temp += 1
#         else:
#             print("no")
#     print(f"grade{round(12*temp/10 ,0)}")
# elif level == "3":
#     temp = 0
#     for i in range(15):
#         a = randint(1,10)
#         b = randint(1,10)
#         print(f"{a} {b}")
#         res = int(input('Result '))
#         if a * b == res:
#            print("Yes")
#            temp += 1
#         else:
#             print("no")
#     print(f"grade{round(12 * temp / 15, 0)}")

# a = int(input("A "))
# b = int(input("B "))
# flag = 0
# for i in range(2,a+1, 1):
#     if a % i == 0 and b % i == 0 :
#         print(f"NSD {i}")
#         flag += 1
#         break
# if flag == 0:
#     print(1)


# b = int(input("6 "))
#
# for i in range(b):
#     print(i, end=" ")
#     for j in range(1, i + 1):
#         if i == 0 or i == b - 1 or j == 0 or j == b - 1 or i == j or i > j:
#             print()
#             break
#         elif


# size = int(input("6 "))
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or i > j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

a = int(input("A "))
for i in range(a):
    for j in range(i + 1):
        print((i + 1) * (i + 1), end=" ")
    print()
