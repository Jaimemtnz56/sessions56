name = input("What is your name?")
print("Hello", name)
age = input("How old are you?")
try:
    #Another way to format the print is via f-strings (to be taught in future sessions)
    print(f"{name}, you were born in {2024-int(age)}")
#  division = int(age) / 0
except ValueError:
    print("Age must be a valid number")
    print(f"The value that you typed was {age}")
except ZeroDivisionError:
    print("You can't divide by 0")
except: #all the other errors
    print("No idea what else can go wrong, but just in case")
else: #in case no exception happened
    print("Thanks for being a good sport and not trying to crash the program")
finally: # this runs in the end no matter what
    print("Thanks for playing")