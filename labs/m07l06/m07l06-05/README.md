# m07l06-05 · The table for a call inside a call

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: Follow the calls carefully and use the values they return. A dash in the table means the variable is undefined at that moment. Local variables, including formal parameters like x, are undefined before they are first given a value, and they are undefined again once the function has finished, which is why x keeps disappearing from the table. See how line five appears three times. We start it, break off to run m, come back and substitute fifteen, break off again for the second call, come back and substitute twenty five, and only then is there an addition to do. Leaving a row, running the call, and returning to the same line is what you need for the exercises.

## Files

- [`starter/the-table-for-a-call-inside-a-call.txt`](starter/the-table-for-a-call-inside-a-call.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-table-for-a-call-inside-a-call.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
