# m20l03-06 · Inheritance where it does not belong

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: Let us make the mistake on purpose, so you recognise it later. An engine has a horsepower and knows how to start. Somebody wants a car that can start, sees that Engine already does that, and writes Car inherits from Engine. It runs, and every line of output looks fine. But the claim is false, and Python believes it: the last line says every car is an engine. That will spread. Anything written to accept an engine will now silently accept a car. The car has picked up horsepower as though it were its own attribute. And a car with two engines, or a car whose engine is replaced, cannot be expressed at all, because the car and the engine have been fused into one object.

## Files

- [`starter/carInherit.py`](starter/carInherit.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l03/m20l03-06/starter`
2. Read `carInherit.py` the way the lesson builds it:
   - Lines 1–8: An engine has a horsepower
   - Lines 9–13: Car inherits from Engine
   - Lines 14–18: It runs, and every line
3. Notes from the lesson:
   - Line 10: a Car is not a kind of Engine: this claim is simply false
   - Line 18: and Python believes it: every Car now counts as an Engine
4. Run it: `python3 carInherit.py`.
5. Check it from the repository root: `./check m20l03-06`.

## Expected output

```text
engine running
90
True
```

## How to check

`./check m20l03-06` copies `starter/` into a scratch directory and runs `python3 carInherit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
