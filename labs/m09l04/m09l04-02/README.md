# m09l04-02 · Splitting a sentence and a word

**Lesson:** [Split And Join](https://learnsome.tech/learn/python-course/m09l04) (lesson 9.4, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can cut a string into a list of parts with split, with or without a separator, glue a sequence of strings back together with join, and use the pair in sequence to rewrite a phrase.

In the lesson: For example, read and follow. Splitting the sentence on white space gives six pieces, one per word, and the full stop stays stuck to the last of them, because a full stop is not white space. Now split Mississippi on the letter i. Every i is removed and the fragments between them come back: M, then s s, then s s, then p p, and then, at the end, the empty string. That last empty piece surprises people, but it is right: the word ends with an i, so there is an empty fragment after the final separator. Finally, split the same word on white space. There is no white space in it at all, so the answer is a list of one element, the whole word.

## Files

- [`starter/shell-splitting-a-sentence-and-a-word.py`](starter/shell-splitting-a-sentence-and-a-word.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l04/m09l04-02/starter`
2. Read `shell-splitting-a-sentence-and-a-word.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   tale = 'This is the best of times.'
   tale.split()
   s = 'Mississippi'
   s.split('i')
   s.split()  # no white space
   ```
4. Run it: `python3 -i < shell-splitting-a-sentence-and-a-word.py`.
5. Check it from the repository root: `./check m09l04-02`.

## Expected output

```text
['This', 'is', 'the', 'best', 'of', 'times.']
['M', 'ss', 'ss', 'pp', '']
['Mississippi']
```

## How to check

`./check m09l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-splitting-a-sentence-and-a-word.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
