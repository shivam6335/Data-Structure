# 28-08
for i in range(int(input())):
    length,target = list(map(int,input().split()))
    l = [int(i) for i in input().split()]
    k=j=flag=None
    print(l)
    i = len(l)-1
    while i>=0:
        k=0
        j=0+i
        while j>len(l):
            if sum(l[k:j+1]) == target:
                flag=1
                break
            k+=1
            j+=1
        if flag:
            break
    if flag:
        print(k+1,j+1)
    else:
        print(-1)
#
# # 28-08
#
# for i in range(int(input())):
#     length,target = list(map(int,input().split()))
#     l = [int(i) for i in input().split()]
#     k=j=flag=None
#     print(l)
#     for i in range(len(l)):
#         k=0
#         j=0+i
#         while j<len(l):
#             if sum(l[k:j+1]) == target:
#                 flag=1
#                 break
#             k+=1
#             j+=1
#         if flag:
#             break
#     if flag:
#         print(k+1,j+1)
#     else:
#         print(-1)