# m08l02-04 · Raw floats are not fit to show a human

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Read along

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: You generally do not want to display the floating point result of a calculation in its raw form. It often carries an enormous number of digits after the decimal point, like the first number on screen. What a reader wants is the second. There are two approaches, and they share the same piece of notation. The first is a format function, not a method, taking the value and a second parameter describing how to lay it out. The second puts that same description inside the braces of a format string, after a colon, for the string format method you already know. Both round rather than truncate, and both hand back a new string while the number itself is untouched.

## Files

- [`starter/raw-floats-are-not-fit-to-show-a-human.txt`](starter/raw-floats-are-not-fit-to-show-a-human.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/raw-floats-are-not-fit-to-show-a-human.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
