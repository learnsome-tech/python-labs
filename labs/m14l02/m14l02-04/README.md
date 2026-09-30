# m14l02-04 · Set up the test data twice

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: That double appearance of the test data is worth stating as a rule, because it holds for every interactive loop. The data must be initialised before the loop, in order for the first test of the while condition to work at all. The test must also work when execution loops back from the end of the body, which means the data has to be set up a second time, inside the loop, commonly as the action in the very last line. It is easy to forget that second time. The skeleton on screen is the shape to remember.

## Files

- [`starter/set-up-the-test-data-twice.py`](starter/set-up-the-test-data-twice.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/set-up-the-test-data-twice.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
