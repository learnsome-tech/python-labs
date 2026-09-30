# m20l04-04 · Why every class needs at least a repr

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Read along

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: If you define neither, Python still has to show your object somehow, and what it falls back on is the class name and the address of the object in memory. That address tells you nothing about the data, and it is different on every run, so it is useless in a bug report and useless when you are comparing two objects by eye. And you will meet it constantly: in the shell, in a printed list, in a debugger, in a log file, inside a failing test's message. So the advice is firm. If you write only one dunder method for a class, write dunder repr. Dunder str is a nicety for output aimed at users; without a repr you are working blind.

## Files

- [`starter/why-every-class-needs-at-least-a-repr.txt`](starter/why-every-class-needs-at-least-a-repr.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/why-every-class-needs-at-least-a-repr.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m20l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
