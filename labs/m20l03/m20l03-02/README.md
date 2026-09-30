# m20l03-02 · Subclassing, and overriding a method

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: The base class holds the initialiser and a general version of speak. Dog names Animal in parentheses, so it inherits everything. It writes no initialiser of its own, so calling Dog with a name runs the one it inherited. It does define speak again, and because the name matches, the new one is used for dogs instead of the inherited one; that is overriding. Puppy goes one level further, inheriting from Dog, and its speak uses the super call to run the version it would otherwise have replaced, then adds to the result. Then the loop calls speak on one of each, and each object answers with the most specialised version available to it. Python finds the method by searching the class, then its base, then the base of that.

## Files

- [`starter/animalSpeak.py`](starter/animalSpeak.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l03/m20l03-02/starter`
2. Read `animalSpeak.py` the way the lesson builds it:
   - Lines 1–8: The base class holds
   - Lines 9–12: Dog names Animal in parentheses
   - Lines 13–16: Puppy goes one level further
   - Lines 17–19: the loop calls speak
3. Notes from the lesson:
   - Line 10: Dog inherits __init__ from Animal; it does not repeat it
   - Line 11: same method name as the base: this overrides it
   - Line 16: super().speak() runs the Dog version, then adds to it
4. Run it: `python3 animalSpeak.py`.
5. Check it from the repository root: `./check m20l03-02`.

## Expected output

```text
Thing makes a sound
Fido says woof
Bit says woof, quietly
```

## How to check

`./check m20l03-02` copies `starter/` into a scratch directory and runs `python3 animalSpeak.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
