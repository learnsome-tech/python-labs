# m22l04-03 · The same thing on Windows

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: Windows does the same job differently. There is no execute permission to set, so the change mode step has no meaning there. Instead the installer registers the dot py extension and installs a small program called the py launcher. Type py followed by your file and it runs with your newest Python, and py followed by a version number picks a particular one, which is the tidiest way to keep several versions on one machine. The launcher also reads the shebang line, so a file written for a Mac still says something useful on Windows. Double clicking works too, although the window closes the instant the program ends, which is why a console is friendlier.

## Files

- [`starter/the-same-thing-on-windows.txt`](starter/the-same-thing-on-windows.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-same-thing-on-windows.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
