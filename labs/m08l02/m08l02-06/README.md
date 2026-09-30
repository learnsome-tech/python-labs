# m08l02-06 · A warning worth its own screen

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Read along

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: This warning catches nearly everybody once. The format function returns the formatted string. It does not change its parameters. Write it as a complete statement on a line of its own in a program and the tidy rounded string is created, returned, and thrown away, with no effect on the variable. Nothing appears, nothing is stored, and the learner stares at unchanged output wondering why. The first line on screen is that mistake. The second is the tutorial's fix: save the formatted value in a variable so the string can be used again by name. The third is the other common fix, passing it straight to the print function.

## Files

- [`starter/a-warning-worth-its-own-screen.py`](starter/a-warning-worth-its-own-screen.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-warning-worth-its-own-screen.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
