# m15l04-15 · Optional: check boxes and a hidden field

**Lesson:** [HTML Forms And Dynamic Programs](https://learnsome.tech/learn/python-course/m15l04) (lesson 15.4, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can read and edit an HTML form, make its field names match the names your CGI script asks for, and recognise the text, submit, radio, checkbox and hidden input tags.

In the lesson: Check boxes allow several selections at once from one group. The syntax matches the radio buttons, with distinct values, but you read them differently: the get list method returns a list of the values checked, so sausage, onions and extra cheese gives three strings. Then the hidden field on the last line. Nothing about it is visible to the user; its input goes into the next run of the script. Each call of a CGI program is independent, so this is how the script knows a form came before it.

## Files

- [`starter/pizzaOrderTemplate1.html`](starter/pizzaOrderTemplate1.html): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pizzaOrderTemplate1.html` alongside the lesson.
2. Notes from the lesson:
   - Line 2: checkbox: several may be selected at once
   - Line 14: hidden: input to the next script, invisible to the user

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l04-15` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
