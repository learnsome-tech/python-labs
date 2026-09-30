# m18l03-04 · Activating it on Windows

**Lesson:** [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) (lesson 18.3, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can create a virtual environment for a project, activate and deactivate it on your own operating system, explain what activation does to PATH, and check from inside Python whether you are in one.

In the lesson: On Windows the idea is identical and the paths are different. Create the environment with the py launcher and the same venv module. Inside the environment folder, the commands live in Scripts with a capital S rather than bin, and the packages live in Lib with a capital L. In PowerShell you run the Activate dot p s one script; in the old Command Prompt you run activate dot bat. There is no source command and none is needed. If PowerShell refuses to run the script and mentions an execution policy, that is Windows blocking unsigned scripts rather than anything wrong with Python; the Command Prompt version will work in the meantime. Leaving is the same word everywhere: deactivate.

## Files

- [`starter/activating-it-on-windows.txt`](starter/activating-it-on-windows.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/activating-it-on-windows.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
