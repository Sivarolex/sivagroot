# words frequency
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
result = {key: test_str.count(key) for key in test_str.split()}

print("The words frequency : " + str(result))


#using List and Set Comprehension

# Split the string into a list of words
listString = test_str.split()

# Using set() and list comprehension to count the frequency of each word
freq = {word: listString.count(word) for word in set(listString)}
 
# Printing result
print("The words frequency : " + str(freq))