# m15l03-11 · The boilerplate you always copy

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: The end of the file is boilerplate you can always copy. fileToStr is the function you have seen before. Then comes the wrapper for main. The print function that tells the server HTML is coming sits here, so main itself only builds and prints the markup. And keep that final block, which catches any execution error and generates trace information you can read in your browser. Writing such code in general is not covered here, but copy it. Leave it out and you lose all feedback. Note that this block calls the cgi module, which was removed from the standard library in Python three point thirteen, so on a current interpreter you would print the trace yourself with the traceback module instead.

## Files

- [`starter/adder.cgi`](starter/adder.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/adder.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 9: keep this: it turns crashes into readable browser output

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
