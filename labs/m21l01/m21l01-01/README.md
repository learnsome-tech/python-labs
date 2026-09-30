# m21l01-01 · The close line you will one day forget

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Read along

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: Back in the files module you opened a file, wrote to it, and closed it by hand. Look at those three lines again, because the last one is the fragile one. If your program returns early, or raises an error before it reaches the close call, the file is never closed, and everything you thought you had written can quietly stay in memory and vanish. You cannot fix that by being careful, because being careful is exactly the thing that fails on a bad day. So Python has a piece of syntax for the entire pattern, and it is called the with statement. From this lesson onward, every file in this course is opened with it, and no close call ever appears again.

## Files

- [`starter/the-close-line-you-will-one-day-forget.py`](starter/the-close-line-you-will-one-day-forget.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-close-line-you-will-one-day-forget.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m21l01-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
