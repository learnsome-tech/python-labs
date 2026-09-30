# m13l05-09 · Do not use if else to produce True or False

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Here is a correct but redundant version of that helper. Read what the if else does. If the compound expression is true, return True. If it is false, return False. In both cases it returns the same value as the test itself. So the four lines can be replaced by one: return the condition. In general you should never need an if else statement to choose between true and false values.

## Files

- [`starter/isBetween.py`](starter/isBetween.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/isBetween.py` alongside the lesson.
2. Notes from the lesson:
   - Line 5: returns True exactly when the condition above was True

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l05-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
