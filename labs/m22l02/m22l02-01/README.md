# m22l02-01 · Saying out loud what you already assumed

**Lesson:** [Type Hints](https://learnsome.tech/learn/python-course/m22l02) (lesson 22.2, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

In the lesson: Look at the first line on screen. What is prices meant to be? A list of numbers, presumably, but nothing says so, and the only way to find out is to read the body or hope the name is honest. The second line says it: prices is a list of floats, discount is a float that defaults to nothing off, and the arrow at the end says the function hands back a float. That is a type hint. It is not a check, it is not enforced, and Python will run either version identically. It is a sentence about your intentions, written where nobody can lose it, and it is machine readable, which is the part that makes it more than a comment.

## Files

- [`starter/saying-out-loud-what-you-already-assumed.py`](starter/saying-out-loud-what-you-already-assumed.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/saying-out-loud-what-you-already-assumed.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l02-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
