def my_practise():
    
    """Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24

    Hints:
    If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
    In case of input data being supplied to the question, it should be assumed to be a console input."""
    import math
    c=50
    h=30
    output=[]
    #inputs = [10,20,30]
    values=[x for x in input("Enter the values: ").split(',')]
    for d in values:
        output.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    print (','.join(output))


    """Write a program that accepts a comma separated sequence of words as input 
    and prints the words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world

    Hints:
    In case of input data being supplied to the question, it should be assumed to be a console input."""

    words = []
    inputs=[x for x in input("Enter names: ").split(',')]
    inputs.sort()
    print(','.join(words))

if __name__ == "__main__":
    my_practise()