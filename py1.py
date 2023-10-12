a=[x*x for x in range(1,11)]
b=[2**y for y in range(1,6)]
c=[x for x in a if x%2 == 0]
print(a)
print(b)
print(c)

words = "the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)


vowels = ['a','e','i','o','u']
word = "akbnriqahohnfbjaerqjfkbzvbjhblaraelrtafufagrf"
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(found)
print("num of vowels found in",word,"is",len(found))