# m02l05-12 · Symptom six: works in Idle, fails in the terminal

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Sixth symptom, and the sneakiest: the file runs perfectly in Idle and fails from the terminal, saying Python cannot open your file. Nothing is wrong with the file or with Python. Idle runs a program from the folder that file lives in, while your terminal is somewhere else, usually your home folder. Python looked where it was standing and found nothing. The fix is to change directory into the folder that holds the file, list the folder to check the name, and run it again. Or hand over the whole path, and read the path in the message.

## Files

- [`starter/symptom-six-works-in-idle-fails-in-the-termi.txt`](starter/symptom-six-works-in-idle-fails-in-the-termi.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/symptom-six-works-in-idle-fails-in-the-termi.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
