# m11l02-09 · getMouse returns where you clicked

**Lesson:** [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) (lesson 11.2, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can write a complete graphics program with the standard starting lines, build a picture from circles, lines, ovals, text and polygons, take input from mouse clicks, and close the window from inside the picture.

In the lesson: After the prompt, the program looks for a response. The get mouse method, called with no parameters, waits for you to click inside the window, and then returns the point where the mouse was clicked. In the face program we ignored that value; here it is the whole point. Three clicks are waited for in turn, each remembered in its own variable, and each point is drawn so you get feedback. Then the three points are gathered into a list.

## Files

- [`starter/triangle.py`](starter/triangle.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/triangle.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: returns the point
   - Lines 4–7: Three clicks
   - Lines 8: into a list

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l02-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
