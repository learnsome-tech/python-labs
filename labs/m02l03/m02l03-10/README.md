# m02l03-10 · Verifying, and what each answer should say

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: Finally, the check. Ask python three for its version and you should get one line, beginning with the word Python and carrying the version you just installed. Then ask pip, and notice the habit on screen: run it through python three with the module flag, because the answer then names the interpreter it belongs to, and a pip that belongs to a different Python is a classic afternoon lost. Its line must end with the version from the first answer. Then start Idle. A window should open. If you get a missing module line instead, go back for the Idle and Tk packages. Three answers that agree, and Linux is ready.

## Files

- [`starter/verifying-and-what-each-answer-should-say.txt`](starter/verifying-and-what-each-answer-should-say.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/verifying-and-what-each-answer-should-say.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
