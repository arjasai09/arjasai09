# def remove(lst):
#     val = 3
#     if len(lst) == 0:
#         return 1

#     else:
#         for i in lst:
#             if i == val:
#                 print(i)
#                 lst.remove(i)
#     # return lst
#     print(lst)


#     k = len(lst)

#     print(k)

# remove([3,2,2,3,])




# def mySqrt(x):
   
#     x //= 2
#     if x == 2:
#         return 2
#     else:
        # return mySqrt(x)
    

# print(mySqrt(2))






# def searchInsert(nums, target):
#         mid = len(nums)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             mid = mid + 1
#         elif nums[mid] > target:
#             mid = mid - 1
#         nums.append(target)
#         nums.sort()
#         return nums.index(target)
            


# print(searchInsert([1,3,5,6], 1))




"""
var xml = parseXml("<foo>Stuff</foo>");
alert(xml.documentElement.nodeName);
"""
#
# a = "13"
# f  = ""
# try:
#     a = int(a)
#     if isinstance(a, int):
#         print(type(a))
# except:
#     f = "Failure"
#
#
# if f == "Failure":
#     print(f)
# else:
#     print(a)
#






x = 10
print(x + 10)

x += 10
print(x)

lst = [0]*1
lst[0] += x

x = hex(16)

print(f"oct value for 16 decimal: {oct(16)}")
print("{} binary value for 16 decimal".format(bin(16)))
print( "hexa decimal value for 16 decimal", x)

x = 1
y = 1

print(x if x | y else y)

print(x >> 2)

import datetime
from datetime import date
import time
 
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time()) 
print(date(2022, 6, 3))
print(date.fromtimestamp(100008000))

print(datetime.datetime.today())
# print(datetime.timedelta(days=7))
# print(datetime.datetime.strptime("2012, August, 8", "%Y, %m, %d"))




x=10
y=8
assert x>y, 'X too small'



for i in [1,2,3,4][::-1]:
        print(i)



print('*', "abcde".center(6), '*', sep='')
