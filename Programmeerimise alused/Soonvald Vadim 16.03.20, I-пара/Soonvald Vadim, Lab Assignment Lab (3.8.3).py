import random # Import random
import datetime # Impressing time

# Information about the author of the work
print(60*'=')
print('R&D: Lab assignment Lab (3.8.3)')
now_date = datetime.date.today ()
print('Date: ', now_date)
print(60*'=')
print('The author of the work: Vadim Soonvald')
print('Specialty: Tarkvaraarendaja')
print('Group: JPTVR19')
print(60*'=')

print("Welcome to the quiz!")
count = 0
print("Question 1: How much will it be if you subtract 5 from 10?")
answer = input()
if answer == "5":
    print(50*'=')
    print("You are a great fellow, the answer is right!")
    print(50*'=')
    count += 1
    print(count)
else:
    print(50*'=')
    print("The answer is incorrect; the correct answer is 5")
    print(50*'=')
    
print("Question 2: Who can fly?\nVariants of the answer:\n1)Gulka\n2)Mouse\n3)Fish\nEnter only the number of response variant.")
answer = input()
if answer == "1":
    print(50*'=')
    print("This is the correct answer, congratulations!")
    print(50*'=')
    count += 1
    print(count)
if answer == "2":
    print(50*'=')
    print("Mice can't fly, the correct answer is option number 1")
    print(50*'=')
if answer == "3":
    print(50*'=')
    print("Fish can't fly, the correct answer is option number 1")
    print(50*'=')
    
print("Question 3: What will be the answer if 10: 2?\nVariants of the answer:\nA)3\nB)5\nC)2\nEnter only the letter of the answer variant.\nEnter the answer in English.")
answer = input()
answer.lower()
if answer == "a":
    print(50*'=')
    print("Unfortunately, this is the wrong answer.")
    print(50*'=')
if answer == "b":
    print(50*'=')
    print("Unfortunately, this is the wrong answer.")
    print(50*'=')
if answer == "c":
    print(50*'=')
    print("This is the correct answer, congratulations!")
    print(50*'=')
    count += 1
    print(count)
    
print("Question 4: Who represents Russia at Eurovision 2020? \ nVariants of the answer:\n1)Sergey Lazarev\n2)Little Big\n3)Grigory Leps\nEnter only the number of the answer variant.")
answer = input()
if answer == "1":
    print(50*'=')
    print("This is the wrong answer, the correct answer is option number 2")
    print(50*'=')
if answer == "2":
    print(50*'=')
    print("This is the correct answer, congratulations!")
    print(50*'=')
    count += 1
    print(count)
if answer == "3":
    print(50*'=')
    print("This is the wrong answer, the correct answer is option number 2")
    print(50*'=')
    
print("Question 5: If you add 235 to 100, what is the answer?")
answer = input()
if answer == "335":
    print(50*'=')
    print("You are a great fellow, the answer is right!")
    print(50*'=')
    count += 1
    print(count)
else:
    print(50*'=')
    print("The answer is incorrect; the correct answer is 5")
    print(50*'=')

print("Congratulations! You have completed the quiz! Total correct answers:",count,".")
procent = 100/5 * count # A formula where only one change will be needed if the number of questions changes.
print("In percentage terms, you decided correctly:",procent,"%.")