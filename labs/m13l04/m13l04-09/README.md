# m13l04-09 · Nesting in every direction

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: Nesting is not only about ifs inside loops. A loop can go inside the block of an if, so that the repetition happens in one case only. An if can go inside another if, which is precisely the shape that elif flattens out. Loops can go inside loops. There is no special rule for each combination, because it is one rule applied over and over: a heading owns the block indented beneath it, whatever that block contains. When you read unfamiliar code, count the levels of indentation before you read the words.

## Files

- [`starter/nesting-in-every-direction.py`](starter/nesting-in-every-direction.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/nesting-in-every-direction.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l04-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
