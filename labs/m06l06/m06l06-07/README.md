# m06l06-07 · A global constant used inside functions

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: Here is the example program constant. At the top of the file, outside every definition, a single assignment statement gives the name PI its value, three point one four one five nine and so on, and the comment beside it says that this is the only place the value of PI is set. Then come the two functions. The first returns the area of a circle for a given radius, and the second returns the circumference, and each uses PI without being passed in. Then main prints both for a radius of five, and the last line calls main. The example uses numbers with decimal points, which we discuss properly a little later on. Notice the name: by convention, names for constants are written in all capital letters.

## Files

- [`starter/constant.py`](starter/constant.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/constant.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a single assignment statement
   - Lines 4–6: the area of a circle
   - Lines 7–9: the circumference
   - Lines 10–15: main prints both
3. Notes from the lesson:
   - Line 3: the one place the value of PI is set
   - Line 6: PI is visible in here without being passed in
   - Line 13: main calls both functions you defined above

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l06-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
