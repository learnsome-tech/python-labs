# m07l02-05 · The general form, and back to the mad lib

**Lesson:** [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) (lesson 7.2, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

In the lesson: Here is that last line, shifted left so it fits on screen. The format string, the format method and the unpacked dictionary are one expression inside the print call, with no named variables at all. You are free to use either coding approach. In general the syntax is on the second line: a format string, a period, format, and inside the parentheses two stars followed by a dictionary. It returns a new formatted string. The format string holds dictionary keys in braces wherever you want the values substituted, and those key names must follow the rules for legal identifiers. With that, we have accounted for everything in the very first sample program of this course, the mad lib. Look at it again; it should make much more sense now.

## Files

- [`starter/the-general-form-and-back-to-the-mad-lib.py`](starter/the-general-form-and-back-to-the-mad-lib.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-general-form-and-back-to-the-mad-lib.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
