# m20l03-03 · super, in the initialiser and in a method

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: This is the pattern you will write most often. An employee has a name and a salary. A manager is a kind of employee, so the manager adds one field of its own without repeating the other two. Its initialiser calls the super call with dunder init, which lets the base do its own job of storing name and salary, and only then sets reports. Its describe method extends the description rather than retyping it: the super call gives back the base sentence and the manager adds a clause. The printed description shows both halves, and the second line proves all three attributes are on the one object. Prefer the super call to naming the base class by hand, because it keeps working when the class hierarchy changes underneath you.

## Files

- [`starter/manager.py`](starter/manager.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l03/m20l03-03/starter`
2. Read `manager.py` the way the lesson builds it:
   - Lines 1–9: An employee has a name and a salary
   - Lines 10–14: the manager adds one field
   - Lines 15–17: extends the description
   - Lines 18–21: The printed description
3. Notes from the lesson:
   - Line 13: let the base set up its own fields, then add yours
   - Line 17: extend rather than retype: the base text stays in one place
4. Run it: `python3 manager.py`.
5. Check it from the repository root: `./check m20l03-03`.

## Expected output

```text
Ada earns 90000 and leads 4
Ada 90000 4
```

## How to check

`./check m20l03-03` copies `starter/` into a scratch directory and runs `python3 manager.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
