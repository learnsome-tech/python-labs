# m18l03-05 · All activation does is change PATH

**Lesson:** [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) (lesson 18.3, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can create a virtual environment for a project, activate and deactivate it on your own operating system, explain what activation does to PATH, and check from inside Python whether you are in one.

In the lesson: It is worth knowing that activation is not clever. Your shell finds commands by walking a list of folders called PATH, in order, and taking the first match. All the activate script does is put the environment's bin folder at the front of that list, set a variable recording which environment is live, and add the name to your prompt. That is the whole trick. Because it is only PATH, you can skip activation entirely and call the environment's Python by its full path, which is exactly what editors and scheduled jobs do. And because it is only PATH, nothing is permanently changed: a new terminal window knows nothing about it.

## Files

- [`starter/all-activation-does-is-change-path.txt`](starter/all-activation-does-is-change-path.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/all-activation-does-is-change-path.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
