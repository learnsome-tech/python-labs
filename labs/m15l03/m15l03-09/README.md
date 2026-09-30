# m15l03-09 · Reading the browser's data

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: Here is the beginning of the adder script. To handle the input we import the cgi module. The body of the code is in a main function, and its first line is a standard line for you to copy, setting up an object called form that holds the data from the browser's request. The two lines after it carry comments too wide for this screen. They use the pattern: a variable, assigned form dot getfirst, with a name from the form and a default, used if the browser sent nothing. One warning before you copy any of it: the cgi module was removed from the standard library in Python three point thirteen, so a current interpreter cannot import it. Treat this screen as the historical form, and read the form data yourself with the URL lib parse module, or with the third party multipart package.

## Files

- [`starter/adder.cgi`](starter/adder.cgi): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/adder.cgi` alongside the lesson.
2. Notes from the lesson:
   - Line 3: the cgi module handles the incoming form data
   - Line 6: standard line: an object holding the form data

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l03-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
