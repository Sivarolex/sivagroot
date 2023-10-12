"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""

l=[]
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (','.join(l))

"""factorial of a number"""

def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
x=int(input("Enter a number to check factorial: "))
print (fact(x))


"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

d=dict()
x = int(input("Enter a Number: "))
for i in range(1,x+1):
    d[i] = i*i
print (d)


