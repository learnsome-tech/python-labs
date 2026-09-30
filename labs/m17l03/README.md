# m17l03 · Reading A Traceback Like A Professional

Module 17: Errors, Exceptions And Debugging · lesson 17.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m17l03)

**Goal:** You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m17l03-02](m17l03-02/) | Four frames, from four real calls | Graded |
| [m17l03-04](m17l03-04/) | When the bottom frame is not your code | Graded |
| [m17l03-06](m17l03-06/) | A syntax error arrives before anything runs | Graded |
| [m17l03-07](m17l03-07/) | IndentationError, its close relative | Graded |
| [m17l03-08](m17l03-08/) | The nine you will meet again and again | Graded |
| [m17l03-09](m17l03-09/) | What each one usually means in practice | Read along |
| [m17l03-10](m17l03-10/) | During handling of the above exception | Graded |

## Check yourself

- In a traceback with four frames, which one is where the exception was raised?
- Why can the fix belong in a frame above the one where the crash happened?
- How do you find the frame to start from when a traceback ends inside a library?
- What tells you at a glance that a program never started running?
- You get an AttributeError saying a NoneType has no such attribute. What is the likely cause?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
