def tellStory(storyFormat):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)
