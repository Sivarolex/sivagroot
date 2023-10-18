"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""
class DigitLetterCount():
    def digits_letters_count(self):
        sentence = input("Enter Sentence: ")
        dic = {"Letters":0,"Digits":0,"Upper":0,"Lower":0}

        for character in sentence:
            if character.isdigit():
                dic["Digits"] += 1
            elif character.isalpha():
                dic["Letters"] += 1
            else:
                pass
        for character in sentence:
            if character.isupper():
                dic["Upper"] += 1
            elif character.islower():
                dic["Lower"] += 1
            else:
                pass
            
        print("No of Letters are: ",dic["Letters"])
        print("No of Digits are: ",dic["Digits"])
        print("No of Upper Letters are: ",dic["Upper"])
        print("No of Lower Letters are: ",dic["Lower"])

if "__name__" == "__main__":
    my_class = DigitLetterCount()
    my_class.digits_letters_count()