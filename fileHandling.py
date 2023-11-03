import os


"""Read a text file and count the number of lines"""

#def count_lines(programs):
# with open("/home/devi/Desktop/sivafile.docx",'r') as file:
#     # lines = file.readlines()
#     # print(len(lines))
#     for line in file:
#         print(line)

# if os.path.exists("/home/devi/Desktop/sivafile.docx"):
#     with open("/home/devi/Desktop/sivafile.docx","r") as file:
#         data = file.read()
# else:
#     print("File not Exist")


file = open("sivafile.docx", "w")  # Opens the file for writing
file.write("Hello, World!")