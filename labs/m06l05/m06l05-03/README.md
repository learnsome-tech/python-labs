# m06l05-03 · Substitution, one step at a time

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: It is worth watching that replacement happen slowly. After the function f finishes executing from inside the first line on screen, it is as if the statement temporarily became the second line, printing nine. Similarly, when executing the fourth line, the interpreter first evaluates f of three and effectively replaces the call by the returned result, nine, as if the statement temporarily became the fifth line. Then it evaluates f of four and replaces that call by sixteen, as if the statement became the last line, resulting finally in twenty-five being calculated and printed. Nothing here is magic and nothing is simultaneous. Each call is made, each call hands back a value, and the expression closes up around it.

## Files

- [`starter/substitution-one-step-at-a-time.py`](starter/substitution-one-step-at-a-time.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/substitution-one-step-at-a-time.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
