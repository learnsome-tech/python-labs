# Hands-on Python: Complete Video Course & Book — lesson m09l04 — Split And Join
# https://learnsome.tech/courses/python-course/watch?lesson=m09l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

seq = 'Go:  Tear some strings apart!'.split()
' '.join(seq)
#   'Go: Tear some strings apart!'
''.join(seq)
#   'Go:Tearsomestringsapart!'
'//'.join(seq)
#   'Go://Tear//some//strings//apart!'
'##'.join(seq)
#   'Go:##Tear##some##strings##apart!'
':'.join(['one', 'two', 'three'])
#   'one:two:three'
