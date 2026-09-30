# m20l02-06 · Docstrings on a class and on a method

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: Document classes the way you learned to document functions. A string as the very first thing in the class body is the class docstring: a sentence saying what this kind of object is. A string as the first thing in the method body is the method docstring, saying what one call does and what it gives back. Both are stored on the object under the attribute dunder doc, and they are printed straight back here so you can see they are real data and not a comment. That is also exactly where the help function reads from, and where your editor finds the little box it shows when you type a dot. Write them as you go; they cost one line, and they are the only documentation that can never drift away from the code.

## Files

- [`starter/dogDoc.py`](starter/dogDoc.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-06/starter`
2. Read `dogDoc.py` the way the lesson builds it:
   - Lines 1–4: the very first thing in the class body
   - Lines 5–12: the first thing in the method body
   - Lines 13–17: printed straight back
3. Notes from the lesson:
   - Line 4: the class docstring: what this kind of object is
   - Line 11: the method docstring: what one call does, and what it returns
4. Run it: `python3 dogDoc.py`.
5. Check it from the repository root: `./check m20l02-06`.

## Expected output

```text
A dog with a name and an age in years.
Return this dog's sound, with its name in front.
Return this dog's sound, with its name in front.
```

## How to check

`./check m20l02-06` copies `starter/` into a scratch directory and runs `python3 dogDoc.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
