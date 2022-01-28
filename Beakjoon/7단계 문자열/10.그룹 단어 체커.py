n = int(input())

for i in range(n):
    word = input()
    # print(type(word))
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j] in word[j+2:]:
                n -= 1
                break


print(n)

# n = int(input())
# # # cnt = 0
# #
# for i in range(n):
#     word = input()
#     cnt = 0
#     ln = []
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             cnt += 1
#             pass
#             temp1 = word[j]
#             temp2 = word[j+1]
#             ln.append(word[j])
#             ln.append(word[j+1])
#             print(ln)
#             print(j)
#             for k in word:
#                 if temp1 == k:
#                     # cnt -= 1
#                     n -= 1
#                 if temp2 == k:
#                     n -= 1
#                 # if temp1 == k or temp2 == k:
#             if word[j] in word[j+2:] or word[j+1] in word[j+2:]:
#                 n -= 1
#
#
#
#         elif word[j] == word[j+1]:
#             temp3 = word[j]
#             # print(temp)
#             # cnt += 1
#             # n += 1
#             for h in word[j+2:]:
#                 if temp3 == h:
#                     n -= 1
#                     # cnt -= 1
#             break
# print(cnt)
# # print(n)
# #
# # a = 'happy'
# # print(a[0])
# # for i in range(len(a)-1):
# #     if a[i] == a[i+1]:
# #         print(i)
#
#
# # a = 'happy'
# # print(len(a))
# #
# # for i in a[2:]:
# #     print(i)