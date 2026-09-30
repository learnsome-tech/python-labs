# m09l01-06 · The dot binds tighter than anything else

**Lesson:** [Objects, Methods And String Case](https://learnsome.tech/learn/python-course/m09l01) (lesson 9.1, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can call a method on a string with the object dot method syntax, explain why a string method returns a new string instead of changing the original, and use upper, lower, capitalize, title and count.

In the lesson: Technically the dot between the object and the method name is an operator, and operators have different levels of precedence. It is important to realise that this dot operator has the highest possible precedence there is. So in the first line, upper applies to the word there on its own, and only then is the shouted result concatenated onto hello. Add brackets around the concatenation and upper applies to the whole joined string instead. The same trap turns up with multiplication. Predict these before you read on. In the third line the count runs on a single capital X, and there are no occurrences of three capital X's inside one of them, so the answer is zero. Bracket the multiplication first and you are counting inside a string of three capital X's, which contains exactly one.

## Files

- [`starter/shell-the-dot-binds-tighter-than-anything-else.py`](starter/shell-the-dot-binds-tighter-than-anything-else.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l01/m09l01-06/starter`
2. Read `shell-the-dot-binds-tighter-than-anything-else.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'hello ' + 'there'.upper()
   ('hello ' + 'there').upper()
   3 * 'X'.count('XXX')
   (3 * 'X').count('XXX')
   ```
4. Run it: `python3 -i < shell-the-dot-binds-tighter-than-anything-else.py`.
5. Check it from the repository root: `./check m09l01-06`.

## Expected output

```text
'hello THERE'
'HELLO THERE'
0
1
```

## How to check

`./check m09l01-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-dot-binds-tighter-than-anything-else.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
