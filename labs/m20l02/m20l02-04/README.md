# m20l02-04 · Class attributes and instance attributes

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: Species is assigned in the class body itself, not on self. That makes it a class attribute: one single value, stored on the class, and every instance sees it. The initialiser still sets name on self, so name is an instance attribute, different for each dog. Run it, and the first line shows both dogs reporting the same species. Change it on the class and both change together, because there was only ever one copy. Now the subtle line. Assigning through one instance does not touch the class at all; it creates a new instance attribute on that dog, which shadows the class one. Fido is a wolf, Rex is still a dog, and the class is still a dog. Reading falls back to the class; writing always lands on the instance.

## Files

- [`starter/dogSpecies.py`](starter/dogSpecies.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-04/starter`
2. Read `dogSpecies.py` the way the lesson builds it:
   - Lines 1–4: assigned in the class body
   - Lines 5–7: The initialiser still sets
   - Lines 8–15: the first line shows both dogs
3. Notes from the lesson:
   - Line 4: one value, stored on the class, shared by every instance
   - Line 14: assigning through an instance makes a new instance attribute
4. Run it: `python3 dogSpecies.py`.
5. Check it from the repository root: `./check m20l02-04`.

## Expected output

```text
Canis familiaris Canis familiaris
dog dog
wolf dog dog
```

## How to check

`./check m20l02-04` copies `starter/` into a scratch directory and runs `python3 dogSpecies.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
