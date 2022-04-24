def binarySerch():
    lst = [1, 2, 3, 4, 5]
    target = 4

    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2

        if lst[mid] == target:
            return f"index position of target: {mid}"
        elif lst[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None


# print(binarySerch())

def recursiveBinarySearch(lst, target):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == target:
            return True
        else:
            if lst[mid] < target:
                return recursiveBinarySearch(lst[mid + 1:], target)
            else:
                return recursiveBinarySearch(lst[:mid], target)


lst = [1, 2, 3, 4, 5]
target = 4
print(recursiveBinarySearch(lst, target))

n = 5
sum1 = (n * (n + 1) * (2 * n + 1)) // 6
print(sum1)










def jumpOperations(lst):

    n = len(lst)
    reachable = 0

    for i in range(n):
        if reachable < i:
            return False
        reachable = max(reachable, i+lst[i])

    return True

print(jumpOperations([1,0,3,4,5]))


def countJumps(lst, n):
    maxR = step = lst[0]
    jump = 1

    if n==1:
        return 0
    elif lst[0] == 0:
        return -1

    else:
        for i in range(n):
            if i == n-1:
                return jump

            maxR = max(maxR, i+lst[i])
            step = step - 1

            if step == 0:
                jump += 1
                if i >= maxR: return -1
                step = maxR - 1

                
print(countJumps([1,2,3,4,5], 5))













