# m14l02-05 · A sentinel says when the data ends

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Read along

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: A practical alternative is a sentinel: a piece of data that would not make sense in the regular sequence, used to mark the end of the input. You could agree to use a line reading done, in capitals. Even simpler, if every real line has some text on it, use an empty line. The Python shell itself uses that approach when you enter a statement with an indented body. So what should the while condition be? Your first thought might be that the line equals the empty string, but that is the termination condition, not the continuation condition. You need the opposite. To negate a condition you may use the word not, as in English, and here there is a shorter way, the not equals operator.

## Files

- [`starter/a-sentinel-says-when-the-data-ends.py`](starter/a-sentinel-says-when-the-data-ends.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-sentinel-says-when-the-data-ends.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m14l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
