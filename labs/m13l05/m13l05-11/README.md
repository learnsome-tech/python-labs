# m13l05-11 · chooseButton one dot py: the Boolean functions

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: The example program that puts all this to work is called choose button one dot py. Here is the top of it. The helper is one return statement, exactly as we worked out, though it calls its first parameter x rather than val. Below it, the outer function pulls the two corners out of the rectangle and joins the two coordinate tests with and. It also takes the point first and the rectangle second, the opposite order from the sketch we started with, so read the heading before you call it. One new piece of syntax appears there. A backslash at the very end of a line tells Python that the statement continues on the line below, which is how a long condition is wrapped without unclosed brackets.

## Files

- [`starter/chooseButton1.py`](starter/chooseButton1.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/chooseButton1.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–10: the helper is one return statement
   - Lines 11–18: the outer function
3. Notes from the lesson:
   - Line 17: a backslash at the end of a line continues the statement below

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l05-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
