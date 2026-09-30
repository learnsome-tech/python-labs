# m09l05-04 · The start of multiplyAll

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Read along

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Accumulating a list with append is particularly useful in a loop. Read the start of this simple example. The heading names two parameters, the list of numbers to work from and the number to multiply by, and the docstring says what it promises: a new list containing all the elements of the given list, each multiplied by the multiplier. One line of that docstring is a leftover from Python two: the sample call is written with print and no parentheses, so do not type it as it stands. The tutorial's version of this fragment ends with a comment saying more to come, because the body is still missing. Clearly the work will be repetitious: we process each element of the list, so a for each loop is right, and we accumulate a new list as we go.

## Files

- [`starter/multiply1.py`](starter/multiply1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/multiply1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the heading names two parameters
   - Lines 4–8: the docstring says what it promises
3. Notes from the lesson:
   - Line 3: two parameters: the list to work from, and the multiplier

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m09l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
