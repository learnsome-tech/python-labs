# m06l01-05 · The Shell remembers, and parentheses matter

**Lesson:** [Defining Your First Function](https://learnsome.tech/learn/python-course/m06l01) (lesson 6.1, module 6: Functions) · Pro  
**Check:** Read along

## Goal

You can write a function definition with def, an indented body and a call, and explain why defining a function is not the same as running it.

In the lesson: After Idle has finished running a program, its Shell still remembers the function definitions from that program. So move to the Shell, not the editor, and type the function name on its own. The result probably surprises you. When you give the Shell an identifier, it tells you the value of that identifier, and without parentheses the value is the function code itself, reported with a location in memory. Now type the name again, with parentheses added. This time the song appears. The parentheses tell Python to execute the named function rather than merely refer to it. Python goes back, looks up the definition, and only then runs the code inside. The term for that action is a function call, or an invocation. In a call there is no def: there is the function name, followed by parentheses.

## Files

- [`starter/shell-the-shell-remembers-and-parentheses-matter.py`](starter/shell-the-shell-remembers-and-parentheses-matter.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-the-shell-remembers-and-parentheses-matter.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
