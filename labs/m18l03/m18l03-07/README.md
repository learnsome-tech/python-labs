# m18l03-07 · One per project, and never committed

**Lesson:** [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) (lesson 18.3, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can create a virtual environment for a project, activate and deactivate it on your own operating system, explain what activation does to PATH, and check from inside Python whether you are in one.

In the lesson: Two habits and this lesson is done. First, one environment per project, created inside the project folder, and never shared. It costs almost nothing and it is the whole reason the mechanism exists. Second, the environment folder is never committed and never copied to another machine. It is full of platform specific files, it can be thousands of them, and it is entirely rebuildable in seconds from a list of package names, which is the next lesson. So add it to your gitignore file, next to the compiled cache folders. What you share with another person is the list of what to install, and they build their own environment from it. The transcript at the top shows the check from the previous segment, run inside an active environment, answering true.

## Files

- [`starter/one-per-project-and-never-committed.txt`](starter/one-per-project-and-never-committed.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/one-per-project-and-never-committed.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l03-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
