# m13l05-07 · A test worth wrapping in a function

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Complicated tests are much easier to live with inside a function with a good name. Think how to finish this one, which asks whether a point lies inside a rectangle. A rectangle is built from two diagonally opposite points, and these are the methods that get them back: get P one and get P two. From each you can get the coordinates with get x and get y. So the job comes down to asking whether the horizontal coordinate lies between the two corner values, and the same vertically.

## Files

- [`starter/isInside.py`](starter/isInside.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/isInside.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l05-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
