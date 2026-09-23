# Hands-on Python: Complete Video Course & Book — lesson m03l01 — A Sample Program, Explained
# https://learnsome.tech/courses/python-course/watch?lesson=m03l01
# © LearnSome.tech
def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)
