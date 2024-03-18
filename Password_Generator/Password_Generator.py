import string
import random
def pass_gen():
    print('ENTER THE COMPLEXITY LEVEL OF PASSWORD-: EASY , MEDIUM or DIFFICULT')
    print("        * Easy = Alpha-numeric\n        * Medium = Numeric + Alpha-numeric\n        * Difficult = Numeric + Alpha-numeric + Special Characters")
    complexity_level  = input("Complexity :- ").lower()
    empty_list=[]
    match complexity_level:
        case "easy":
            keys = string.ascii_lowercase
            try:
                Pass_lenght = int(input("Len of Pass :- "))
                for i in range(Pass_lenght):
                    keys_collection = random.choice(keys)
                    empty_list.append(keys_collection)
                password = ''.join(empty_list)
                print("Password :- ",password)
            except :
                print("Error - Invalid Input! , Can Only Be Integer Value")
        case "medium":
            keys = string.ascii_lowercase + string.digits
            try:
                Pass_lenght = int(input("Len of Pass :- "))
                for i in range(Pass_lenght):
                    keys_collection = random.choice(keys)
                    empty_list.append(keys_collection)
                password = ''.join(empty_list)
                print("Password :- ",password)
            except :
                print("Error - Invalid Input! , Can Only Be Integer Value")
        case "difficult":
            keys = string.ascii_lowercase + string.digits + string.punctuation
            try:
                Pass_lenght = int(input("Len of Pass :- "))
                for i in range(Pass_lenght):
                    keys_collection = random.choice(keys)
                    empty_list.append(keys_collection)
                password = ''.join(empty_list)
                print("Password :- ",password)
            except :
                print("Error - Invalid Input! , Can Only Be Integer Value")
        case _ :
            print("Invalid Difficulty Level")
if __name__== '__main__':
    pass_gen()