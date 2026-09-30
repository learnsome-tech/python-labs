# m22l01-05 · Running them: pytest -q

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: Pytest is not part of the standard library, so install it once with pip, then run it from the folder holding your code. The q flag is short for quiet, and quiet is what you want most of the time. Here is the whole report: three dots, one per test that passed, and a summary line saying three passed and how long it took. That is the shape of a good day. Notice what you did not have to do: you never listed your tests anywhere, never imported them, and never called them. You wrote functions in a file with the right name and pytest found them, which is the feature that makes writing the next test cost nothing.

## Files

- [`starter/terminal`](starter/terminal): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/terminal` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
