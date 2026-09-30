# m11l07-03 · The label, and reading what was typed

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: One line is missing between the screens, because it is too wide to show: a Text object thirty units above the box, holding the string Name, drawn immediately as a static label. An Entry carries no label of its own, so you always add one. Now the program calls getMouse, and the only reason is to know that the user has finished typing; where the click lands does not matter. Once it is processed, getText hands back the contents of the Entry as a string. Then two greetings are built by concatenation and drawn at a third and at two thirds of the width. Finally promptClose takes the instructions object and reuses it for the closing message.

## Files

- [`starter/greet.py`](starter/greet.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/greet.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: the program calls getMouse
   - Lines 2–3: getText hands back the contents
   - Lines 4–9: two greetings are built by concatenation
   - Lines 10–13: promptClose takes the instructions object

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
