# m14l03 · Graphical Applications With While

Module 14: While Loops · lesson 14.3 · Pro · [Open the lesson](https://learnsome.tech/learn/python-course/m14l03)

**Goal:** You can drive an interactive graphics program with a while loop, decide where to cut a repeating pattern into a loop body, and use checkMouse so an animation continues until the user clicks.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m14l03-02](m14l03-02/) | Imagining a concrete sequence of clicks | Read along |
| [m14l03-03](m14l03-03/) | Where to cut the circle into a loop | Read along |
| [m14l03-04](m14l03-04/) | The last undraw, and how to cancel it | Read along |
| [m14l03-05](m14l03-05/) | The finished polyHere function | Read along |
| [m14l03-06](m14l03-06/) | Calling polyHere twice from main | Read along |
| [m14l03-08](m14l03-08/) | checkMouse looks, getMouse waits | Read along |
| [m14l03-09](m14l03-09/) | Getting a direction from a mouse click | Read along |
| [m14l03-10](m14l03-10/) | Unpacking the shift in bounceBall | Read along |
| [m14l03-11](m14l03-11/) | Remembering which click stopped the loop | Read along |
| [m14l03-12](m14l03-12/) | The outer loop that follows the clicks | Read along |
| [m14l03-14](m14l03-14/) | One loop, three reasons to change direction | Read along |
| [m14l03-15](m14l03-15/) | Exiting from the depths with return | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: moving undraw, and making a path

1. Moving Undraw: write makePoly2.py with the undraw call at the start of the loop body.
2. Move no other statement in the loop; adjust only the code before and after it.
3. Make Path: write makePath.py with pathHere, drawing a segment from each point to the next.
4. Return the list of lines, then recolour one path and rewiden the other in main.

> **Hint:** Drawing a Polygon with an empty vertex list is legal and shows nothing on screen.

### Exercises: random start, mad libs, find the hole

1. Random Start: write startRandom.py so pt and the ball's position are random.
2. Mad Lib While: write madlib4.py, redoing getKeys of madlib2.py with a while loop.
3. Find Hole Game: write findHole.py, where the player clicks to find a hidden circle.
4. Show every point tried, reveal the circle when found, and report the number of steps.

> **Hint:** Distance is dx*dx + dy*dy to the power 0.5; adapt getShift from bounce2.py.

## Check yourself

- Why can a click outside the rectangle serve as a sentinel for the polygon loop?
- Where in the repeating pattern may you cut it into a while loop, and why there?
- Two ways to avoid the unwanted final undraw: what are they, and which is neater?
- How does checkMouse differ from getMouse, and what does it return after no click?
- In bounce four, what ends the loop, given that its condition is permanently True?

---

[Course README](../../README.md) · [Hands-on Python: Complete Video Course & Book on LearnSome.tech](https://learnsome.tech/courses/python-course)
