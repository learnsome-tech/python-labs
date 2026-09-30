# m13l04-03 · A bouncing ball needs a test every step

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Read along

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: The rest of this section is graphical. Run the example program bounce one dot py and you get a red ball moving obliquely and bouncing off the edges, starting from a random place each time. After the program has run you can call the bounce ball function again from the shell with your own step sizes; keep the magnitudes under ten. Earlier animations were completely scripted, but here the direction changes at every bounce. The central animation step moves the shape. When the ball reaches the left wall the horizontal part of the motion reverses, so the horizontal step changes sign, while the vertical step is untouched. That happens only sometimes, and only sometimes is the signal for an if statement.

## Files

- [`starter/a-bouncing-ball-needs-a-test-every-step.py`](starter/a-bouncing-ball-needs-a-test-every-step.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/a-bouncing-ball-needs-a-test-every-step.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m13l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
