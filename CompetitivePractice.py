def validParenthesis():
    str1 = "[[]][]"
    counter = 0
    for i in str1:
        if i == "[":
            counter += 1
        else:
            counter -= 1

        if counter < 0:
            return False
    return True

print(validParenthesis())

def multipleParenthesis(str2):
    st = []
    m =  {"[":"]", "{":"}", "(":")"}
    for el in str2:
        if el in m:
            st.append(el)
        else:
            if len(st) == 0:
                return 0
            elif m[st[-1]] == el:
                st.pop()
            else:
                return 0
    return 1 if len(st)==0 else 0

print(multipleParenthesis("[]{"))



def removeDuplicates(s):
    st = []
    for el in s:
        if len(st) == 0 or st[-1] != el:
            st.append(el)
        else:
            st.pop()
    return "".join(st)


print(removeDuplicates("awwxz"))


a = [1,2,3,4]
b = [3,4,5,6]

c =  [x for x in a if x not in b]
print(c)




a = {"Hello" : "World", "First" : 1}
b = { val :k for k, val in a.items()}

print(b)

print(len(["hello",2,3,4]))


def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return "No"
    return "Yes"

n = 4
print(isPrime(n))





# Python program to check if the number is an Armstrong number or not

# take input from the user
num = 23

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print("Yes")
else:
   print("No")




x = "abcab"
y = "aabab"


for A, B in zip(x,y):
    if A != B:
        c = 1

print(c)
