# m15l02-09 · Input, then processing, then display

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: The common case is more interesting: input is processed into a result, and the result, often with some of the original input, is embedded in the output page. This program adds two numbers. Only these few lines are new, because the rest is the standard functions reused. Note three things. All input arrives as strings, so we convert the digit strings to integers before the arithmetic. A real, if simple, result is calculated and used in the page. And the input is obtained in a distinct place from where it is processed, so that when it later comes from a web form, only the obtaining changes.

## Files

- [`starter/additionWeb.py`](starter/additionWeb.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/additionWeb.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: all form data is text, so convert before calculating
   - Line 9: obtaining the input is kept apart from processing it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l02-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
