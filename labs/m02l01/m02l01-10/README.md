# m02l01-10 · Python was not found: the commonest failure

**Lesson:** [Installing Python On Windows](https://learnsome.tech/learn/python-course/m02l01) (lesson 2.1, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can install Python on Windows from python.org with the PATH box ticked, verify it in a fresh command prompt with both py and python, and recognise and fix the Microsoft Store stub message.

In the lesson: Here is the message that stops more first installs than anything else. You type python, and Windows replies that Python was not found, and offers to install it from the Microsoft Store. Python is not talking to you there. Windows ships a tiny stub program, also called python dot exe, which lives in a folder called WindowsApps and does nothing but advertise the Store. That folder sits early on your PATH, so if the real Python was never added to PATH, the stub is the only thing with that name and it answers. The giveaway is that py still starts Python quite happily.

## Files

- [`starter/python-was-not-found-the-commonest-failure.txt`](starter/python-was-not-found-the-commonest-failure.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/python-was-not-found-the-commonest-failure.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
