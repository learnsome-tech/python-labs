# m22l04-06 · Installing your own package

**Lesson:** [Shipping: scripts, entry points and git](https://learnsome.tech/learn/python-course/m22l04) (lesson 22.4, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can turn a script into a command you can run from anywhere, describe your project in a pyproject file, build and install it, and keep its history in git.

In the lesson: Now install it, into a virtual environment as always. The dot means install the project in this folder, and the e flag means editable: pip links to your source rather than copying it, so the code you edit is the code that runs, which is what you want while you are working on it. Here are the last lines of what pip prints. Notice it installed rich as well, because your project said it depends on it, and nobody had to remember that. And now the payoff on the final line: the word wordcount, on its own, from anywhere in that environment, is a command. Your program has a name.

## Files

- [`starter/terminal`](starter/terminal): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/terminal` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
