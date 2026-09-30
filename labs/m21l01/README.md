# m21l01 · Paths And Files The Modern Way

Module 21: Files, Formats And The Standard Library · lesson 21.1 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m21l01)

**Goal:** You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m21l01-01](m21l01-01/) | The close line you will one day forget | Read along |
| [m21l01-02](m21l01-02/) | The with statement closes the file for you | Graded |
| [m21l01-03](m21l01-03/) | It closes even when the block goes wrong | Graded |
| [m21l01-04](m21l01-04/) | All at once, or one line at a time | Graded |
| [m21l01-05](m21l01-05/) | Append instead of destroying what is there | Graded |
| [m21l01-06](m21l01-06/) | Text, bytes, and what an encoding is | Graded |
| [m21l01-07](m21l01-07/) | Paths as objects, not glued together strings | Graded |
| [m21l01-08](m21l01-08/) | Why glued path strings break on other machines | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### A folder report

1. Write folderReport.py using pathlib and with statements only, no close calls.
2. Write three small text files into a folder your program creates.
3. Loop over the folder with iterdir and print each name and its line count.
4. Append one summary line to a report file each time the program runs.

> **Hint:** Count lines by looping over the open file and adding one each time, so a huge file would still work. The append mode is the letter a.

## Check yourself

- What exactly does the with statement do at the end of its block?
- Why can an error in the middle of a program leave an empty file behind?
- When should you loop over a file rather than call the read method?
- What does an encoding decide, and which one should you name?
- Name two things that go wrong when you glue a path together as a string.

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
