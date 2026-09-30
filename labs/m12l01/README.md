# m12l01 · Files: Writing And Reading

Module 12: Files And Chapter Review · lesson 12.1 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m12l01)

**Goal:** You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m12l01-02](m12l01-02/) | Three lines that create a file | Graded |
| [m12l01-04](m12l01-04/) | Why close is essential | Graded |
| [m12l01-05](m12l01-05/) | write adds nothing you did not ask for | Graded |
| [m12l01-06](m12l01-06/) | Say it with a newline code | Graded |
| [m12l01-07](m12l01-07/) | Reading a whole file back | Read along |
| [m12l01-08](m12l01-08/) | The string that comes back | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### PrintUpper Exercise

1. printUpper.py: read the sample2 text file and print its contents in upper case.
2. Make it work for any contents: do not assume the string nextFile.py wrote.
3. fileUpper.py: prompt for a file name, then print that file in upper case.
4. copyFileUpper.py: write the upper case text to a new file, named by prepending UPPER.

> **Hint:** Save these in the same directory as your sample text files. The new file name is just a string, so it can be built from the old one with concatenation.

### Mad Lib File Exercise

1. Copy madlib2.py to madlib3.py and change only the main function.
2. Prompt the user for the name of a file holding a mad lib format string.
3. Read that file and pass the contents to tellStory as the story format.
4. Write your own story into myMadlib.txt, then test with jungle.txt and with it.

> **Hint:** The story file holds the format string as plain text, with no quotes around it. You are only a user of tellStory here; leave it and the functions it calls alone.

## Check yourself

- What happens to the old contents of a file you open with the write mode?
- Why can a program that writes to a file leave no file behind at all?
- How does the write method differ from the print function?
- What does the read method return, and how much of the file does it give you?
- Name the three separate ideas: the file name, the file object and what else?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
