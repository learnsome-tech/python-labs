# m22l02-05 · mypy: the tool that does check them

**Lesson:** [Type Hints](https://learnsome.tech/learn/python-course/m22l02) (lesson 22.2, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

In the lesson: So who does the checking? A separate program called a type checker, and the best known is mypy. You install it with pip, and it reads your files without running them. Run it on both files from a moment ago. The annotated shopping cart is clean, and mypy says so. The doubling program is not: it reports the file, the line number, the argument, the type you passed and the type the function promised, then counts the errors. Nothing was executed to find that. This is the payoff for writing the hints: a whole class of mistake, the kind that normally shows up as a strange error deep inside somebody else's function, gets caught before the program starts.

## Files

- [`starter/terminal`](starter/terminal): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/terminal` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
