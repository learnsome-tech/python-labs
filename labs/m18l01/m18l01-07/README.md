# m18l01-07 · Where Python looks, in order

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: When Python cannot find a module, it is worth knowing where it looked. There is a list of directories called sys dot path, and Python tries them in order, taking the first match. On screen is a real one, shortened. Notice the order. The folder holding the program you ran comes first. Then the standard library that shipped with Python. Last comes site-packages, the folder where anything you install yourself lands. So your own files are searched before the standard library, not after. That ordering is deliberate, it is occasionally useful, and it is the cause of one very specific beginner disaster, which is next.

## Files

- [`starter/where-python-looks-in-order.txt`](starter/where-python-looks-in-order.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/where-python-looks-in-order.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l01-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
