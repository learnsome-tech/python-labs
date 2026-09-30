# m03l01-05 · addPick: asking the user one question

**Lesson:** [A Sample Program, Explained](https://learnsome.tech/learn/python-course/m03l01) (lesson 3.1, module 3: Meet Idle And The Shell) · Pro  
**Check:** Read along

## Goal

You can read madlib.py from top to bottom and say what each line contributes, from the shebang and the documentation string to the format string, the two definitions and the two calls that start everything.

In the lesson: Here is addPick itself. This line is the heading of a definition, giving the name addPick to the statements indented below. The name is followed by two words in parentheses, cue and dictionary. These two are associated with an actual cue word and dictionary given when this definition is invoked, which is what those three lines in tellStory did. Next comes a documentation comment for the definition. The plus sign then concatenates parts of the string assigned to the name prompt, placing the current value of cue into it. On the next line, the right hand side of the equal sign causes an interaction with the user: the prompt is printed to the screen, and the computer waits for the user to enter a line of text. That text becomes a string, tidied by the strip method, and is assigned to response. Finally, the left-hand side of the last equal sign refers to the definition of the cue word in the dictionary, so that definition becomes the response the user typed.

## Files

- [`starter/madlib.py`](starter/madlib.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/madlib.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: two words in parentheses
   - Lines 2–4: a documentation comment
   - Lines 5: The plus sign
   - Lines 6: waits for the user
   - Lines 7: of the last equal sign
3. Notes from the lesson:
   - Line 1: cue and dictionary stand for whatever is supplied at the call
   - Line 6: input prints the prompt, waits, and hands back the typed line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
