print("hello")


def selectionSort(lst):
    for i in range(len(lst) - 1):
        mid = i
        for j in range(i + 1, len(lst)):
            if lst[mid] >= lst[j]:
                mid = j
        lst[i], lst[mid] = lst[mid], lst[i]
    return f"Selection Sort: {lst}"


print(selectionSort([8, 5, 6, 3, 4, 1]))


def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] >= lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return f"Bubble Sort: {lst}"


print(bubbleSort([8, 5, 6, 3, 4, 1]))


def insertionSort(lst):
    for i in range(len(lst)):
        key = lst[i]

        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]

            j = j - 1
        lst[j + 1] = key
    return f"Insertion Sort: {lst}"


print(insertionSort([8, 5, 6, 3, 4, 1]))


def anagram(str1, str2):
    if len(str1) != len(str2):
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return 0
    return 1


print(anagram("act", "tak"))


def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10  # 121%10 = 1
        rev = rev * 10 + dig  # 1  # 10+2 = 12 #
        n = n // 10

    return temp == rev


print(palindrome(131))


def reverse(n):
    temp = 0

    while n > 0:
        dig = n % 10
        temp = temp * 10 + dig
        n = n // 10

    return temp


print(reverse(512))


# create function sumOddEven with parameter lst is a array
def sumOddEven(lst):
    tempOdd = 0
    tempEven = 0

    for i in lst:
        if i % 2 == 0:
            tempEven += i
        else:
            tempOdd += i

    return tempOdd, tempEven


print(sumOddEven([1, 2, 3, 4, 5, 6, 7]))

import math
from typing import OrderedDict


def power():
    return func(10, 5)


def func(i, e):
    return math.pow(i, e), math.lcm(i, e), math.gcd(i, e)


print(power())

# def secondLargestElement(lst):
#     start = 0
#     end = len(lst)-1                     # 5-1 = 4
#     while (start<=end):                    # 0 <= 4
#         mid = (start + end)//2           # 0+4//2 = 2
#         # lst[2-1] < lst[2] and lst[2] > lst[2+1]
#         if lst[mid-1] < lst[mid] and lst[mid] > lst[mid+1]: 
#             return lst[mid]

#         if lst[mid-1] < lst[mid] and lst[mid] < lst[mid+1]:
#             start =  mid+1

#         else:
#             end = mid - 1


# print(secondLargestElement([2,4,1,3,5]))


queue = []


def enque(elem):
    return queue.append(elem)


def dequeue():
    if not queue:
        return "queue is empty"
    else:
        return queue.pop(0)


def display():
    return queue


enque(2)
enque(3)
enque(4)
print(display())

# print(dequeue())
dequeue()
# dequeue()
# dequeue()
print(display())

a = "sai vamsi"

print("".join(a[4:]) + " " + "".join(a[:4]))
# str1 = a + b
# a = str1[:3]
# b = str1[3:]

# print(a)


s = "@n a^pple i( a basket"
arr = s.split(" ")
print(arr)
char = "[{(!@#$%^&*)}]"
count = 0
for word in arr:
    if not word.isalnum() and word[1] in char:
        count = count + 1
print(count)


# def decimalToBinary(n):
#     remstack = []

#     while n > 0:
#         rem = n % 2
#         remstack.append(rem)
#         n = n // 2

#     binstring = ""
#     while remstack != []:
#         binstring = binstring + str(remstack.pop())

#     return binstring


# print(decimalToBinary(42))

# def basConverter(n, base):
#     digits = "0123456789ABCDEF"

#     remstack = []

#     while n > 0:
#         rem = n % base
#         remstack.append(rem)
#         n = n // base

#     newString = ""
#     while remstack != []:
#         newString = newString + digits[remstack.pop()]

#     return newString


# print(basConverter(25, 2))
# print(basConverter(25, 16))


# def longestSubArray(n):
#     lst = [int(i) for i in (input()).split()]
#     odd = 0
#     even = 0
#     print(lst)
#     for j in lst:
#         if j == 1:
#             odd += 1
#         even += 1

#     if odd > even:
#         return 2*even
#     return 2*odd


# print(longestSubArray(5))


# # from pythonds.basic import Queue

# import random

# class Printer:
#     def __init__(self, ppm):
#         self.pagerate = ppm
#         self.currentTask = None
#         self.timeRemaining = 0

#     def tick(self):
#         if self.currentTask != None:
#             self.timeRemaining = self.timeRemaining - 1
#             if self.timeRemaining <= 0:
#                 self.currentTask = None

#     def busy(self):
#         if self.currentTask != None:
#             return True
#         else:
#             return False

#     def startNext(self,newtask):
#         self.currentTask = newtask
#         self.timeRemaining = newtask.getPages() * 60/self.pagerate

# class Task:
#     def __init__(self,time):
#         self.timestamp = time
#         self.pages = random.randrange(1,21)

#     def getStamp(self):
#         return self.timestamp

#     def getPages(self):
#         return self.pages

#     def waitTime(self, currenttime):
#         return currenttime - self.timestamp


# def simulation(numSeconds, pagesPerMinute):

#     labprinter = Printer(pagesPerMinute)
#     printQueue = Queue()
#     waitingtimes = []

#     for currentSecond in range(numSeconds):

#       if newPrintTask():
#          task = Task(currentSecond)
#          printQueue.enqueue(task)

#       if (not labprinter.busy()) and (not printQueue.isEmpty()):
#         nexttask = printQueue.dequeue()
#         waitingtimes.append( nexttask.waitTime(currentSecond))
#         labprinter.startNext(nexttask)

#       labprinter.tick()

#     averageWait=sum(waitingtimes)/len(waitingtimes)
#     print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

# def newPrintTask():
#     num = random.randrange(1,181)
#     if num == 180:
#         return True
#     else:
#         return False

# for i in range(10):
#     simulation(3600,5)


# class Deque:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def addFront(self, item):
#         self.items.append(item)

#     def addRear(self, item):
#         self.items.insert(0,item)

#     def removeFront(self):
#         return self.items.pop()

#     def removeRear(self):
#         return self.items.pop(0)

#     def size(self):
#         return len(self.items)


# def boolena():
#     interested = True

#     if not interested:
#         return 1
#     return 0

# print(boolena())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def __repr__(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNxt):
        self.next = newNxt


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def __repr__(self) -> str:
        lst = []
        current = self.head

        while current:
            if current is self.head:
                lst.append(current.getData())
            elif current.next is None:
                lst.append(current.getData())
            else:
                lst.append(current.getData())

        current = current.getNext()

        return '--->'.join(lst)

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


myList = UnorderedList()

myList.add(12)
myList.add(23)
myList.add(13)
myList.add(4)
# myList.add(2)



# print(mylist.size())
# print(mylist.search(22))
# mylist.remove(13)
# print(mylist.size())


# Ordered List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return self.next
#
#     def setData(self, newdata):
#         self.data = newdata
#
#     def setNext(self, newnxt):
#         self.next = newnxt

#
# class Orderedlist:
#     def __init__(self):
#         self.head = None
#
#     def isEmpty(self):
#         return self.head == None
#
#     def size(self):
#         count = 0
#         current = self.head
#
#         while current != None:
#             count = count + 1
#             current = current.getNext()
#
#         return count
#
#     def search(self, item):
#         current = self.head
#         found = False
#         stop = False
#
#         while current != None and not found and not stop:
#             if current.getData() == item:
#                 found = True
#
#             else:
#                 if current.getData() > item:
#                     stop = True
#                 else:
#                     current = current.getNext()
#
#         return found
#
#     def add(self, item):
#         li = []
#         current = self.head
#         previous = None
#         stop = False
#         while current != None and not stop:
#             if current.getData() > item:
#                 stop = True
#             else:
#                 previous = current
#                 current = current.getNext()
#
#         temp = Node(item)
#         if previous == None:
#             temp.setNext(self.head)
#             self.head = temp
#         else:
#             temp.setNext(current)
#             previous.setNext(temp)
#
#
# mylst = Orderedlist()
#
# mylst.add(12)
# mylst.add(34)
# mylst.add(45)
# mylst.add(54)
# mylst.add(34)
# print(mylst.search(34))
#
# print(mylst.size())
