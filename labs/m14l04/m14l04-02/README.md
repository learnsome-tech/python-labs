# m14l04-02 · Numbers and None, converted to Boolean

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: Start with numbers and with the special value None. Two is True. Minus three point one is also True, so a negative number is no different. Zero is False. So is the float zero, written with a decimal point, which is a different object but the same numerical value. None, the special object used to indicate the lack of a regular object, is False as well. So far the pattern feels familiar: nothing there means False, and something there means True.

## Files

- [`starter/shell-numbers-and-none-converted-to-boolean.py`](starter/shell-numbers-and-none-converted-to-boolean.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l04/m14l04-02/starter`
2. Read `shell-numbers-and-none-converted-to-boolean.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   bool(2)
   bool(-3.1)
   bool(0)
   bool(0.0)
   bool(None)
   ```
4. Run it: `python3 -i < shell-numbers-and-none-converted-to-boolean.py`.
5. Check it from the repository root: `./check m14l04-02`.

## Expected output

```text
True
True
False
False
False
```

## How to check

`./check m14l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-numbers-and-none-converted-to-boolean.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
