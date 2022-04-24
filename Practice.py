# def sumOfArray():
#     lst = list(map(int, input().split()))
#     print(sum(lst))


# sumOfArray()


# def largestNumber():
#     lst = list(map(int, input().split()))
#     print(max(lst))

# largestNumber()


# def arrayRotation():
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     d = 2
#     n = 7

#     lst2 = list(arr[d:])

#     lst2.extend((arr[:d]))
#     print(lst2)

# arrayRotation()


# def splitArray():
#     arr1 = [10, 2, 4, 5, 7, 8]
#     n = 2

#     lst2 = list(arr1[n:])
#     lst2.extend((arr1[:n]))
#     print(lst2)

# splitArray()


# def multiply():
#     arr = [10, 2, 4, 5, 6, 7]
#     n = 11
#     mul = 1
#     for i in arr:
#         mul = mul*i
#     print(mul)
#     print(mul//n)

# multiply()

x, y = "12"
y, z = "34"
print(x + y + z)

# str1 = "geeks"
# print(str1 == (str1[::-1]))


# str1 = "geeks for geeks coding"
# lst = list(str1.split(" "))
# print(" ".join(lst[::-1]))


# substr ="gees"
# str1 = "geeks for geeks"
# if substr in str1:
#     print("yes")
# else:
#     print("NO")


# str1 = "geeks for geeks"
# d = dict(map(str, str1))
# print(d)

# from numpy import str0


from ast import Str

from numpy import str_

# input_split = "GF is Best".split(" ")
# input_split.sort()
# count = {}
# for i in input_split:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)


# str = "This is a Python language".split(" ")
# lst = list(str)
# for i in lst:
#     if len(i)%2 == 0:
#         print(i)


# def CheckString(s):
#     s = s.lower()
#     vowels = set("aeiou")
#     for char in s:
#         if char in vowels:
#             vowels.remove(char)
#     if len(vowels) == 0:
#         print("Accepted")
#     else:
#         print("Not accepted")


# s1= "AeBIdeffoBUw"
# # print(s1)
# CheckString(s1)

# s2="geeks for geeks"
# # print(s2)
# CheckString(s2)


# str1 = "geeksforgeeks"
# print("".join(sorted(set(str1))))
# # print("".join(set(str1)))


# k = 4
# lst = []
# str1 = "Hello world is computer language code".split(" ")
# for i in str1:
#     if len(i) > k:
#         lst.append(i)
# print(" ".join(lst))


# str1 = "mama"
# str3 = str1[0]
# str2 = str1[1::]+str3
# str1 = str1[::-1]
# if str1 == str2:
#     print(1)
# else:
#     print(0)


# lst = [1,23,4,5,7,8,9,5,3]
# n=1
# print(lst[n])

# n = 5
# sum1 = str_(n**4)
# print(int(sum1[-1]) == n)


# # Contigenous characters
# s='321'
# n=len(s)
# a=0
# for i in range(n):
#     a+=int(s[i])
#     t=s[i]
#     print(t)
#     for j in range(i+1,n):
#
#         t+=s[j]
#         a+=int(t)
# print(a)


s = str(1)
print(type(s))






