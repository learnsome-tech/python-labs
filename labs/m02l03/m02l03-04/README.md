# m02l03-04 · Why Idle is a separate package

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: Here is the reasoning behind that split, because it explains an otherwise mysterious symptom. Most Linux machines in the world are servers with no screen attached. Tk is a graphical toolkit that needs graphics libraries, and on a server that is waste. So distributions ship Tk and Idle as packages of their own. The result is the pair of messages on screen. Asking Python to run the idle library says there is no such module. Importing the Tk binding says the same about tkinter. Neither means your Python is damaged, and reinstalling will not help. Install the Idle package and the Tk package, and both messages go away.

## Files

- [`starter/why-idle-is-a-separate-package.txt`](starter/why-idle-is-a-separate-package.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/why-idle-is-a-separate-package.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
