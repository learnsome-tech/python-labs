# Hands-on Python: Complete Video Course & Book — lesson m06l03 — Function Parameters
# https://learnsome.tech/courses/python-course/watch?lesson=m06l03
# © LearnSome.tech
'''Triggers error inside nested function call'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    happyBirthday('Emily')
    happyBirthday('Andre')
    # next line causes error, illustrates traceback
    happyBirthday(2) 

main()
