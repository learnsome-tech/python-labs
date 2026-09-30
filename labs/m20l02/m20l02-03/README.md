# m20l02-03 · self is filled in, not conjured

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: Let us prove that self is not magic. Define the smallest possible class with one method, and make one instance. Calling it the ordinary way, through the instance, gives woof. Calling it through the class and passing the instance yourself does the same work and gives the same answer. Those two lines are the same operation. Reached through the class, speak is a plain function. Reached through the instance, it is a method: an object that remembers which instance it came from and slots that in as the first argument. That is the whole trick. And if you leave the instance out altogether, Python tells you plainly that one required positional argument, self, is missing. Python prefers spelling this out to hiding it.

## Files

- [`starter/shell-self-is-filled-in-not-conjured.py`](starter/shell-self-is-filled-in-not-conjured.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-03/starter`
2. Read `shell-self-is-filled-in-not-conjured.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   class Dog:
       def speak(self):
           return 'woof'
   d = Dog()
   d.speak()
   Dog.speak(d)
   type(Dog.speak).__name__
   type(d.speak).__name__
   Dog.speak()
   ```
4. Run it: `python3 -i < shell-self-is-filled-in-not-conjured.py`.
5. Check it from the repository root: `./check m20l02-03`.

## Expected output

```text
'woof'
'woof'
'function'
'method'
Traceback (most recent call last):
TypeError: Dog.speak() missing 1 required positional argument: 'self'
```

## How to check

`./check m20l02-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-self-is-filled-in-not-conjured.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
