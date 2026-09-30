# m05l03-02 · Greeting built with format

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: The example file hello underscore you three dot py creates and prints the same string as the version with the separator did. The first statement asks for the name, exactly as before. The middle line is the new one: the string carries the greeting with an empty pair of braces in it, and format is applied to that string with person as its one parameter. That marks where the value of person is substituted. The result is assigned to greeting, and greeting is then printed. Notice no space appears around the exclamation point, with nothing special done to achieve it, because the fixed text says precisely what it wants.

## Files

- [`starter/hello_you3.py`](starter/hello_you3.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `hello_you3.py` the way the lesson builds it:
   - Lines 1–4: asks for the name
   - Lines 5–6: then printed
3. Notes from the lesson:
   - Line 5: the braces mark where the value of person is substituted
4. Run it: `python3 hello_you3.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
Enter your name: Hello, Anna!
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `python3 hello_you3.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
