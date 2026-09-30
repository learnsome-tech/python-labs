# m02l04-07 · System Python, and why you leave it alone

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: One Python on your machine is not yours: the system Python. On a Mac it belongs to Apple's developer tools; on Linux it is the interpreter the package manager itself runs on. It is old on purpose, and it changes when the operating system changes, not when you want it to. Two rules follow. Do not build your own project on it, and do not install packages into it, because the tools that depend on it can break. Recent versions defend themselves: pip refuses outright, with a message about an externally managed environment, and points you at a virtual environment instead. That refusal is a feature, not a fault.

## Files

- [`starter/system-python-and-why-you-leave-it-alone.txt`](starter/system-python-and-why-you-leave-it-alone.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/system-python-and-why-you-leave-it-alone.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
