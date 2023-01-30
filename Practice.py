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

# x, y = "12"
# y, z = "34"
# print(x + y + z)

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


# from ast import Str
#
# from numpy import str_

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


def insertionSort():
    lst = [2, 1, 5, 3, 6, 4, 9, 8]

    for i in range(0, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = temp
    return f"Insertion Sort: {lst}"


print(insertionSort())

print(ord('A'))
print(chr(97))


def selectionSort():
    lst = [4, 2, 5, 1, 8, 7]
    for i in range(0, len(lst) - 1):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        if min != i:
            lst[min], lst[i] = lst[i], lst[min]

    return f"Selection Sort: {lst}"

print(selectionSort())


# def mergeSort(lst, l ,r):
#     if (l<r):
#         m = (l+r)//2
#         mergeSort(lst, l, m)
#         mergeSort(lst, m+1, r)
#         merge(lst, l, m, r)

# def merge(lst, l, m, r):
#     i = l
#     k = l
#     j = m+1
#     temp = []
#     while(i<=m and j<=r):
#         if lst[i] < lst[j]:
#             lst[k] = lst[i]
#             i = i+1
            
#         else:
#             lst[k] = lst[j]
#             j = j+1
#         k = k+1
#     while(i<=m):
#         lst[k] = lst[i]
#         i = i+1
#         k = k+1

#     while(j <= r):
#         lst[k] = lst[j]
#         j = j+1
#         k = k+1
#     # for i in temp:
#     #     lst.append(i)
#     # print(f"MergeSort: {lst1}")
#     print(lst)

# lst = [5,3,6,1,7,2,8]
# n = len(lst) - 1
# mergeSort(lst, 0, n)

# lst = [5,3,6,1,7,2,8]
# lst.sort()
# print(lst[0] + lst[-1])





# def mergeSort(lst):
#     l = 0
#     r = len(lst)-1
#     if l < r:
#         mid = (l+r)//2
#         left = lst[:mid]
#         right = lst[mid+1:]

#         mergeSort(left)
#         mergeSort(right)

#         merge(left, right, lst)

# def merge(a, b, lst):
#     len_a = len(a)
#     len_b = len(b)
#     i = 0
#     j = 0
#     k = 0
#     temp = []
#     while i < len_a and j < len_b:
#         if a[i] < a[j]:
#             temp[k] = a[i]
#             i = i + 1
#         else:
#             temp[k] = b[j]
#             j = j + 1
#         k = k + 1

#     while i < len_a:
#         temp[k] = a[i]
#         i = i + 1
#         k = k + 1
#     while j < len_b:
#         temp[k] = b[j]
#         j = j + 1
#         k = k + 1

#     print(lst)


# def merge_sort(original_list):
#     if len(original_list) <= 1:
#         return original_list

#     half_index = len(original_list) // 2
#     left = merge_sort(original_list[:half_index])
#     right = merge_sort(original_list[half_index:])

#     i = j = 0

#     merged_list = []

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged_list.append(left[i])
#             i += 1
#         else :
#             merged_list.append(right[j])
#             j += 1

#     while i < len(left):
#         merged_list.append(left[i])
#         i += 1

#     while j < len(right):
#         merged_list.append(right[j])
#         j += 1
        

#     return merged_list


    



# print(merge_sort([3,6,5,2,8,1]))



def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        mergeSort(left)
        mergeSort(right)

        lft = rgt = k = 0

        while lft < len(left) and rgt < len(right):
            if left[lft] < right[rgt]: 
                lst[k] = left[lft]
                lft += 1
            else:
                lst[k] = right[rgt]   
                rgt += 1
            k += 1
        while lft < len(left):
            lst[k] = left[lft]
            lft += 1
            k += 1
        while rgt < len(right):
            lst[k] = right[rgt]
            rgt += 1
            k += 1

    return f"Merge Sort: {lst}" 

print(mergeSort([5,4,6,2,3, 1,8]))







































