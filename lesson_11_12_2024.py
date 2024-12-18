# def mul_num(a,b):
#     if a > b:
#         a,b = b,a
#     res = 1
#     for i in range(a,b+1):
#         res *= i
#         return res
#
#
# a = 5
# b = 25
# print(mul_num(a,b))

# def get_perim(a,b):
#     return 2 * (a,b)
#
#
# a = 2
# b = 7
# print(get_perim(a,b))


# def isnum(a: int,st: str) -> bool:
#     if str(a) in st:
#         return True
#     else:
#         return False
#
#
# a = 5
# st = "Hello"
# print(isnum(a,st))


# def sum_num(a, *args):
#     return sum(args)
#
#
# print(sum_num(2,15))
# from random import randint
#
# def get_sum_list(lst):
#     s = 0
#     for i in lst:
#         s+=i
#     return s
#
#
# lst = [randint(1,10) for i in range(5)]
# print(get_sum_list(lst))

# def func(a,lst=[]):
#     lst.append(a)
#     return lst
#
#
# print(func(2))
# print(func(5))
from random import randint
#
# def useless(*lst):
#
#     for i in lst:
#         if not i % 2:
#             res['even']
#
# lst = [randint(-10,10)for _ in range(5)]
# useless(lst)


def num_f(a,b):
    if b in a:
        count = 0
        for i in a:
            if b == i:
                count +=1
        print(True,count)
    else:
        return False


a =[1,23,5,5,67,456,2]
print(a)
b = 5
print(num_f(a,b))