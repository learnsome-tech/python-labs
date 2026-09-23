# Hands-on Python: Complete Video Course & Book — lesson m18l02 — Packages, And Your Own Library
# https://learnsome.tech/courses/python-course/watch?lesson=m18l02
# © LearnSome.tech
# weather/__init__.py, the plain version
'''The weather package.'''

# the re-exporting version
from weather.report import summary

# which lets a caller write
from weather import summary
