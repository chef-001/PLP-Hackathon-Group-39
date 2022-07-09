import random

career_question=['Do you love teaching? ','Are you good with debate? ','Do you love business and mathematics? ','Do you love saving lives?']
career_options=['Accountant', 'Doctor','Lawyer','Teacher']
career_advice=["Success doesn't come easily.", 'Never stop learning.', 'Speak up and focus on results.', 'Challenge yourself and believe.']

random_question = random.choice(career_question)

if random_question == career_question[0]:
    print(random_question)
    answer = input("Yes or No: ").lower()
    if answer == "yes":
        print(f"Your should consider venturing into {career_options[3]} career.")
        print(f"Here is some career advice: {random.choice(career_advice)}\n")
    elif answer == "no":
        print(career_question[2])
        answer = input("Yes or No: ")
    else:
        print("Invalid response.")
        print(random_question)
        answer = input("Yes or No: ")

elif random_question == career_question[1]:
    print(random_question)
    answer = input("Yes or No: ").lower()
    if answer == "yes":
        print(f"Your should consider venturing into {career_options[2]} career.")
        print(f"Here is some career advice: {random.choice(career_advice)}\n")
    elif answer == "no":
        print(career_question[2])
        answer = input("Yes or No: ")
    else:
        print("Invalid response.")
        print(random_question)
        answer = input("Yes or No: ")

elif random_question == career_question[2]:
    print(random_question)
    answer = input("Yes or No: ").lower()
    if answer == "yes":
        print(f"Your should consider venturing into {career_options[0]} career.")
        print(f"Here is some career advice: {random.choice(career_advice)}\n")
    elif answer == "no":
        print(career_question[0])
        answer = input("Yes or No: ")
    else:
        print("Invalid response.")
        print(random_question)
        answer = input("Yes or No: ")

elif random_question == career_question[3]:
    print(career_question)
    answer = input("Yes or No: ").lower()
    if answer == "yes":
        print(f"Your should consider venturing into {career_options[1]} career.")
        print(f"Here is some career advice: {random.choice(career_advice)}\n")
    elif answer == "no":
        print(career_question[1])
        answer = input("Yes or No: ")
    else:
        print("Invalid response.")
        print(random_question)
        answer = input("Yes or No: ")
