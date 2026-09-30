# m18l03-02 · Making one, and what is inside it

**Lesson:** [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) (lesson 18.3, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can create a virtual environment for a project, activate and deactivate it on your own operating system, explain what activation does to PATH, and check from inside Python whether you are in one.

In the lesson: You make one with the venv module, run by name with the dash m switch you met last lesson. Give it the folder to create. By convention that folder is called dot venv: it is short, the leading dot hides it from ordinary listings, and every editor recognises it. Look inside. There is a bin folder holding a python command and a pip command for this environment. There is a lib folder whose site-packages is where installed packages will land, and at the start it holds only pip itself. And there is a small text file, pyvenv dot cfg, recording which real Python this environment was built from. Notice what is not there: the standard library is not copied. The environment points back at your installed Python for that, so it stays tiny.

## Files

- [`starter/making-one-and-what-is-inside-it.txt`](starter/making-one-and-what-is-inside-it.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/making-one-and-what-is-inside-it.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
