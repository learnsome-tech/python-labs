# m20l03-07 · The same car, composed instead

**Lesson:** [Inheritance And Composition](https://learnsome.tech/learn/python-course/m20l03) (lesson 20.3, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a subclass that overrides a method and calls super, test types with isinstance, build the same design out of composition instead, and choose between the two on purpose.

In the lesson: Engine is untouched. Car now takes an engine as an argument and stores it in an attribute. The car's own start method asks the engine to do the engine part and adds what only the car knows, its name. That is delegation, and it is most of what composition looks like in practice. The car still starts. Horsepower is still reachable, through the engine, which is honest about where it belongs. And a car is no longer an engine, so nothing that expects an engine will accept one by accident. You can hand in a different engine, or two of them, or a test engine that does nothing, without editing the Car class at all.

## Files

- [`starter/carCompose.py`](starter/carCompose.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l03/m20l03-07/starter`
2. Read `carCompose.py` the way the lesson builds it:
   - Lines 1–8: Engine is untouched
   - Lines 9–13: stores it in an attribute
   - Lines 14–16: The car's own start method
   - Lines 17–21: The car still starts
3. Notes from the lesson:
   - Line 10: no base class: Car is its own thing
   - Line 13: the engine arrives as an argument and is held, not inherited
   - Line 16: delegation: ask the engine, then add what the car knows
4. Run it: `python3 carCompose.py`.
5. Check it from the repository root: `./check m20l03-07`.

## Expected output

```text
Mini: engine running
90
False
```

## How to check

`./check m20l03-07` copies `starter/` into a scratch directory and runs `python3 carCompose.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
