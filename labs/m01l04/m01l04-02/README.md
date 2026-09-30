# m01l04-02 · The shell answers back

**Lesson:** [Editors, IDEs And Shells](https://learnsome.tech/learn/python-course/m01l04) (lesson 1.4, module 1: Before You Write Code) · Free  
**Check:** Graded

## Goal

You can tell a terminal, a shell and a Python shell apart, choose between an interactive shell, an editor with a terminal, and an IDE for a given piece of work, and say what Idle gives you and when to move on from it.

In the lesson: Here is the shell doing its one trick. Type an expression, press return, and it shows you the value. Two plus three gives five. A piece of text gives the text back, wrapped in quotation marks, because it is showing you the value as Python would write it, not as a person would read it. Compare that with the print call underneath: print shows the text with no quotation marks, because print is for a reader rather than for you. Then notice the fourth line. An assignment prints nothing at all. That is not a failure; assigning a value is an instruction, not a question, so there is no answer to show. Ask for the name afterwards and the value is there.

## Files

- [`starter/shell-the-shell-answers-back.py`](starter/shell-the-shell-answers-back.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `shell-the-shell-answers-back.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   2 + 3
   'hello'
   print('hello')
   x = 4
   x * 5
   ```
4. Run it: `python3 -i < shell-the-shell-answers-back.py`.
5. Check it from the repository root: `./check m01l04-02`.

## Expected output

```text
5
'hello'
hello
20
```

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-shell-answers-back.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
