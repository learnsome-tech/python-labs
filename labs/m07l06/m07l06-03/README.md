# m07l06-03 · The trace that catches the culprit

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: Read the table one row at a time. Line four sets number to one, line five prints, line six increases number to two, exactly as intended. Then line three moves on to the next element, and line four runs again, because it is inside the loop body, and it puts number straight back to one. The increment on line six was undone before it could ever be used. Notice how much the table tells you that the output could not: not merely that the count is wrong, but the precise line that spoils it. Notice too that as soon as the wrong value appears you can stop. So here is the warning to remember. Always make sure your one time initialisation for a loop goes before the loop, and not inside it.

## Files

- [`starter/the-trace-that-catches-the-culprit.txt`](starter/the-trace-that-catches-the-culprit.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-trace-that-catches-the-culprit.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
