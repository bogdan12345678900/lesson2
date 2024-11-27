# a = [[1,2,3],[4,5,6],[7,8,9]]
# count = 0
# suma = 0
# for i in a:
#     for j in i:
#         suma +=1
#         count +=1
# print(suma/count)

# a = [[1,2,3],[4,5,6],[7,8,9]]
# res = list(zip(*a))
# print(res)

# tpl = ()
# print(type(tpl))
#
# lst = [1,2,3]
# lst[2] = 30
# print(lst)
#
# tpl = (1,2,30)
# tpl[2] = 30
# print(len(tpl))
# print(tpl.count(3))
# print(tpl.index(2))

# stud = dict()
# stud ={}
# print(stud)
# print(type(stud))
# stud ={"name":"Oleg"}
# print(len(stud))
#
# print(stud["name"])
# s = "qw"
# print(id(s))
# s = "qwe"
# print(id(s))


# s = []
# print(id(s))
# s = [1,2,3]
# print(id(s))
#
#
# s = "qw"
# b = "qw"
# lst = [None,None]
# print(id(lst[0]),id(lst[1]))

# stud ={"name":"Oleg","age":16}
# stud["phone"] = "+380668947129"
# print(stud.keys())
# print(list(stud.keys()))
# print(stud.values())
# print(stud.items())
# print(stud.pop("phone"))
# print(stud.popitem())
# print(stud.get("phone"))
# print(stud)
# stud.update({"phone":"+380668947129"})
# print(stud)

# flag = True
# mass = [1,2,3,4,1,2,5,6,1]
# for i in range(len(mass)):
#     for j in range(i+1 , len(mass)):
#         if mass[i] == mass[j] :
#             print(False)
#             break
#     if not flag:
#         break
# else:
#     print(True)


import requests
url = "https://api.openweathermap.org/data/2.5/weather?"
city = input("City: ")
API = "b22d0ddb2956385d16120b6d7a502fe0"
params = {'q':city , "units":"metric","appid":API}
resp = requests.get(url=url,params=params)
if resp.status_code == 200:
    data = resp.json()
    temperatura = data["main"]["temp"]
    print(data["weather"][0]["icon"])
print(temperatura)
