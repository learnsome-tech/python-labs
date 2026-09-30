# m15l04-12 · A form, in full

**Lesson:** [HTML Forms And Dynamic Programs](https://learnsome.tech/learn/python-course/m15l04) (lesson 15.4, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can read and edit an HTML form, make its field names match the names your CGI script asks for, and recognise the text, submit, radio, checkbox and hidden input tags.

In the lesson: Here is the adder page in full, form and all. A form can only appear inside the body, and input tags only inside the form. The form's own tag carries three attributes, and the only one you ever change is the action attribute, naming the script that will act on the data. Then two text input tags, which have no closing tag. Each carries the name and the value: name identifies the field for your program, value is what starts in the box. Last comes the submit button.

## Files

- [`starter/adder.html`](starter/adder.html): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/adder.html` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–11: the form's own tag
   - Lines 12–16: two text input tags
   - Lines 17–21: the submit button
3. Notes from the lesson:
   - Line 11: the action names the script that will get the data
   - Line 13: name identifies the field; value is what starts in the box

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l04-12` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
