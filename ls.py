# a = input("in")
# count_l , count_n = 0 , 0
# for i in range(0, len(a)):
#     if a[i].isalpha():
#         count_l +=1
#     if a[i].isnumeric():
#         count_n += 1
# print(f"letters{count_l}, num{count_n}")
# print(len(a))


# a = input("in")
# count_l , count_n = 0 , 0
# for let in range(0, len(a)):
#     if a[let].isalpha():
#         count_l +=1
#     if a[let].isnumeric():
#         count_n += 1
# print(f"letters{count_l}, num{count_n}")
# print(len(a))

# a = input()
# print(a.count("із"))

# a = input()
# b = input()
# c = input()
#
# print(a.replace(b,c))

# a = "А буду я у дуба"
#
# b = a[::-1].replace(" ","").lower()
# if a.replace(" ","").lower() == b:
#     print("t")
# else:
#     print("f")

a = "https://pythoncod.club/stroki-v-python-i-metody-raboty/gfpihk'gbjujnpo"
b = a.find("/")
c = a.find("/")
print(a.find("/",b+1))
temp = a[a.find("/",b+1)+1:]
print(temp[:temp.find("/")])