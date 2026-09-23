# Hands-on Python: Complete Video Course & Book — lesson m05l03 — The String Format Method
# https://learnsome.tech/courses/python-course/watch?lesson=m05l03
# © LearnSome.tech
'''Compare print with concatenation and with format string.'''

applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print(interviewer + ' will interview ' + applicant + ' at ' + time +'.')
print(interviewer, ' will interview ', applicant, ' at ', time, '.', sep='')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))
