# Hands-on Python: Complete Video Course & Book — lesson m21l02 — JSON And CSV
# https://learnsome.tech/courses/python-course/watch?lesson=m21l02
# © LearnSome.tech
import json

print(json.dumps({'when': (1, 2), 'ok': True, 'gone': None}))
print(json.dumps({7: 'seven'}))
print(json.loads('{"7": "seven"}'))

try:
    print(json.dumps({'tags': {'a', 'b'}}))
except TypeError as problem:
    print('TypeError:', problem)
