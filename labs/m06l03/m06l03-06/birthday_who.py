# Hands-on Python: Complete Video Course & Book — lesson m06l03 — Function Parameters
# https://learnsome.tech/courses/python-course/watch?lesson=m06l03
# © LearnSome.tech
'''User input supplies function parameter'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

main()
