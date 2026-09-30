# m12l01-08 · The string that comes back

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Graded

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: The same round trip in the shell, so you can see the string itself. We write two lines into a file, close it, then open it for reading. The read method hands back everything in one string, which we hold in contents. Now ask the shell for it plainly and you see the whole file as one value, with the newline codes showing as a backslash and an n inside it. Print it and those codes do their job, and the two lines appear as two lines. Closing a file you have only read from is generally optional. Closing a file you wrote to is not optional at all.

## Files

- [`starter/sample3.txt`](starter/sample3.txt)
- [`starter/shell-the-string-that-comes-back.py`](starter/shell-the-string-that-comes-back.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m12l01/m12l01-08/starter`
2. Read `shell-the-string-that-comes-back.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   outFile = open('sample3.txt', 'w')
   outFile.write('A revised output file!\n')
   outFile.write('Write some more.\n')
   outFile.close()
   inFile = open('sample3.txt', 'r')
   contents = inFile.read()
   contents
   print(contents)
   ```
4. Run it: `python3 -i < shell-the-string-that-comes-back.py`.
5. Check it from the repository root: `./check m12l01-08`.

## Expected output

```text
23
17
'A revised output file!\nWrite some more.\n'
A revised output file!
Write some more.
```

## How to check

`./check m12l01-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-string-that-comes-back.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
