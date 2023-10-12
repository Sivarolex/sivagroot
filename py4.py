class MyClass:
    def my_function(self):
        """Write a program that accepts sequence of lines as input 
        and prints the lines after making all characters in the sentence capitalized.
        Suppose the following input is supplied to the program:
        Hello world
        Practice makes perfect
        Then, the output should be:
        HELLO WORLD
        PRACTICE MAKES PERFECT"""
        lines=[]
        while True:
            s=input("Enter sectence: ")
            if s:
                lines.append(s.upper())
            else:
                break;
        for word in lines:
            print(word)
    
    def remove_duplicate_words(self):
        """Write a program that accepts a sequence of whitespace separated 
        words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
        Suppose the following input is supplied to the program:
        hello world and practice makes perfect and hello world again
        Then, the output should be:
        again and hello makes perfect practice world"""
        words = input("Enter the words: ")
        sentence = [word for word in words.split(' ')]
        print(" ".join(sorted(list(set(sentence)))))

if __name__ == "__main__":
    my_instance = MyClass()
    my_instance.my_function()
    my_instance.remove_duplicate_words()