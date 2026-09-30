# m19l03-02 · sorted against sort

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Four words in the Shell, and one of them with a capital letter. Sorted gives you a new list, in order. Ask for the original again and it has not moved, which is the whole point. Now call the method instead. It prints nothing, and when you look, the list itself has changed. Print what it returned and it gives you back None. And notice the order itself: capital F comes before lower case b, because comparing strings compares character codes, and every capital letter sorts before every small one. That is almost never what a human wants, and fixing it is the next thing we do.

## Files

- [`starter/shell-sorted-against-sort.py`](starter/shell-sorted-against-sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l03/m19l03-02/starter`
2. Read `shell-sorted-against-sort.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['pear', 'Fig', 'banana', 'kiwi']
   sorted(words)
   words
   words.sort()
   words
   print(words.sort())
   ```
4. Run it: `python3 -i < shell-sorted-against-sort.py`.
5. Check it from the repository root: `./check m19l03-02`.

## Expected output

```text
['Fig', 'banana', 'kiwi', 'pear']
['pear', 'Fig', 'banana', 'kiwi']
['Fig', 'banana', 'kiwi', 'pear']
None
```

## How to check

`./check m19l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-sorted-against-sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
