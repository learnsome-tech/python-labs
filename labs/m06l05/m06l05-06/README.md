# m06l05-06 · The None you did not expect

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: Try the same mistake in a real program. Open addition five again and change the last line of its main function so that it reads as on screen, wrapping the call in print. Then run it. The desired printing is already done inside sumProblem, and you have added a statement that prints what sumProblem returns. Although sumProblem returns nothing explicitly, Python makes every function return something, and when there is nothing explicit that something is the special value None. You will see it in the Shell output, on a line of its own after the sentence. This is a fairly common error. If you see a None in your printed output where you do not expect one, it is very likely that you printed the return value of a function that returned nothing explicitly.

## Files

- [`starter/the-none-you-did-not-expect.py`](starter/the-none-you-did-not-expect.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-none-you-did-not-expect.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l05-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
