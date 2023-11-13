def commonfun(str1,str2):
    return(len((set(str1)).intersection(set(str2))))
 
#string1=input("Enter String 1 : ")
string1="VISHAV"
string2="VANSHIKA"
#string2=input("Enter String 2 : ")
 
no_of_common_character=commonfun(string1.lower(),string2.lower())
 
print("NO. OF COMMON CHRACTERS ARE : ",no_of_common_character)


# Using Dictionary

def count(str1, str2):
    common_dict={}
    for i in str1:
        if i in common_dict:
            common_dict[i]+=1
        else:
            common_dict[i]=1

    counter = 0

    for i in str2:
        if i in common_dict and common_dict[i] > 0:
            counter += 1
            common_dict[i] -= 1
    print("No. of matching characters are: " + str(counter))

if __name__ == "__main__":
    # Define two strings to compare.
    str1 = 'aabcddekll12@'
    str2 = 'bb2211@55k'
 
    # Call the count function with the two strings.
    count(str1, str2)