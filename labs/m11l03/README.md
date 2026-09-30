# m11l03 · Reading The graphics.py Documentation

Module 11: Graphics · lesson 11.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m11l03)

**Goal:** You can find any graphics method for yourself in the reference, by knowing whether it belongs to every graphics object, to one particular type, or to the window, and you know the additions this tutorial makes to Zelle's package.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m11l03-03](m11l03-03/) | The types you can construct | Read along |
| [m11l03-04](m11l03-04/) | The methods every graphics object has | Read along |
| [m11l03-05](m11l03-05/) | The methods that belong to just one type | Read along |
| [m11l03-06](m11l03-06/) | The window has its own methods | Read along |
| [m11l03-07](m11l03-07/) | A tutorial addition: turning the axis the right way up | Read along |
| [m11l03-08](m11l03-08/) | A tutorial addition: promptClose, in two forms | Read along |
| [m11l03-09](m11l03-09/) | A tutorial addition: printing a graphics object | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Scene Exercise

1. Make a program scene.py that creates a scene of your own with the graphics methods.
2. Expect to adjust the positions of objects by trial and error until they look right.
3. Make sure graphics.py is in the same directory as your program.

> **Hint:** Copy the shape of face2.py: the standard opening lines, then your shapes, then promptClose.

### Changing Scene Exercise

1. Elaborate the scene program above so it becomes changeScene.py.
2. It should change one or more times when you click the mouse, using win.getMouse().
3. The click may just mean carry on, or its position may affect what happens next.

> **Hint:** getMouse returns the Point clicked, so you can move objects there, undraw them, or add new ones.

## Check yourself

- Where in the reference do you look for a method that works on every shape?
- Which methods are shared by all graphics objects, and which belong to the window?
- What does yUp change, and when in a program should you call it?
- What are the two ways of calling promptClose, and when would you use each?
- What does printing a graphics object tell you, and what does it not tell you?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
