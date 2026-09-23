# Hands-on Python: Complete Video Course & Book — lesson m18l02 — Packages, And Your Own Library
# https://learnsome.tech/courses/python-course/watch?lesson=m18l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import os.path
import email
email.__name__
#   'email'
os.path.basename(email.__file__)
#   '__init__.py'
email.__path__[0].endswith('email')
#   True
import email.message
email.message.__name__
#   'email.message'
from email.message import EmailMessage
EmailMessage.__name__
#   'EmailMessage'
