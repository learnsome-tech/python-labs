# m20l01-05 · The class itself, and an instance of it

**Lesson:** [Classes And Instances](https://learnsome.tech/learn/python-course/m20l01) (lesson 20.1, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a class with an initialiser, create instances of it, store data on each instance, and explain the difference between the class and an instance of it.

In the lesson: Here is the distinction that beginners trip over, in the shell. Define a tiny class in the shell first. Ask for the bare name Dog and Python shows you an object: the class is itself a value living in your program, and its own type is type. Now make one instance. The instance reports its type as Dog. And isinstance asks the same question in the form you will actually write. Then the important pair. The instance has the attribute n, because dunder init put it there on self. But ask the class for it and you get an attribute error, because that data was never on the class. The class is the cutter; each instance is a separate biscuit.

## Files

- [`starter/shell-the-class-itself-and-an-instance-of-it.py`](starter/shell-the-class-itself-and-an-instance-of-it.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l01/m20l01-05/starter`
2. Read `shell-the-class-itself-and-an-instance-of-it.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   class Dog:
       def __init__(self, n):
           self.n = n
   Dog
   type(Dog)
   d = Dog('Fido')
   type(d)
   isinstance(d, Dog)
   d.n
   Dog.n
   ```
4. Run it: `python3 -i < shell-the-class-itself-and-an-instance-of-it.py`.
5. Check it from the repository root: `./check m20l01-05`.

## Expected output

```text
<class '__main__.Dog'>
<class 'type'>
<class '__main__.Dog'>
True
'Fido'
Traceback (most recent call last):
AttributeError: type object 'Dog' has no attribute 'n'
```

## How to check

`./check m20l01-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-class-itself-and-an-instance-of-it.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
