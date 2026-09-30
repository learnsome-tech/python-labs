# m15l02-08 · Proving it without a browser

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Graded

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: That template step deserves to be seen without a browser in the way, so here is the same machinery with the page printed instead of displayed. The function is the same fileToStr. The name is fixed rather than typed, to keep it short. Then we read the template, call the format method on it, and print the result. Look at what came out. It is the template, character for character, except that the braces have gone and the name sits in the body of the page. That text is exactly what the earlier programs wrote to a file and handed to the browser.

## Files

- [`starter/templateDemo.py`](starter/templateDemo.py): the listing from the lesson
- [`starter/www/helloTemplate.html`](starter/www/helloTemplate.html)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m15l02/m15l02-08/starter`
2. Read `templateDemo.py`.
3. Run it: `python3 templateDemo.py`.
4. Check it from the repository root: `./check m15l02-08`.

## Expected output

```text
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head>
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
  <title>Hello</title></head>

<body>
Hello, Alice!
</body></html>
```

## How to check

`./check m15l02-08` copies `starter/` into a scratch directory and runs `python3 templateDemo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
