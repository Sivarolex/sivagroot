# Email Validation
import re
class EmailValidation():
    def email_validation(self):
        email = input("Enter Your Email: ")

        email_pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]'
        if re.match(email_pattern,email):
            print("Entered Email is correct.")
        else:
            print("Re-Enter Email.")

if "__name__" == "__main__":
    my_class=EmailValidation()
    my_class.email_validation()