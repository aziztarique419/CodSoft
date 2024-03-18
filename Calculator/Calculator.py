print('Welcome To Simple Calculator for Basic Operations')
print("-------------------------------------------------")
def calculator():
    first_val= input("Enter first number :- ")
    print("Choose an operation +,-,*,/")
    operation = input()
    second_val= input("Enter second number :- ")
    try:
        match operation :
            case "+":
                print(float(first_val)+float(second_val))
            case "-":
                print(float(first_val)-float(second_val))

            case "/":
                print(float(first_val)/float(second_val))
            case "*":
                print(float(first_val)*float(second_val))
            case _ :
                print("Error, Please Enter A Right Operation")
    except :
        print('Error - Wrong Value Entered')
if __name__ == "__main__":
    while True:
        calculator()
        print('For Another Calculation Type "Reset" & For Stop Calculatioin Type "Finish".')
        resume_or_exit = input().capitalize()
        if resume_or_exit == 'Reset':
            continue
        elif resume_or_exit == 'Finish':
            print('Thank you For Using This Calculator')
            break
        else:
            print('Entered an invalid Choice ,Thank You ')
            break