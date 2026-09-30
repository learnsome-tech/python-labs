# m15l03-14 · Seeing an execution error on purpose

**Lesson:** [CGI: Dynamic Web Pages](https://learnsome.tech/learn/python-course/m15l03) (lesson 15.3, module 15: Dynamic Web Pages) · Pro  
**Check:** Graded

## Goal

You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

In the lesson: You can see that browser trace for yourself. The tutorial suggests putting this one statement into the main function of the adder script, running it, then taking it out. Here it is on its own, so you can read the message you get. A string has no append method; lists do. In Idle such a trace lands in the shell. In a CGI script the same trace is captured by the final block and printed into the page your browser shows.

## Files

- [`starter/bad.py`](starter/bad.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m15l03/m15l03-14/starter`
2. Read `bad.py`.
3. Run it: `python3 bad.py`.
4. Check it from the repository root: `./check m15l03-14`.

## Expected output

```text
Traceback (most recent call last):
AttributeError: 'str' object has no attribute 'append'
```

## How to check

`./check m15l03-14` copies `starter/` into a scratch directory and runs `python3 bad.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
