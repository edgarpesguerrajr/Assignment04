def FirstGroup():
    Name1 = input('Enter your name: ')
    Age1 = int(input('Enter your age: '))
    Address1 = input('Enter your address: ')
    return Name1, Age1, Address1

def FinalOutput(Name2, Age2, Address2):
    print (f'Hi, my name is {Name2}. I am {Age2} years old and I live in {Address2}.')

Name, Age, Address = FirstGroup()
FinalOutput(Name, Age, Address)