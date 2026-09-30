# m21l03-01 · A date is a value, not a piece of text

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Read along

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: Nearly everybody stores their first date as a string, and nearly everybody regrets it. Two strings cannot be subtracted to find out how many days apart they are, they sort in a strange order unless you were careful about leading zeros, and there is nothing to stop one of them saying the thirty second of Movember. The standard library has a module named datetime holding the three types you need. A date is a single day. A datetime is a day plus a time of day. And a timedelta is a length of time, which is what you get when you subtract one from another, and what you add to move forwards or backwards. Import the three names and the whole subject becomes arithmetic.

## Files

- [`starter/a-date-is-a-value-not-a-piece-of-text.py`](starter/a-date-is-a-value-not-a-piece-of-text.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-date-is-a-value-not-a-piece-of-text.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m21l03-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
