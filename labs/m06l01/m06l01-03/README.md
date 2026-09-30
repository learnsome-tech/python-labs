# m06l01-03 · The whole song, written out

**Lesson:** [Defining Your First Function](https://learnsome.tech/learn/python-course/m06l01) (lesson 6.1, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function definition with def, an indented body and a call, and explain why defining a function is not the same as running it.

In the lesson: Here is the song as a program, in the example file birthday one. Four print calls, one line of the song each, with Emily's name in the third. Read it, and run it. You get exactly what you asked for. But notice what is unsatisfying about it. If you wanted the song twice, you would type all four lines again. If you wanted it for Andre, you would copy the block and change one word. This program has no name for the idea of the song; it only has the song itself. Giving that idea a name is what a function definition does, and that is where we go next.

## Files

- [`starter/birthday1.py`](starter/birthday1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-03/starter`
2. Read `birthday1.py`.
3. Run it: `python3 birthday1.py`.
4. Check it from the repository root: `./check m06l01-03`.

## Expected output

```text
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
```

## How to check

`./check m06l01-03` copies `starter/` into a scratch directory and runs `python3 birthday1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
