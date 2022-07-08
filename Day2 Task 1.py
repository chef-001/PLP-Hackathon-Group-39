#Day 2 Task One
Num_books = input("Enter number of books you have purchased this month: ")

if Num_books == 0:
    print("You have 0 points.")
elif Num_books == 1:
    print("You have 6 points.")
elif Num_books == 2:
    print("You have 16 points.")
if Num_books == 3:
    print("You have 32 points.")
else:
    print("You have 60 points.")