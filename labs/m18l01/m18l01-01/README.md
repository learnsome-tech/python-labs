# m18l01-01 · A module is just a file of Python

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: You have been writing one file at a time. Real programs are several files, and the moment there are two of them, one has to reach into the other. Python's answer is the module, and a module is nothing more exotic than a file of Python code. Its module name is the file name with the dot py ending taken off. When you write the word import followed by a name, Python finds that file, runs it, and gives you a name you can use to reach everything inside. You have already done this: the graphics module was a file sitting beside your program. The standard library is hundreds of such files, already on your machine. On screen are the three forms of the import statement, and we will take them one at a time.

## Files

- [`starter/a-module-is-just-a-file-of-python.py`](starter/a-module-is-just-a-file-of-python.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-module-is-just-a-file-of-python.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l01-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
