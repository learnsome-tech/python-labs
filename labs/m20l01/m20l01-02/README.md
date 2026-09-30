# m20l01-02 · A first class, and a first instance

**Lesson:** [Classes And Instances](https://learnsome.tech/learn/python-course/m20l01) (lesson 20.1, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a class with an initialiser, create instances of it, store data on each instance, and explain the difference between the class and an instance of it.

In the lesson: Here is a class of your own. The word class, then the name Dog, then a colon, and everything indented under it is the class body. By strong convention a class name is written in capitalised words run together, so a reader can tell a class from an ordinary variable at a glance. Inside the body is a function whose name is dunder init, spelled with two underscores on each side. That is the initialiser. It runs automatically when you call the class, and its job is to set up the new object. Its first parameter, self, is that new object. Assigning to self dot name and self dot age stores two pieces of data on it. Then we call the class, hand it a name and an age, and read them straight back out with a dot.

## Files

- [`starter/dog1.py`](starter/dog1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l01/m20l01-02/starter`
2. Read `dog1.py` the way the lesson builds it:
   - Lines 1–3: The word class
   - Lines 4–6: That is the initialiser
   - Lines 7–8: Then we call the class
   - Lines 9–12: read them straight back
3. Notes from the lesson:
   - Line 3: class, then a CapWords name, then a colon, then an indented body
   - Line 4: __init__ runs when you call the class; self is the new object
   - Line 8: calling Dog makes an instance and hands it back to you
4. Run it: `python3 dog1.py`.
5. Check it from the repository root: `./check m20l01-02`.

## Expected output

```text
Fido
3
Dog
{'name': 'Fido', 'age': 3}
```

## How to check

`./check m20l01-02` copies `starter/` into a scratch directory and runs `python3 dog1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
