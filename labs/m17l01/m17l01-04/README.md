# m17l01-04 · The shape of the whole statement

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: This is the full shape, and you will rarely use all of it at once. The try block and at least one except clause are the required part. You may write several except clauses, and the first one whose type matches is the one that runs. The else clause runs only if the try block got all the way through without raising. The finally clause runs on every way out of the statement: the block succeeded, or it failed and was handled, or it failed and is still travelling up. We will watch each of those in turn.

## Files

- [`starter/the-shape-of-the-whole-statement.txt`](starter/the-shape-of-the-whole-statement.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-shape-of-the-whole-statement.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
