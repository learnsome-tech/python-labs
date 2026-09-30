# m21l03-08 · Not for anything secret

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Read along

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: One warning, and it is not a small one. The random module is not random in the way a security person means. It is a mathematical generator that produces a fixed sequence from its starting point, which is exactly the property that made the seed useful a moment ago. Given enough of its output, somebody can work out where it is and predict every number it will produce next. So never use it for a password, a session token, a password reset link or an encryption key. For those the standard library has a module named secrets, with the same shaped functions, drawing from the operating system's own source of unpredictability. For games, simulations, sampling and shuffling, random is exactly right.

## Files

- [`starter/not-for-anything-secret.py`](starter/not-for-anything-secret.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/not-for-anything-secret.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m21l03-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
