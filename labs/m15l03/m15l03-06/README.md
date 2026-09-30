# m15l03-06 · The same idea, but sending HTML

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: Now a variation that sends an already determined HTML page. Two changes matter. The first print function now declares that the output will be HTML, and that is the boilerplate line for your own scripts. The remaining print function carries the markup for a page, and the enclosing triple quotes work for a multi line string. As anything but an illustration this script is useless: the same text in a file would do. But the page is now produced by a running program.

## Files

- [`starter/hellohtml.cgi`](starter/hellohtml.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/hellohtml.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 3: boilerplate: the rest of the output is html
   - Line 5: triple quotes carry a multi line string

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
