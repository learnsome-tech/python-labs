# m20l02-05 · The shared mutable attribute trap

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: Here is the classic bug, and it catches experienced people too. The first class puts an empty list in the class body. Because assigning through an instance is the only thing that makes an instance attribute, appending does not assign; it reaches the class attribute and changes it in place. So every dog is sharing the same one list. The second class does it properly: the list is built inside dunder init, so each dog gets a fresh list every time. Run it. Teaching Fido to sit in the bad class teaches Rex to sit as well, which is nonsense. In the good class Rex knows nothing and Fido knows one trick. The rule is short: never put a list, a dictionary or a set in a class body unless you truly want one shared copy.

## Files

- [`starter/tricks.py`](starter/tricks.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-05/starter`
2. Read `tricks.py` the way the lesson builds it:
   - Lines 1–7: an empty list in the class body
   - Lines 8–12: The second class does it properly
   - Lines 13–20: Teaching Fido to sit
3. Notes from the lesson:
   - Line 4: one list for the whole class: every dog appends to that list
   - Line 12: a fresh list per instance, because it is built in __init__
4. Run it: `python3 tricks.py`.
5. Check it from the repository root: `./check m20l02-05`.

## Expected output

```text
['sit']
[]
['sit']
```

## How to check

`./check m20l02-05` copies `starter/` into a scratch directory and runs `python3 tricks.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
