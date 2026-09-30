# m06l06-05 · The names on each side are independent

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: With parameter passing, the parameter name x in the function f does not need to match the name of the actual parameter in main. The definition of f could just as well have been the two lines on screen, taking a parameter called whatever. Main would not change at all, and the program would print three exactly as before. This follows from what we said about arguments earlier: only the value is passed, never the name. So choose the name that reads best inside the function you are writing, and leave the caller free to choose the name that reads best there. That independence is precisely what makes a function usable by someone who has never read its body.

## Files

- [`starter/the-names-on-each-side-are-independent.py`](starter/the-names-on-each-side-are-independent.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-names-on-each-side-are-independent.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l06-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
