# m02l04-01 · How a command name becomes a program

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: When you type python three at a prompt and press Enter, the shell does not know what that is. It is a name, not a program. To turn the name into a program on disk, the shell reads an environment variable called PATH, which holds a list of folders. It tries the first folder, looks for a file with your name in it, and if there is one, runs it and stops looking. If not, it tries the next folder, and the next. If none of them has it, you get the message command not found. That is the whole mechanism, and almost every install problem in this module follows from it: order matters, and the first match wins.

## Files

- [`starter/how-a-command-name-becomes-a-program.py`](starter/how-a-command-name-becomes-a-program.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/how-a-command-name-becomes-a-program.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-01` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
