#8
# mylist = [1, 2, 5, 6]
# ans = 0
# c = 0
# for i in range(1, 4):
#     for x in mylist:
#         if x % i == 0:
#             ans += x
#             c += 1
# print(ans, c)

#10
# def even(n):
#     s = 0.0
#     for i in range(2, n + 1, 2):
#         s += 1.0 / i
#     return s
#
#
# def odd(n):
#     s = 0.0
#     for i in range(1,n+1,2):
#         s += 1.0 / i
#     return s
#
#
# n = int(input("请输入一个正整数n："))
# if n%2==0:
#     sum = even(n)
# else:
#     sum = odd(n)
# print(sum)