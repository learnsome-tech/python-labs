# m15l02-05 · The page becomes a format string

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: The second version changes very little, and the changed parts are marked in the file. In the page text, the fixed greeting has become a name in braces, so the string is now a format string, which is why it was renamed to the more appropriate pageTemplate. The main function gains two lines. It asks for a name at the keyboard, and then this single line uses the format method with the locals function to incorporate that name into the contents of the page, before saving it and displaying it. Run it, type your name, and your browser greets you.

## Files

- [`starter/helloWeb2.py`](starter/helloWeb2.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/helloWeb2.py` alongside the lesson.
2. Notes from the lesson:
   - Line 10: the only edit to the markup: a name in braces
   - Line 16: format fills the braces from the local variables

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
