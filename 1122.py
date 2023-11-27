# fib_list = [0, 1]
# total = 0
# i = 0
# for times in range(20):
#     total = fib_list[i] + fib_list[i + 1]
#     fib_list.append(total)
#     i += 1
# print(fib_list)

a = [1,2,3,4,5,6,1,2,3,4,6,7]
for i, n in enumerate(a[:-1]):
    print(n, a[i+1])
    if n > a[i+1]:
        a[i], a[i+1] = a[i+1], n
    print(a)

# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
b = list(enumerate(a))
a[0], a[1] = a[1], a[0]
print(a, b)