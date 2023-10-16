"""Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010"""
class example():
    def binary_5_division(self):
        binary_number = [x for x in input("Enter four digit binary numbers: ").split(',')]
        li = []
        for i in binary_number:
            intp = int(i, 2)
            if not intp%5:
                li.append(i)

        print(','.join(li))



    def evennumbers_betweenrange(self):
        values = []
        for i in range(1000, 3001):
            s = str(i)
            if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
                values.append(s)
        print(",".join(values))


if "__name__" == "__main__":
    my_instance = example()
    my_instance.binary_5_division()
    my_instance.evennumbers_betweenrange()
