# m03l01-04 · tellStory: the shape of the whole job

**Lesson:** [A Sample Program, Explained](https://learnsome.tech/learn/python-course/m03l01) (lesson 3.1, module 3: Meet Idle And The Shell) · Pro  
**Check:** Read along

## Goal

You can read madlib.py from top to bottom and say what each line contributes, from the shebang and the documentation string to the format string, the two definitions and the two calls that start everything.

In the lesson: This line is the heading of a definition. The word def is short for definition of a function, and it makes the name tellStory a short way to refer to the sequence of statements that start indented beneath it and continue to the end of the block. Nothing runs yet. Inside, the equal sign is another assignment statement: the name userPicks is associated with a new empty dictionary, created by the Python code dict followed by empty parentheses. The next three lines call addPick, a function defined further down the file, whose job is to add one more definition to a dictionary based on the user's input. Together they add definitions for each of the three words animal, food and city. Then the name story is assigned a string formed by substituting into storyFormat using definitions from the dictionary, giving the user's customised story. And the last line is where all the work becomes visible: it prints that story to the screen.

## Files

- [`starter/madlib.py`](starter/madlib.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: short for definition
   - Lines 2: a new empty dictionary
   - Lines 3–5: three words
   - Lines 6–7: becomes visible
3. Notes from the lesson:
   - Line 1: def, a name, parentheses, a colon: the heading of a definition
   - Line 6: Substitute into storyFormat using the pairs held in userPicks

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
