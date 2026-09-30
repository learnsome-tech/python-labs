# m15l03-07 · Output that cannot come from a static page

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: One more step: a script whose output cannot come from a static page. Try it, then press refresh and look again. Two ideas here. A library module, time, is imported and used to build a string for the current date and time. And the page is made as in the earlier template program, embedding dynamic data in a literal format string: notice the name in braces, and the format method at the bottom. This time the contents are printed rather than saved, because the server is listening.

## Files

- [`starter/now.cgi`](starter/now.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/now.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 6: the time module supplies the current date and time
   - Line 12: a name in braces, as in the template programs

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
