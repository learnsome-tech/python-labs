# m19l02-06 · When a loop is the clearer choice

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Read along

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: A comprehension is not automatically better, and knowing when to stop is a real skill. The rule I would give you: one for and at most one simple if, and it fits comfortably on one line, so use the comprehension. Beyond that, write the loop. The expression on screen is legal Python and nobody can read it. There are two other cases where the loop wins outright. If you are building two lists in the same pass, a comprehension forces you to loop twice or to be clever. And if the body does something rather than producing a value, such as printing or writing to a file, use a loop. A comprehension whose result you throw away is a comprehension misused.

## Files

- [`starter/when-a-loop-is-the-clearer-choice.py`](starter/when-a-loop-is-the-clearer-choice.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/when-a-loop-is-the-clearer-choice.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m19l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
