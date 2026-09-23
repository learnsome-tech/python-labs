# Hands-on Python: Complete Video Course & Book — lesson m10l02 — Mad Libs Revisited: The Whole Program
# https://learnsome.tech/courses/python-course/watch?lesson=m10l02
# © LearnSome.tech
def tellStory(storyFormat):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)
