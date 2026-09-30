# m13l03-02 · Nesting an if inside every else

**Lesson:** [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) (lesson 13.3, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

In the lesson: Read it from the top. If the score is at least ninety the letter is A and we are done. Otherwise the grade is still undecided, so we ask again inside the else. At least eighty gives B. Otherwise ask again. At least seventy gives C, at least sixty gives D, and anything left is an F. The logic is right and the comments make the reasoning clear. The trouble is the shape. Every new question adds another level of indentation, so by the fourth test the code is marching off to the right, and a longer chain would fall off the screen. Python offers a neater way to say the same thing.

## Files

- [`starter/letterGrade.py`](starter/letterGrade.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/letterGrade.py` alongside the lesson.
2. Notes from the lesson:
   - Line 4: everything not an A is still undecided, so test again in here
   - Line 11: four tests deep, and the code is marching off to the right

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
