# m10l02-04 · getKeys, now returning a set

**Lesson:** [Mad Libs Revisited: The Whole Program](https://learnsome.tech/learn/python-course/m10l02) (lesson 10.2, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can read the revised mad lib program function by function, explain why getKeys returns a set, and name the creative problem solving steps that produced it.

In the lesson: Here is the function inside the revised program. Above it the file has a ten line comment describing the program, which is off screen. Notice that the documentation string now says a set containing all the keys. The body is untouched: the same empty list, the same end set to zero, the same repeat loop, the same two find calls, the same slice, the same append. Only the last line differs. It builds a set from the accumulated list, and a set cannot hold a repetition, so the duplicates fall away. Be aware of what else you lose: a set has no order at all, so the cues will be offered to the user in an order you cannot predict. For prompting, that does not matter.

## Files

- [`starter/madlib2.py`](starter/madlib2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib2.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the documentation string now says a set
   - Lines 4–13: The body is untouched
   - Lines 14: Only the last line differs
3. Notes from the lesson:
   - Line 14: set(keyList) throws the duplicates away, and returns no order

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
