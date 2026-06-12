# def k(m, n):
#     x = bin(m)[2:]
#     y = bin(n)[2:]
#     ans = ''
#     while len(x) > len(y):
#         y = '0' + y
#     while len(x) < len(y):
#         x = '0' + x
#     for i in range(len(x)):
#         if x[i] == y[i]:
#             ans += x[i]
#         else:
#             ans += '0'
#     return int(ans, 2)
#
#
# def f(x):
#     return ((k(x, 52) != 0) and (k(x, 48) == 0)) <= (not(k(x, a) == 0))
# for a in range(75):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break




def f(x):
    return ((x&52 != 0) and (x&48==0)) <= (not(x&a ==0))
for a in range(75):
    if all(f(x) for x in range(1000)):
        print(a)
        break

