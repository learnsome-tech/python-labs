# m17l04-07 · The seven commands worth memorising

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Read along

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: Seven commands will carry you a long way, and they are on screen. The pair to keep straight is next and step: both run one line, but at a line containing a call, next runs the whole call and stops after it, while step goes inside and stops on the call's first line. Use next until you reach something you suspect, then step into it. Two habits will save you confusion. Always use p to look at a variable, because a bare name might collide with a command name; the variable called n is the classic victim. And pressing enter on its own repeats your last command, which makes stepping through a loop quick.

## Files

- [`starter/the-seven-commands-worth-memorising.txt`](starter/the-seven-commands-worth-memorising.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-seven-commands-worth-memorising.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m17l04-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
