# m13l04-06 · Choosing a random starting point

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: The ball starts from an arbitrary point inside the allowed rectangle, and that is wrapped up in this small utility function. It uses the randrange function from the random module. Note the pattern in both the range function and randrange: the end you state is one past the last value you actually want, which is why each bound has a one added to it here. There is nothing nested in this function at all; it is here because the main animation calls it.

## Files

- [`starter/bounce1.py`](starter/bounce1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bounce1.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
