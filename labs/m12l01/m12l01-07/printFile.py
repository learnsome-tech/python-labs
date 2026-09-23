# Hands-on Python: Complete Video Course & Book — lesson m12l01 — Files: Writing And Reading
# https://learnsome.tech/courses/python-course/watch?lesson=m12l01
# © LearnSome.tech
'''Quick illustration of reading a file.
(needs revisedFile.py run first to create sample3.txt)
'''

inFile = open('sample3.txt', 'r')
contents = inFile.read()
print(contents)
