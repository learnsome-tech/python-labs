# Hands-on Python: Complete Video Course & Book — lesson m10l02 — Mad Libs Revisited: The Whole Program
# https://learnsome.tech/courses/python-course/watch?lesson=m10l02
# © LearnSome.tech
def addPick(cue, dictionary): # from madlib.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    promptFormat = "Enter a specific example for {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response


def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks
