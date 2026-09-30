# m15l03-05 · The simplest possible script

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: The simplest case is a script with no input, generating plain text rather than HTML. The top line tells the operating system that this is a Python three program and where to find the interpreter. That location matters on a Unix derived server, including any Mac; on Windows only the distinction between Python two and three matters. Keep the line and you have one less thing to worry about later. Then the first print function tells the server that the rest of the output is plain text, and that rest becomes the document, verbatim.

## Files

- [`starter/hellotxt.cgi`](starter/hellotxt.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/hellotxt.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 1: tells the operating system which interpreter to use
   - Line 4: declares to the server that plain text follows

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
