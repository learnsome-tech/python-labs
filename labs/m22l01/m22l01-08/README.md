# m22l01-08 · How pytest finds your tests

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: Run it without the quiet flag and you can see the discovery happen. Pytest reports the platform and the versions, then the root directory it started from, then the number of items it collected, then a line per file. Collection follows three rules worth memorising. Files must be named test underscore something dot py, or something underscore test dot py. Functions inside them must start with test underscore. And it searches down through subfolders from wherever you ran it, so one command at the top of a project runs everything. You can also name a single file or a single test on the command line when you want to work on just that one.

## Files

- [`starter/terminal`](starter/terminal): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/terminal` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
