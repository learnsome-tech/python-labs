# m15l03 · CGI: Dynamic Web Pages

Module 15: Dynamic Web Pages · lesson 15.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m15l03)

**Goal:** You can start the local Python web server, read the small CGI scripts the tutorial builds up, and say which of the three places an error will show itself in.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m15l03-03](m15l03-03/) | The example in operation | Read along |
| [m15l03-05](m15l03-05/) | The simplest possible script | Read along |
| [m15l03-06](m15l03-06/) | The same idea, but sending HTML | Read along |
| [m15l03-07](m15l03-07/) | Output that cannot come from a static page | Read along |
| [m15l03-08](m15l03-08/) | Data arriving in the address itself | Read along |
| [m15l03-09](m15l03-09/) | Reading the browser's data | Read along |
| [m15l03-10](m15l03-10/) | Processing, unchanged from the local version | Read along |
| [m15l03-11](m15l03-11/) | The boilerplate you always copy | Read along |
| [m15l03-14](m15l03-14/) | Seeing an execution error on purpose | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Quotient.cgi Exercise

1. Save your quotient web program as quotient.cgi beside localCGIServer.py and your template
2. Merge the standard CGI code from adder.cgi with your own processInput
3. Keep the form data names x and y, so main needs no changes from adder.cgi
4. Test it from the browser address bar, with values typed in after the script name

> **Hint:** Check for syntax errors in Idle, and have the local server running before you try the link.

## Check yourself

- What does the server do with the output your CGI script prints?
- Why can a dot cgi file be edited in Idle but never run there?
- Where does a syntax error in a CGI script appear, and where does an execution error appear?
- What does the first print function in every one of these scripts declare?
- Why can the processing function be copied unchanged from the keyboard version?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
