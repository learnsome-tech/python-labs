# m14l02-07 · Comment out one line and it never stops

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: Now try the experiment the tutorial suggests, but read to the end of this sentence first. Comment out the last line of the loop body and run it again: it will never stop. The variable line will forever have the initial value you gave it, that value is not empty, so the condition stays true. You can stop the program by holding the control key and pressing c. That is worth doing once, so the failure feels familiar rather than frightening. It also gives you the habit to build in: as you finish coding a while loop, always check that you change something, inside the loop, that will eventually make the condition false.

## Files

- [`starter/readLinesForever.py`](starter/readLinesForever.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/readLinesForever.py` alongside the lesson.
2. Notes from the lesson:
   - Line 11: with this commented out, line keeps its first value for ever

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
