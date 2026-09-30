# m07l06 · Playing Computer

Module 7: Dictionaries And Loops · lesson 7.6 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m07l06)

**Goal:** You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l06-02](m07l06-02/) | A very natural mistake | Graded |
| [m07l06-03](m07l06-03/) | The trace that catches the culprit | Read along |
| [m07l06-04](m07l06-04/) | Tracing functions that return values | Graded |
| [m07l06-05](m07l06-05/) | The table for a call inside a call | Read along |
| [m07l06-07](m07l06-07/) | Code you have not been told about | Read along |
| [m07l06-09](m07l06-09/) | Code with a mistake in it | Read along |
| [m07l06-11](m07l06-11/) | One function, called twice in one line | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Play Computer sumList Exercise

1. Open playComputerSumStub.rtf outside Idle and save it at once as playComputerSum.rtf.
2. Play computer on the call sumList([5, 2, 4, 7]); nums gets no column, since it never changes.
3. One row per line executed, using the line numbers shown beside the code in the tutorial.
4. Your last row is an execution of line 6, with the comment: return 18.

> **Hint:** If a value is unchanged on a row, leave the cell blank: the current value is the last one recorded above.

### Play Computer Odd Loop Exercise

1. Work in a word processor, starting from playComputerStub.rtf, and save it as playComputer.rtf.
2. Play computer on the code on the previous screen, with columns for line, x, y and n.
3. Reality check: 31 is printed when line 6 finally executes.

> **Hint:** The first row is line 1 setting x, and n has no value at all until the loop heading first runs.

### Play Computer Error Exercise

1. Add to playComputer.rtf, with columns for line, n and prod; row one sets nums to [5, 4, 6].
2. Play computer on product([5, 4, 6]) only until a wrong number is produced, then stop.
3. End with a comment saying how the error is now visible.
4. Then copy numProductWrong.py to numProduct.py and fix the new file, saving it again.

> **Hint:** A major use of playing computer is finding the exact step where the value you expected turns into the value you did not.

### Play Computer Functions Exercise

1. Add a third table to playComputer.rtf, with columns for line, x and a comment.
2. First row covers lines 1 to 2: remember the definition of f. The second row is line 3.
3. Reality check: 70 is printed.

> **Hint:** Look again at the table for the m example: the same line is revisited, with the rows for the function call in between.

## Check yourself

- What is a logical error, and why can running the program fail to reveal its cause?
- In the wrong numbering loop, which line undoes the work of the increment, and why?
- What does a dash mean in a playing computer table, and what does a blank cell mean?
- Why does the same line number appear several times in a trace of nested function calls?
- When tracing a program you suspect is wrong, when should you stop extending the table?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
