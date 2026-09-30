# m12l01-05 · write adds nothing you did not ask for

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Graded

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: Let us do the same thing a step at a time in the shell, so we can see what happens. First open the file for writing. Then write the first string: the shell answers with the number of characters written, twenty two characters, which is a detail the write method reports and a program normally ignores. Write the second string, close it, and read it straight back. The two strings have run together on a single line. The write method is not like the print function. It adds nothing to the file except exactly the data you tell it to write. If you want a line break, you have to say so.

## Files

- [`starter/sample2.txt`](starter/sample2.txt)
- [`starter/shell-write-adds-nothing-you-did-not-ask-for.py`](starter/shell-write-adds-nothing-you-did-not-ask-for.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m12l01/m12l01-05/starter`
2. Read `shell-write-adds-nothing-you-did-not-ask-for.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   outFile = open('sample2.txt', 'w')
   outFile.write('My second output file!')
   outFile.write('Write some more.')
   outFile.close()
   print(open('sample2.txt').read())
   ```
4. Run it: `python3 -i < shell-write-adds-nothing-you-did-not-ask-for.py`.
5. Check it from the repository root: `./check m12l01-05`.

## Expected output

```text
22
16
My second output file!Write some more.
```

## How to check

`./check m12l01-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-write-adds-nothing-you-did-not-ask-for.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
