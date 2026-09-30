# m15l02-03 · Two functions you will reuse constantly

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Read along

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: The program encapsulates two basic operations into these last two functions, and you will use them over and over. The first, strToFile, has nothing new in it: it puts the text you give it in a file with the name you give it. The second, browseLocal, does more. It takes some text, presumably a web page, puts it in a file, and displays that file in your default browser. Its final line, too wide for this screen, calls the open function from the webbrowser module on the absolute path of the file. Since the page is generated for one immediate viewing, the same throwaway name is reused, as the default of a keyword parameter.

## Files

- [`starter/helloWeb1.py`](starter/helloWeb1.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/helloWeb1.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: nothing new here: text in, file out
   - Line 7: a keyword parameter gives the throwaway file its name

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m15l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
