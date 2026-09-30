# m02l05-07 · Symptom two: install it from the Microsoft Store

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Read along

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Second symptom, and this one is Windows only. You type python and get a whole English sentence back, saying Python was not found and offering to install it from the Microsoft Store. That is not Python failing to start. It is a stub program of the same name, shipped by Windows, sitting in a folder early on your PATH, whose only job is to sell you the Store version. It answers because the real Python is not ahead of it. The fix is to switch that alias off in settings, or to re-run the installer with the environment variables box ticked.

## Files

- [`starter/symptom-two-install-it-from-the-microsoft-st.txt`](starter/symptom-two-install-it-from-the-microsoft-st.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/symptom-two-install-it-from-the-microsoft-st.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
