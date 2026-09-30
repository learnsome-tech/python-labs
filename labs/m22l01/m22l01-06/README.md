# m22l01-06 · A real failure, and what it tells you

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: Now break it on purpose. Someone edits the last line so it returns the amount taken off rather than the price after the discount, which is the kind of mistake that reads perfectly well. Run pytest with the x flag, which stops at the first failure. Read the report from the top. The capital F says a test failed. Then the failing test is named, and its source is shown with an arrow marking the exact assertion. The lines beginning with capital E are the explanation: the assertion said something should equal eighteen, the value was two, and the where line tells you which call produced it. Then the file and line number, and a summary. Everything you need, without touching the program.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pricing.py` alongside the lesson.
2. Notes from the lesson:
   - Line 5: the bug: this returns the discount, not the new price

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
