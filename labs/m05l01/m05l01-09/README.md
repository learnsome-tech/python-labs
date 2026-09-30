# m05l01-09 · The program documentation string

**Lesson:** [The Idle Editor And Running Programs](https://learnsome.tech/learn/python-course/m05l01) (lesson 5.1, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can open, write, save and run a Python program file in the Idle editor, and you can tell program code apart from Shell text.

In the lesson: The hello program is self evident, and shows how short and direct a program can be. Still, get used to documenting a program. Python has a special feature: if the very beginning of a program is just a quoted string, that string is taken to be the program's documentation string. Here is the example file hello two dot py. Initial documentation usually runs on for several lines, so a multi-line string delimiter is used, the triple quotes. For completeness the program also shows another form of comment, starting with a hash symbol and running to the end of the line. The interpreter ignores it entirely. Run the program and see that neither makes any difference to the result.

## Files

- [`starter/hello2.py`](starter/hello2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-09/starter`
2. Read `hello2.py` the way the lesson builds it:
   - Lines 1–4: documentation string
   - Lines 5–6: another form of comment
3. Notes from the lesson:
   - Line 1: a quoted string at the very beginning is the documentation string
4. Run it: `python3 hello2.py`.
5. Check it from the repository root: `./check m05l01-09`.

## Expected output

```text
Hello world!
```

## How to check

`./check m05l01-09` copies `starter/` into a scratch directory and runs `python3 hello2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
