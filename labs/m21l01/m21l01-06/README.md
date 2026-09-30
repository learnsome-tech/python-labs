# m21l01-06 · Text, bytes, and what an encoding is

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: A disk stores numbers, not letters. An encoding is the agreement about which numbers stand for which letters, and utf eight is the answer: it can write every character in every writing system, and it is what you should name every time you open a text file. Watch what happens when the letters change. The word cafe with an accent goes in, followed by a newline. Opened in binary mode, with the mode r b, the file comes back as bytes rather than a string, and because the accented letter takes two bytes, those five characters are six bytes on the disk. Opened as text with the right encoding, you get your string back exactly. Opened with the wrong encoding, Python raises a unicode decode error rather than inventing something plausible, which is a kindness.

## Files

- [`starter/bytesAndText.py`](starter/bytesAndText.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-06/starter`
2. Read `bytesAndText.py`.
3. Run it: `python3 bytesAndText.py`.
4. Check it from the repository root: `./check m21l01-06`.

## Expected output

```text
b'caf\xc3\xa9\n'
<class 'bytes'> 6
'café\n'
ascii cannot read this file
```

## How to check

`./check m21l01-06` copies `starter/` into a scratch directory and runs `python3 bytesAndText.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
