# m15l03-10 · Processing, unchanged from the local version

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: Here is the second half of main, and the processing function. The first line is the twin of the line above it on the last screen, taking the value the browser sent under the name y. Then main calls processInput with both strings and prints what comes back. And processInput is exactly the same as in the addition program of the last module, so we know it works. That is the payoff for separating obtaining input from processing it. Output is easier here too: no file to save, just print it.

## Files

- [`starter/adder.cgi`](starter/adder.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/adder.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 1: the twin of the line above it, for the name y
   - Line 5: identical to the version in additionWeb.py

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
