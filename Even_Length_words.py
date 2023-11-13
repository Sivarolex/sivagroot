sentence = "i am groot"

result = sentence.split(" ")

for i in result:
    if len(i)%2==0:
        print(i)

# Using lamda function
l = list(filter(lambda x: (len(x)%2==0),result))
print(l)

# Using List Comprehension

print([x for x in result if len(x)%2==0])