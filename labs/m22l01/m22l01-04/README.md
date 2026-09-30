# m22l01-04 · Arrange, act, assert

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: Every test has the same three part shape, and naming it makes writing them mechanical. Arrange: build whatever data the test needs. Act: call the one thing you are testing. Assert: say what must now be true. In the examples we just saw, the arranging and the acting were short enough to sit on the same line as the assertion, and for a function this simple that is fine. Two rules of thumb go with the shape. Test one behaviour per function, so a failure tells you exactly what broke. And give each test a name that describes that behaviour, because when it fails at half past four on a Friday the name is the first thing you will read.

## Files

- [`starter/arrange-act-assert.py`](starter/arrange-act-assert.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/arrange-act-assert.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
