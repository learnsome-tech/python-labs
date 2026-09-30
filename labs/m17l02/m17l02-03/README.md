# m17l02-03 · Choosing which built-in exception to raise

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: Which exception should you raise? Almost always one that already exists. The two you will reach for constantly are these. ValueError means the type of the argument was right but its value is not usable: a negative age, an empty list where a total was wanted. TypeError means the argument was not that sort of thing at all: a string where a number belonged. Then there are the container ones, KeyError and IndexError, for a key or a position that is not there, and RuntimeError as a last resort when nothing more precise fits. The rule is to raise the exception a reader would have guessed, because your caller will be writing except clauses against it.

## Files

- [`starter/choosing-which-built-in-exception-to-raise.txt`](starter/choosing-which-built-in-exception-to-raise.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/choosing-which-built-in-exception-to-raise.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
