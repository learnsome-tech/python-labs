# m15l04-10 · An output template in raw markup

**Lesson:** [HTML Forms And Dynamic Programs](https://learnsome.tech/learn/python-course/m15l04) (lesson 15.4, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can read and edit an HTML form, make its field names match the names your CGI script asks for, and recognise the text, submit, radio, checkbox and hidden input tags.

In the lesson: For the exercises the expected pattern is an output page template: a static file that later gets modified by the string format operation inside your program. Here is the template for the adder programs, used by both the local version and the server script. Text outside tags is what you would see if this page were displayed directly, including the names in braces. The programs never display it directly; they use it as a format string, so substitutions happen first.

## Files

- [`starter/additionTemplate.html`](starter/additionTemplate.html): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/additionTemplate.html` alongside the lesson.
2. Notes from the lesson:
   - Line 12: three names in braces, filled by the format method

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l04-10` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
