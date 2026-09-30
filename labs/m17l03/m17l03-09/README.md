# m17l03-09 · What each one usually means in practice

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Knowing the type is one thing; knowing what it usually means in practice is what saves you time. Four of these deserve a warning. An AttributeError complaining about None almost never means None is the problem: it means something further back returned None when you thought it returned an object, often a function with a missing return statement. An IndexError is nearly always an off by one at the end of a sequence. An ImportError usually means the package is not installed in the environment you are actually running. And a FileNotFoundError with a short relative path in it usually means your program is running in a different folder from the one you imagined.

## Files

- [`starter/what-each-one-usually-means-in-practice.txt`](starter/what-each-one-usually-means-in-practice.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-each-one-usually-means-in-practice.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l03-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
