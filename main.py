def askQuestion():
    x = int(input("Give me a number between 1 and 10: ")) # it's asking for x
    if x >= 1 and x <= 10:
        print(f"Thank you for giving me {x}")
    else:
        print("No, that is not between 1 and 10")
        askQuestion()

# Begin
askQuestion()