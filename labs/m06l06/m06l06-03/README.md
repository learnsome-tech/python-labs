# m06l06-03 · Watching a local name disappear

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: You can watch that happen in the Shell in three steps. First define a function that makes a name of its own, y, and prints it. Then call it, and five appears, so the name certainly existed while the call was running. Now ask for it afterwards, on its own, at the prompt. The same NameError. The name y lived only inside that call and vanished when the call finished. A local name is not merely private, it is temporary: it comes into being when the function starts running and is gone by the time you get an answer back. Formal parameters are local names too, made in the same way and lasting exactly as long.

## Files

- [`starter/shell-watching-a-local-name-disappear.py`](starter/shell-watching-a-local-name-disappear.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l06/m06l06-03/starter`
2. Read `shell-watching-a-local-name-disappear.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   def f():
       y = 5
       print(y)
   f()
   y
   ```
4. Run it: `python3 -i < shell-watching-a-local-name-disappear.py`.
5. Check it from the repository root: `./check m06l06-03`.

## Expected output

```text
5
Traceback (most recent call last):
NameError: name 'y' is not defined
```

## How to check

`./check m06l06-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-watching-a-local-name-disappear.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
