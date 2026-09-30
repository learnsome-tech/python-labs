# m15l02-07 · Reading the template from the file

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: The third version behaves exactly like the second, but is different inside. It does not contain the page template at all. The first new function, fileToStr, returns a string holding the contents of the named file, and it is the inverse of strToFile. Expect to reuse it constantly. In main, one line does both jobs: it reads the template file into a string, and calls the format method on that string with the local variables. Now try something. Open the template, add an extra line of text after the greeting, and save it under the same name. Run again: the output changed without touching the Python.

## Files

- [`starter/helloWeb3.py`](starter/helloWeb3.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/helloWeb3.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: fileToStr is the inverse of strToFile
   - Line 10: read the file, then format it, in one line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
