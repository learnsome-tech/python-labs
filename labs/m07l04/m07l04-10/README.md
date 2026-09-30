# m07l04-10 · Playing computer on the numbering loop

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: Here is the discipline that stops loops being magic. You keep a table with one row for every line that gets executed, and in each row you write which line ran and what it changed. Because the heading and the body run again and again, the same line numbers appear over and over, and the line number in a row is often not one more than the row above. Watch the repeating trio. Line four prints, line five prepares for the next pass, then line three moves on to the next element. After the last colour, line three finds nothing left and the loop ends. The final value of number is never printed, and that is fine. Every pass is on screen, so read the first column downwards and check each change for yourself.

## Files

- [`starter/playing-computer-on-the-numbering-loop.txt`](starter/playing-computer-on-the-numbering-loop.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/playing-computer-on-the-numbering-loop.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l04-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
