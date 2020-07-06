# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()


time = str(getdate())
print("Welcome to the 'Health Management System' developed by Sourav Saini:\n\n")
print("Who are you?")
print("1) Press 1 if you are Harry")
print("2) Press 2 if you are Rohan")
print("3) Press 3 if you are Hammad")
name_user = int(input())


def Harry():
    print("Welcome Harry!!\n\n")
    print("1) Enter 1 for exercise")
    print("2) Enter 2 for food\n\n")
    fitness = int(input())
    print()
    if fitness == 1:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Harry-Exercise.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Harry-Exercise.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve)")
    elif fitness == 2:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Harry-Food.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Harry-Food.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve)")


def Rohan():
    print("Welcome Rohan!!\n\n")
    print("1) Enter 1 for exercise")
    print("2) Enter 2 for food\n\n")
    fitness = int(input())
    print()
    if fitness == 1:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Rohan-Exercise.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Rohan-Exercise.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve)")
    elif fitness == 2:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Rohan-Food.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Rohan-Food.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve)")


def Hammad():
    print("Welcome Hammad!!\n\n")
    print("1) Enter 1 for exercise")
    print("2) Enter 2 for food\n\n")
    fitness = int(input())
    print()
    if fitness == 1:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Hammad-Exercise.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Hammad-Exercise.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve)")
    elif fitness == 2:
        print("What do you want to do?")
        print("1) Press 1 to Lock a new value")
        print("2) Press 2 to Retrieve a old value")
        lock_retrieve = int(input())
        if lock_retrieve == 1:
            print("Enter here:")
            with open("Hammad-Food.txt", "a") as f:
                new_value1 = input()
                f.write("\n" + str([str(time)]) + ": " + new_value1)
            print("Successfully Written!!")
        elif lock_retrieve == 2:
            with open("Hammad-Food.txt") as f:
                print(f.read())
        else:
            print("Please enter a valid input (Lock, Retrieve")


if name_user == 1:
    Harry()
elif name_user == 2:
    Rohan()
elif name_user == 3:
    Hammad()
else:
    print("Please enter valid value (Harry, Rohan, Hammad)")
