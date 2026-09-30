# m20l02-02 · Writing a method, and calling it

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: The initialiser is as before, and now there are two more methods under it. Notice they sit at the same indentation as dunder init, all inside the class. The first, speak, reads self dot name and builds a string from it; it returns a value and changes nothing. The second, birthday, writes to self dot age, adding a year to whichever dog it was called on; it changes the object and returns nothing at all. Both are perfectly ordinary functions. Run it and the first line shows Fido being noisy. Then the birthday call moves the age from three to four. The last line calls speak the long way round, through the class, passing fido as the argument by hand, and gets exactly the same answer.

## Files

- [`starter/dogMethods.py`](starter/dogMethods.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-02/starter`
2. Read `dogMethods.py` the way the lesson builds it:
   - Lines 1–6: The initialiser is as before
   - Lines 7–9: speak reads self dot name
   - Lines 10–12: writes to self dot age
   - Lines 13–18: Run it and the first line
3. Notes from the lesson:
   - Line 9: self.name is the name of the dog this call was made on
   - Line 12: a method may change the instance; no return needed
   - Line 18: Dog.speak(fido) is the same call, spelled the long way
4. Run it: `python3 dogMethods.py`.
5. Check it from the repository root: `./check m20l02-02`.

## Expected output

```text
Fido says woof
4
Fido says woof
```

## How to check

`./check m20l02-02` copies `starter/` into a scratch directory and runs `python3 dogMethods.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
