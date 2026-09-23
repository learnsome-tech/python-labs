# Hands-on Python: Complete Video Course & Book — lesson m21l02 — JSON And CSV
# https://learnsome.tech/courses/python-course/watch?lesson=m21l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import json
book = {'title': 'Dune', 'year': 1965}
json.dumps(book)
#   '{"title": "Dune", "year": 1965}'
type(json.dumps(book))
#   <class 'str'>
json.loads('{"a": 1, "b": [2, 3]}')
#   {'a': 1, 'b': [2, 3]}
json.loads('{"a": 1}')['a'] + 1
#   2
